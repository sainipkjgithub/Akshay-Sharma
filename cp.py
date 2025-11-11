import requests
import json
from script import bot, BASE_PATH
from pyrogram import Client, filters
from cp_create_html import generate_appx_html   # ⚙️ तुम्हारा बनाया हुआ function import
import os
from pyrogram import Client, filters
from pyromod import listen
import requests
import re,os
import json
import asyncio
import base64
import json
from pyrogram import Client, filters
from pyromod import listen
import requests
import asyncio
import base64
import json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import base64
import json
import asyncio
from pyrogram import filters
import base64
import json
import asyncio
from pyrogram import filters
import asyncio
from pyrogram import filters
from cp_txt_extroctor import fetch_classplus_content

def get_org_detalisby_code(org_code):
   url = f"https://api.classplusapp.com/v2/orgs/{org_code}"
   headers = {
    "accept-encoding": "gzip",
    "user-agent": "Mobile-Android",
    }
   try:
       res = requests.get(url, headers=headers)
       res.raise_for_status()
       data = res.json()
       org_id = data["data"]["orgId"]
       print("✅ Org ID:", org_id)
       print("🏫 Org Name:", data["data"]["orgName"])
       return data
   except Exception as e:
       print("⚠️ Error:", e)
       return None

async def generate_classplus_otp(org_id: int, mobile: str):
    """
    Classplus OTP Generate Function
    :param org_code: Organization Code (जैसे 'EPVSB')
    :param mobile: Mobile Number (जैसे '9799138998')
    """

    try:
        # Step 1: Get Organization ID
        # Step 2: Send OTP Request
        api = "https://api.classplusapp.com/v2/otp/generate"

        headers = {
            'accept-encoding': 'gzip',
            'accept-language': 'EN',
            'api-version': '35',
            'app-version': '1.4.73.2',
            'build-number': '35',
            'connection': 'Keep-Alive',
            'content-type': 'application/json',
            'device-details': 'Xiaomi_Redmi 7_SDK-32',
            'device-id': 'c28d3cb16bbdac01',
            'host': 'api.classplusapp.com',
            'region': 'IN',
            'user-agent': 'Mobile-Android',
            'webengage-luid': '00000187-6fe4-5d41-a530-26186858be4c'
        }

        data = {
            "countryExt": "91",
            "mobile": mobile,
            "viaSms": 1,
            "orgId": org_id,
            "eventType": "login",
            "otpHash": "j7ej6eW5VO"
        }

        res = requests.post(api, headers=headers, data=json.dumps(data))
        res.raise_for_status()

        resp_json = res.json()

        if "data" in resp_json and "sessionId" in resp_json["data"]:
            session_id = resp_json["data"]["sessionId"]
            print(f"✅ OTP sent successfully to {mobile}")
            print(f"📩 Session ID: {session_id}")
            return session_id
        else:
            print("⚠️ OTP generation failed:", resp_json)
            return None

    except Exception as e:
        print(f"❌ Error: {e}")
        return None

async def verify_classplus_otp(session_id: str, org_id: int, mobile: str, otp: str):
    try:
        api = "https://api.classplusapp.com/v2/users/verify"

        headers = {
            'accept-encoding': 'gzip',
            'accept-language': 'EN',
            'api-version': '35',
            'app-version': '1.4.73.2',
            'build-number': '35',
            'connection': 'Keep-Alive',
            'content-type': 'application/json',
            'device-details': 'Xiaomi_Redmi 7_SDK-32',
            'device-id': 'c28d3cb16bbdac01',
            'host': 'api.classplusapp.com',
            'region': 'IN',
            'user-agent': 'Mobile-Android',
            'webengage-luid': '00000187-6fe4-5d41-a530-26186858be4c'
        }

        payload = {
            "otp": otp,
            "sessionId": session_id,
            "orgId": org_id,
            "fingerprintId": "a3ee05fbde3958184f682839be4fd0f7",
            "countryExt": "91",
            "mobile": mobile
        }

        # 🔹 request भेजो (raise_for_status हटाया गया)
        res = requests.post(api, headers=headers, data=json.dumps(payload))

        # 🔹 हर हालत में JSON parse करने की कोशिश करो
        try:
            resp_json = res.json()
        except Exception:
            return {
                "status": "error",
                "message": f"Invalid JSON response: {res.text}"
            }

        # 🔹 अब 200 या 409 — दोनों में एक जैसा response logic
        if (
            resp_json.get("status") == "success"
            and "data" in resp_json
            and "token" in resp_json["data"]
        ):
            user_info = resp_json["data"].get("user", {})
            token = resp_json["data"].get("token")
            name = user_info.get("name", "Unknown")
            user_id = user_info.get("id")

            return {
                "status": "success",
                "message": resp_json.get("message", "OTP verified successfully"),
                "token": token,
                "user_id": user_id,
                "name": name
            }

        # 🔹 अब 409 या कोई और failure यहाँ आएगा
        return {
            "status": resp_json.get("status", "failure"),
            "message": resp_json.get("message", "Unknown error"),
            "data": resp_json.get("data", [])
        }

    except Exception as e:
        print(f"❌ Error verifying OTP: {e}")
        return {
            "status": "error",
            "message": f"Exception: {e}"
        }
