from pyrogram import Client, filters
from pyromod import listen
import requests
import re,os
import json
import asyncio

from pyrogram import Client, filters
from pyromod import listen
import requests
import asyncio
import base64
import json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import bot, BASE_PATH
import cp
# ──────────────── /cp Command ────────────────
@bot.on_message(filters.command("cp_start") & filters.private)
async def get_hash(_, message):
    await message.reply_text("I am alive\n/cp")
    
@bot.on_message(filters.command("cp") & filters.private)
async def get_hash(_, message):
    await message.reply_text("कृपया Organization hash भेजें\n\n/gethash कमांड से इसे प्राप्त करें।")

    try:
        org_msg = await bot.listen(message.chat.id, timeout=60)
        org_hash = org_msg.text.strip()

        # base64 → decode → JSON → orgId
        decoded = base64.b64decode(org_hash).decode("utf-8")
        org_data = json.loads(decoded)
        org_id = org_data.get("orgId")

        if not org_id:
            await message.reply_text("❌ Invalid hash, orgId नहीं मिला।")
            return

        await send_courses_unified(message, org_hash, start=0, limit=5)

    except asyncio.TimeoutError:
        await message.reply_text("⏰ समय समाप्त! कृपया पुनः प्रयास करें।")
    except Exception as e:
        await message.reply_text(f"⚠️ त्रुटि:\n`{e}`")

def make_org_hash(org_id: int) -> str:
    """org_id से base64 encoded hash बनाता है"""
    data = {
        "tutorId": None,
        "orgId": org_id,
        "categoryId": None
    }
    json_str = json.dumps(data, separators=(",", ":"))  # compact JSON
    encoded = base64.b64encode(json_str.encode("utf-8")).decode("utf-8")
    return encoded

import os
import json
import base64
import requests
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import base64, json, os, asyncio

# Global dict to track courses per chat
user_course_map = {}