def extract_user_id_from_token(token: str):
    try:
        # Token को 3 हिस्सों में बाँटते हैं (header.payload.signature)
        parts = token.split('.')
        if len(parts) != 3:
            raise ValueError("Invalid token format")

        payload_b64 = parts[1]
        
        # Base64 padding सही करना (JWT में '=' हटाया होता है)
        padding = len(payload_b64) % 4
        if padding:
            payload_b64 += '=' * (4 - padding)
        
        # Decode payload
        decoded_bytes = base64.urlsafe_b64decode(payload_b64)
        payload_data = json.loads(decoded_bytes.decode('utf-8'))

        # User ID निकालना
        user_id = payload_data.get("id")
        return user_id

    except Exception as e:
        print("Error decoding token:", e)
        return None
def get_purchased_courses(token: str):
    user_id = int(extract_user_id_from_token(token))
    try:
        api = f"https://api.classplusapp.com/v2/profiles/users/data?userId={user_id}&tabCategoryId=3"

        headers = {
            'accept-encoding': 'gzip',
            'accept-language': 'EN',
            'api-version': '35',
            'app-version': '1.4.73.2',
            'build-number': '35',
            'connection': 'Keep-Alive',
            'content-type': 'application/json',
            'device-details': 'Xiaomi_Redmi 7_SDK-35',
            'device-id': 'c28d3cb16bbd78899',
            'host': 'api.classplusapp.com',
            'region': 'IN',
            'user-agent': 'Mobile-Android',
            'webengage-luid': '00000187-6fe4-5d41-a530-858be4c',
            'x-access-token': token
        }

        res = requests.get(api, headers=headers)
        res.raise_for_status()

        data = res.json()

        # Extract course list
        courses = data.get("data", {}).get("responseData", {}).get("coursesData", [])

        purchased_courses = []

        for c in courses:
            if c.get("isPurchased") == 1:  # purchased course check
                purchased_courses.append({
                    "course_id": c.get("id"),
                    "org_id": c.get("orgId"),
                    "course_name": c.get("name"),
                    "expires_at": c.get("expiresAt"),
                    "final_price": c.get("finalPrice"),
                    "resources": c.get("resources", {}),
                    "image_url": c.get("imageUrl"),
                })

        print(json.dumps(purchased_courses, indent=2))
        return 200, purchased_courses

    except Exception as e:
        print(f"❌ Error fetching purchased courses: {e}")
        return 404, []

@bot.on_message(filters.command("cp_gen_token") & filters.private)
async def generate_token_handler(_, message):
    try:
        # 1️⃣ Ask for Organization Code
        await message.reply_text("Please send your **Organization Code**:")
        org_msg = await bot.listen(message.chat.id, timeout=60)
        org_code = org_msg.text.strip()

        if not org_code:
            await message.reply_text("❌ Organization Code is empty. Please run `/cp_gen_token` again and provide a valid code.")
            return

        # 2️⃣ Ask for Mobile Number
        msg = await message.reply_text(f"Please Wait Checking...")
        org_data = get_org_detalisby_code(org_code)
        if org_data:
           org_id = org_data["data"]["orgId"]
           org_name = org_data["data"]["orgName"]
        else:
          await msg.edit_text("Wrong Organization Id Please Double check it.🫣")
          return
        await msg.edit_text(f"""
**Your Organization Details**
**Org Code** : `{org_code}`
**Org ID** : `{org_id}`
**Org Name** : `{org_name}`


Now send your **Mobile Number (10 digits, without +91):**""")
        mb_msg = await bot.listen(message.chat.id, timeout=60)
        mobile = mb_msg.text.strip()

        if not mobile.isdigit() or len(mobile) != 10:
            await message.reply_text("❌ Invalid mobile number. Please send 10 digits only (without +91).")
            return

        # 3️⃣ Generate OTP
        msg = await message.reply_text("🔄 Generating OTP... Please wait.")
        try:
            session_id = await generate_classplus_otp(org_id, mobile)
        except Exception as e:
            await msg.edit_text(f"❌ Error generating OTP:\n`{e}`")
            return

        if not session_id:
            await msg.edit_text("❌ Server did not return a valid session ID. Please check your Organization Code.")
            return

        # 4️⃣ Ask for OTP
        await msg.edit_text("📩 Please send the OTP you received:")
        otp_msg = await bot.listen(message.chat.id, timeout=120)
        otp = otp_msg.text.strip()

        if not otp.isdigit():
            await message.reply_text("❌ Invalid OTP format. Only numeric values are accepted.")
            return

        # 5️⃣ Verify OTP
        msg = await message.reply_text("🔐 Verifying OTP... Please wait.")
        try:
            verify_resp = await verify_classplus_otp(
                session_id=session_id,
                org_id=org_id,
                mobile=mobile,
                otp=otp
            )
        except Exception as e:
            await msg.edit_text(f"❌ Error verifying OTP:\n`{e}`")
            return

        # 6️⃣ Handle structured response
        if not isinstance(verify_resp, dict):
            await msg.edit_text(f"⚠️ Unexpected server response:\n`{verify_resp}`")
            return

        status = verify_resp.get("status", "error").lower()
        msg_text = verify_resp.get("message", "No message provided by server.")

        if status == "success":
            token = verify_resp.get("token")
            name = verify_resp.get("name", "User")

            if token:
                await msg.edit_text(
                    f"✅ **OTP Verified Successfully!**\n\n"
                    f"👤 Name: `{name}`\n"
                    f"📱 Mobile: `{mobile}`\n"
                    f"🔑 **Access Token:**\n`{token}`"
                )
            else:
                await msg.edit_text(
                    f"This number is not registered with {org_name}. Please sign up on the App or [Website](https://web.classplusapp.com/login?orgCode={org_code}), complete your profile, and then try again."
                )

        elif status == "failure":
            await msg.edit_text(
                f"❌ **OTP Verification Failed!**\n\nServer message: `{msg_text}`"
            )

        else:
            await msg.edit_text(
                f"⚠️ Unexpected response.\n\nStatus: `{status}`\nMessage: `{msg_text}`"
            )

    except asyncio.TimeoutError:
        await message.reply_text("⏰ Timeout! Please run `/cp_gen_token` again and try once more.")

    except Exception as e:
        await message.reply_text(f"⚠️ Unexpected Error:\n`{e}`")
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

temp_tokens = {}

@bot.on_message(filters.command("cp_my_course") & filters.private)
async def cp_my_course_handler(_, message):
    user_id = message.from_user.id
    try:
        # Ask for token (or ask to get one)
        await message.reply_text(
            "Please send your Classplus token.\n"
            "/cp_gen_token\n"
            "/skip"
        )

        # wait for user's reply (token or /cp_gen_token or /skip)
        reply = await bot.listen(message.chat.id, timeout=180)
        text = reply.text.strip() if reply.text else ""

        # allow user to cancel
        if text.lower() == "/skip":
            await message.reply_text("Operation cancelled.")
            return

        # if user typed the command to generate token, instruct them and wait for token
        if text.startswith("/cp_gen_token"):
            await message.reply_text("Please send /cp_gen_token again...")
            return

        token = text  # assume whatever user sent now is token
        if not token:
            await message.reply_text("No token provided. Aborting.")
            return

        # store temp token mapped to Telegram user id
        temp_tokens[user_id] = token

        msg = await message.reply_text("Token received. Fetching your purchased courses...")

        # get purchased courses (await assumed)
        try:
            status, purchased = await get_purchased_courses(token)
        except TypeError:
            # if get_purchased_courses is sync, call it directly
            status, purchased = get_purchased_courses(token)
        except Exception as e:
            await msg.edit_text(f"Error fetching courses: `{e}`")
            return

        if not purchased:
            if status == 200:
               await msg.edit_text("No purchased courses found for this account.")
               return
            await msg.edit_text("⚠️ Invalid or Expired Token")
            return

        # Build list of names in order
        lines = []
        for idx, c in enumerate(purchased, start=1):
            name = c.get("course_name") or c.get("name") or "Unnamed course"
            expires = c.get("expires_at") or "N/A"
            lines.append(f"{idx}. {name} (expires: {expires})")

        list_text = "Your purchased courses:\n\n" + "\n".join(lines)
        list_text += "\n\nSend the serial number (e.g. `1`) of the course you want."
        await msg.edit_text(list_text)

        # Wait for user to send serial number
        try:
            sel_msg = await bot.listen(message.chat.id, timeout=120)
            sel_text = sel_msg.text.strip() if sel_msg.text else ""
        except asyncio.TimeoutError:
            await message.reply_text("Timeout waiting for selection. Please run /cp_my_course again.")
            return

        if not sel_text.isdigit():
            await message.reply_text("Invalid input. Please send the numeric serial number of the course.")
            return

        sel_index = int(sel_text) - 1
        if sel_index < 0 or sel_index >= len(purchased):
            await message.reply_text("Selection out of range. Operation cancelled.")
            return

        course = purchased[sel_index]
        course_id = course.get("course_id") or course.get("id")
        org_id = course.get("org_id") or course.get("orgId")
        name = course.get("course_name") or course.get("name") or "Unnamed course"
        expires_at = course.get("expires_at") or course.get("expiresAt") or "N/A"
        final_price = course.get("final_price") or course.get("finalPrice") or "N/A"
        resources = course.get("resources", {})
        image_url = course.get("image_url") or course.get("imageUrl")

        # build caption / message with all details
        detail_lines = [
            f"Course Name: {name}",
            f"Course ID: {course_id}",
            f"Organization ID: {org_id}",
            f"Expires At: {expires_at}",
            f"Final Price: {final_price}",
            f"Resources: {json.dumps(resources) if resources else 'None'}"
        ]
        caption = "\n".join(detail_lines)

        # inline confirm button
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Yes Confirm", callback_data=f"get_cp_course_{course_id}")]]
        )

        # try to send image if available
        if image_url:
            try:
                await message.reply_photo(photo=image_url, caption=caption, reply_markup=keyboard)
            except Exception:
                # fallback to text if sending image failed
                await message.reply_text(caption, reply_markup=keyboard)
        else:
            # no image, send as text with button
            await message.reply_text(caption, reply_markup=keyboard)

    except asyncio.TimeoutError:
        await message.reply_text("Timeout. Please run /cp_my_course again to start over.")
    except Exception as e:
        await message.reply_text(f"Unexpected error: `{e}`")