async def send_courses_unified(message, org_hash, start=0, limit=5, search_query=None, edit=False):
    """
    📚 Unified function to show courses with pagination, search, and select by serial number
    """
    url = f"https://api.classplusapp.com/v2/course/preview/similar/{org_hash}?limit=9999"
    if search_query:
        url += f"&search={search_query}"

    headers = {
        "accept-encoding": "gzip",
        "accept-language": "EN",
        "api-version": "35",
        "app-version": "1.4.73.2",
        "build-number": "35",
        "connection": "Keep-Alive",
        "device-details": "Xiaomi_Redmi 7_SDK-32",
        "device-id": "c28d3cb16bbdac01",
        "host": "api.classplusapp.com",
        "region": "IN",
        "user-agent": "Mobile-Android",
        "webengage-luid": "00000187-6fe4-5d41-a530-26186858be4c"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if data.get("status") != "success":
            text = "❌ डेटा प्राप्त करने में समस्या हुई।"
            if edit:
                await message.edit_text(text)
            else:
                await message.reply_text(text)
            return

        courses = data["data"]["coursesData"]
        total = len(courses)

        decoded = base64.b64decode(org_hash).decode("utf-8")
        org_data = json.loads(decoded)
        org_id = org_data.get("orgId")

        slice_courses = courses[start:start + limit]
        if not slice_courses:
            text = "📭 और कोई कोर्स नहीं मिला।"
            if edit:
                await message.edit_text(text)
            else:
                await message.reply_text(text)
            return

        # Page count
        current_page = (start // limit) + 1
        total_pages = (len(courses) + limit - 1) // limit

        # Message text
        text = f"🎓 **Available Courses**\n📑 Page: {current_page}/{total_pages}\n"
        if search_query:
            text += f"🔍 Search: `{search_query}`\n"
        text += "\n"

        course_map = {}
        for i, c in enumerate(slice_courses, start=start + 1):
            text += f"{i}. {c['name']}\n"
            course_map[str(i)] = c["id"]  # serial number → course_id

        # Save course_map for this chat
        user_course_map[message.chat.id] = {"course_map": course_map, "org_id": org_id}

        # Pagination buttons
        nav_buttons = []
        if start > 0:
            nav_buttons.append(
                InlineKeyboardButton(
                    "⬅️ Previous", callback_data=f"cp_prev_{org_id}_{start - limit}" + (f"_{search_query}" if search_query else "")
                )
            )
        if start + limit < total:
            nav_buttons.append(
                InlineKeyboardButton(
                    "➡️ Next", callback_data=f"cp_next_{org_id}_{start + limit}" + (f"_{search_query}" if search_query else "")
                )
            )

        # Search button
        search_button = [InlineKeyboardButton("🔍 Search", callback_data=f"cp_search_{org_id}")]

        keyboard = []
        if nav_buttons:
            keyboard.append(nav_buttons)
        keyboard.append(search_button)
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send or edit
        if edit:
            await message.edit_text(text, reply_markup=reply_markup)
        else:
            await message.reply_text(text, reply_markup=reply_markup)

    except Exception as e:
        error_text = f"⚠️ डेटा लाने में त्रुटि:\n`{e}`"
        if edit:
            await message.edit_text(error_text)
        else:
            await message.reply_text(error_text)


# ---------------- User selection handler -----------------

@bot.on_callback_query(filters.regex(r"^cp_"))
async def paginate(bot, query):
    try:
        parts = query.data.split("_")
        action = parts[1]   # next / prev / search
        org_id = int(parts[2])

        # ✅ Search Mode
        if action == "search":
            await query.answer()
            await query.message.delete()
            ask = await query.message.reply_text("🔍 Please Send a search query:")
            search_msg = await bot.listen(query.message.chat.id, timeout=60)
            search_query = search_msg.text.strip()
            await ask.edit_text(f"Searching Please Wait...: `{search_query}` ...")

            org_hash = make_org_hash(org_id)
            await send_courses_unified(query.message, org_hash, start=0, limit=5, search_query=search_query)
            await ask.delete()
            return

        # ✅ Pagination Mode
        start = int(parts[3])
        search_query = None
        if len(parts) > 4:
            search_query = "_".join(parts[4:])  # यदि search active है तो उसे बनाए रखे

        org_hash = make_org_hash(org_id)
        await query.answer("⏳ Loading more courses...")
        await send_courses_unified(query.message, org_hash, start=start, limit=5, search_query=search_query, edit=True)
        #await send_courses_unified(query.message, org_hash, start=5, edit=True)

    except Exception as e:
        await query.message.reply_text(f"⚠️ Pagination Error:\n`{e}`")
@bot.on_message(filters.command("gethash") & filters.private)
async def get_hash(_, message):
    await message.reply_text("🔢 कृपया Organization Code भेजें... (उदा: epvsb)")

    try:
        # यूज़र से org code लो
        org_msg = await bot.listen(message.chat.id, timeout=60)
        org_code = org_msg.text.strip().lower()

        await message.reply_text(f"🔍 `{org_code}` का डेटा प्राप्त किया जा रहा है... कृपया प्रतीक्षा करें...")

        url = f"https://{org_code}.courses.store/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/128.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            await message.reply_text("❌ अमान्य Organization Code या सर्वर उपलब्ध नहीं है।")
            return

        html = response.text

        # Script JSON खोजें
        match = re.search(
            r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
            html,
            re.S
        )

        if not match:
            await message.reply_text("⚠️ JSON स्क्रिप्ट नहीं मिली — पेज स्ट्रक्चर बदला हो सकता है।")
            return

        json_text = match.group(1)

        try:
            data = json.loads(json_text)
            # JSON से hash निकालना
            hash_value = data["props"]["pageProps"]["_infoData"]["success"]["data"]["hash"]
            org_name = data["props"]["pageProps"]["_infoData"]["success"]["data"].get("name", "Unknown")
            org_id = data["props"]["pageProps"]["_infoData"]["success"]["data"].get("orgId", "N/A")

            await message.reply_text(
                f"✅ **Hash Details Found!**\n\n"
                f"🏢 **Organization:** `{org_name}`\n"
                f"🆔 **Org ID:** `{org_id}`\n"
                f"🔹 **Code:** `{org_code}`\n"
                f"🔑 **Hash:** `{hash_value}`"
            )

        except Exception as e:
            await message.reply_text(f"Please Send a valid Organization code.\n`{e}`")

    except asyncio.TimeoutError:
        await message.reply_text("⌛ समय समाप्त — कृपया फिर से प्रयास करें।")
    except Exception as e:
        await message.reply_text(f"🚫 त्रुटि हुई:\n`{e}`")

import requests
import json
import base64
import asyncio
import os

# ─────────────── Helper Function ───────────────
def make_course_hash(course_id, org_id, tutor_id=None, category_id=None):
    data = {"courseId": str(course_id), "orgId": org_id, "tutorId": tutor_id, "categoryId": category_id}
    return base64.b64encode(json.dumps(data).encode()).decode()

# ─────────────── Recursive Fetch Function ───────────────
import re
import requests

def convert_url(url_val):  
    if not url_val:  
        return None  

    if "media-cdn.classplusapp.com/tencent/" in url_val:  
        return url_val.rsplit('/', 1)[0] + "/master.m3u8"  

    elif "media-cdn.classplusapp.com" in url_val and url_val.endswith('.jpg'):  
        identifier = url_val.split('/')[-3]  
        return f"https://media-cdn.classplusapp.com/alisg-cdn-a.classplusapp.com/{identifier}/master.m3u8"  

    elif "tencdn.classplusapp.com" in url_val and url_val.endswith('.jpg'):  
        identifier = url_val.split('/')[-2]  
        return f"https://media-cdn.classplusapp.com/tencent/{identifier}/master.m3u8"  

    elif "4b06bf8d61c41f8310af9b2624459378203740932b456b07fcf817b737fbae27" in url_val and url_val.endswith('.jpeg'):  
        identifier = url_val.split('/')[-1].split('.')[0]  
        return f"https://media-cdn.classplusapp.com/alisg-cdn-a.classplusapp.com/b08bad9ff8d969639b2e43d5769342cc62b510c4345d2f7f153bec53be84fe35/{identifier}/master.m3u8"  

    elif "cpvideocdn.testbook.com" in url_val and url_val.endswith('.png'):  
        match = re.search(r'/streams/([a-f0-9]{24})/', url_val)  
        video_id = match.group(1) if match else url_val.split('/')[-2]  
        return f"https://cpvod.testbook.com/{video_id}/playlist.m3u8"  

    elif "media-cdn.classplusapp.com/drm/" in url_val and url_val.endswith('.png'):  
        video_id = url_val.split('/')[-3]  
        return f"https://media-cdn.classplusapp.com/drm/{video_id}/playlist.m3u8"  

    elif "https://media-cdn.classplusapp.com" in url_val and ("cc/" in url_val or "lc/" in url_val or "uc/" in url_val or "dy/" in url_val) and url_val.endswith('.png'):  
        return url_val.replace('thumbnail.png', 'master.m3u8')  

    elif "https://tb-video.classplusapp.com" in url_val and url_val.endswith('.jpg'):  
        video_id = url_val.split('/')[-1].split('.')[0]  
        return f"https://tb-video.classplusapp.com/{video_id}/master.m3u8"  

    elif url_val.endswith('.png'):  
        return url_val.rsplit('/', 1)[0] + "/master.m3u8"  

    return url_val  


async def fetch_course_content(course_id, org_id, txt_path, parent_folder=None, folder_id=0):
    course_hash = make_course_hash(course_id, org_id)

    url = f"https://api.classplusapp.com/v2/course/preview/content/list/{course_hash}?folderId={folder_id}&limit=9999"
    headers = {
        "accept-encoding": "gzip",
        "user-agent": "Mobile-Android",
        "api-version": "35",
        "x-access-token": "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTMwMTI0MTUyLCJvcmdJZCI6MTM4MjQsInR5cGUiOjEsIm1vYmlsZSI6IjkxOTExOTIwMTAzMyIsIm5hbWUiOiJEZWVwYWsgS3VtYXIiLCJlbWFpbCI6ImdhZHdhbGRlZXBhazk0QGdtYWlsLmNvbSIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5Ijp0cnVlLCJvcmdDb2RlIjoiZXB2c2IiLCJpc0RpeVN1YmFkbWluIjowLCJmaW5nZXJwcmludElkIjoiMTcyMDEwMDQzODY4NyIsImlhdCI6MTc2MTMwNjkyOCwiZXhwIjoxNzYxOTExNzI4fQ.fBWJdxFCtnk3D9uWc2r_ca1xhVyB91N1i14xcaZYnNo1hrxzkQ5LYbIHno6JI3iq"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get("status") != "success":
        print(f"❌ Failed to fetch content for folder {parent_folder}")
        return

    for item in data.get("data", []):
        if item.get("contentType") == 1:  # Folder
            sub_folder_name = item.get("name", "Unnamed Folder")
            if parent_folder: 
                await fetch_course_content(course_id, org_id, txt_path, parent_folder=f"{parent_folder} > {sub_folder_name}", folder_id=item["id"])
            else:
                await fetch_course_content(course_id, org_id, txt_path, parent_folder=f"{sub_folder_name}", folder_id=item["id"])

        elif item.get("contentType") == 2:  # Lecture
            lecture_name = item.get("name", "Unnamed Lecture")
            thumb_url = item.get("thumbnailUrl") or ""
            video_url = convert_url(thumb_url) if thumb_url else "N/A"

            if parent_folder:
                line = f"{parent_folder} > {lecture_name}: {video_url}\n"
            else:
                line = f"{lecture_name}: {video_url}\n"

            with open(txt_path, "a", encoding="utf-8") as f:
                f.write(line)
            print(line.strip())

# ─────────────── Main Function ───────────────
async def start_course_fetch(course_id, org_id, txt_file=f"{BASE_PATH}/course_content.txt"):
    # फ़ाइल clear कर दो
    if os.path.exists(txt_file):
        os.remove(txt_file)

    await fetch_course_content(course_id, org_id, txt_file)
    print(f"\n✅ Finished! Saved in {txt_file}")

@bot.on_message(filters.text & filters.create(lambda _, __, msg: msg.chat.id in user_course_map))
async def handle_course_selection(client, message):
    chat_id = message.chat.id
    selected = message.text.strip()

    course_info = user_course_map[chat_id]
    course_map = course_info["course_map"]
    org_id = course_info["org_id"]

    if selected not in course_map:
        await message.reply_text("⚠️ कृपया सही नंबर भेजें।")
        return

    course_id = course_map[selected]
    await message.reply_text("⏳ चयनित कोर्स का कंटेंट लाया जा रहा है...")

    txt_file = f"{BASE_PATH}/{course_id}.txt"
    if os.path.exists(txt_file):
        os.remove(txt_file)

    # Async content fetch
    await start_course_fetch(course_id, org_id, txt_file=txt_file)

    # Send the fetched file
    await bot.send_document(chat_id=chat_id, document=txt_file)
    os.remove(txt_file)

    # Cleanup
    user_course_map.pop(chat_id, None)
#print("🤖 Bot चालू हो गया...")
#bot.run()