from pyrogram import filters
from pyrogram.types import CallbackQuery
import os
import asyncio

@bot.on_callback_query(filters.regex(r"^get_cp_course_(\d+)$"))
async def handle_course_callback(_, query: CallbackQuery):
    user_id = query.from_user.id
    course_id = int(query.data.split("_")[-1])

    # Check if token exists for this user
    token = temp_tokens.get(user_id)
    if not token:
        await query.message.reply_text(
            "❌ Token not found. Please run `/cp_my_course` again and provide a valid token."
        )
        return

    # Define file path for saving
    file_dir = f"{BASE_PATH}/ClassPlus-txts"
    os.makedirs(file_dir, exist_ok=True)
    file_path = f"{file_dir}/{course_id}.txt"

    # Inform user
    await query.message.reply_text("📦 Fetching course content... Please wait.")

    try:
        # Fetch content using your custom function
        await fetch_classplus_content(
            token,
            course_id,
            file_path=file_path
        )

        # Send the file to user
        if os.path.exists(file_path):
            await query.message.reply_document(
                document=file_path,
                caption=f"✅ Course content for ID `{course_id}`"
            )
        else:
            await query.message.reply_text("⚠️ File not found after fetching. Something went wrong.")

    except asyncio.TimeoutError:
        await query.message.reply_text("⏰ Timeout while fetching course data.")
    except Exception as e:
        await query.message.reply_text(f"❌ Error fetching course:\n`{e}`")
        
@bot.on_message(filters.command("cp_create_html") & filters.private)
async def create_html_from_txt(bot, message):
    # ✅ यूज़र ने किसी txt फाइल को reply में भेजा है क्या?
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply_text("कृपया किसी .txt फाइल को reply करके यह कमांड भेजें 📄")
        return

    doc = message.reply_to_message.document

    # ⚙️ केवल .txt फाइलों पर ही काम करे
    if not doc.file_name.endswith(".txt"):
        await message.reply_text("❌ यह .txt फाइल नहीं है। कृपया सही फाइल दें।")
        return

    # ⬇️ फाइल डाउनलोड करें
    status = await message.reply_text("⏳ फाइल डाउनलोड की जा रही है...")
    download_path = await bot.download_media(doc, file_name=f"{BASE_PATH}/tmp/{doc.file_name}")
    output_path = download_path.replace(".txt", ".html")
    try:
        # 🔧 HTML जेनरेट करें
        await status.edit("⚙️ HTML जेनरेट हो रही है...")
        output_path = generate_appx_html(download_path, output_path)

        if output_path and os.path.exists(output_path):
            await status.edit("✅ HTML तैयार हो गया, भेजा जा रहा है...")
            await message.reply_document(
                document=output_path,
                caption=f"✅ HTML फ़ाइल तैयार: `{os.path.basename(output_path)}`"
            )
        else:
            await status.edit("❌ HTML बनाने में समस्या आई।")
    except Exception as e:
        await status.edit(f"⚠️ त्रुटि: {e}")
    finally:
        # 🧹 Cleanup
        if os.path.exists(download_path):
            os.remove(download_path)
