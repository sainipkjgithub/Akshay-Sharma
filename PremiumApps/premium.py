"""
JAY SHREE RAM
"""
"""
FUNCTIONS Here 
#search_and_send_inline,search_and_send_app,send_document
"""
##Imports
import requests
import json
import sys
import os
##Imports#From Pyrogran 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,InputMediaPhoto, CallbackQuery

#From Previous Folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from script import FILE_CHANNEL_ID,user_status,BOT_TOKEN, temp_data,SEARCH_URL,user_status

saveii = {}
#Main Functions Started
async def search_and_send_inline(msg, search_query, page=1):
    response = requests.get(SEARCH_URL + search_query)
    user_id = msg.chat.id
    if user_id not in saveii:
        saveii[user_id] = {}
    if response.status_code != 200:
        await msg.edit("Error Searching App")
        return
    saveii[user_id]['page'] = page
    saveii[user_id]['search_query'] = search_query
    apps = response.json()
    if not apps:
        await msg.edit("No App found")
        return

    results_per_page = 10
    total_pages = (len(apps) + results_per_page - 1) // results_per_page  # कुल पेज
    
    # पेज इंडेक्स सेट करें
    start_idx = (page - 1) * results_per_page
    end_idx = start_idx + results_per_page
    apps = apps[start_idx:end_idx]  # सिर्फ़ 10 परिणाम फ़िल्टर करें
    if user_id in user_status:
       del user_status[user_id]
    buttons = []
    row = []

    for idx, app in enumerate(apps):
        short_id = f"app_{start_idx + idx}"  # यूनिक Short ID
        temp_data[short_id] = app["file_id"]

        row.append(InlineKeyboardButton(app["file_name"], callback_data=f"pre_{short_id}"))

        if len(row) == 2:
            buttons.append(row)
            row = []

    if row:
        buttons.append(row)

    # पेज नेविगेशन बटन
    nav_buttons = []
    if page > 1:
        nav_buttons.append(InlineKeyboardButton("⬅ Previous", callback_data=f"page_{page-1}_{search_query}"))
    if total_pages == 1:
      nav_buttons.append(InlineKeyboardButton("🔍 Search Again", callback_data=f"premium_apps"))
    if total_pages > 1:
      nav_buttons.append(InlineKeyboardButton(f"{page}/{total_pages}", callback_data=f"premium_apps"))
    if page < total_pages:
        nav_buttons.append(InlineKeyboardButton("Next ➡", callback_data=f"page_{page+1}_{search_query}"))

    if nav_buttons:
        buttons.append(nav_buttons)

    await msg.edit(
        f"Here is your Search Result For : \n**{search_query}** \n\n Please Choose An App:\n",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    return temp_data  # Short IDs को बाद में एक्सेस करने के लिए रिटर्न करें


async def search_and_send_app(client, msg, file_id):
    try:
        chat_id = msg.chat.id
        res = send_document(chat_id, file_id, caption="Enjoy This😊😊", protect_content=True, parse_mode="HTML")
        if res =="OK":
          await msg.delete()
        elif res =="ER":
          await msg.edit("Failed to send the file. pleaee contect to admin")
        
    except Exception as e:
        await msg.edit("Failed to send the file.")
        print(f"Error: {e}")

def send_document(chat_id, file_id, caption="", protect_content=True, parse_mode="HTML"):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    user_id = chat_id
    print(saveii)
    print(saveii[user_id])
    search_query = saveii[user_id]['search_query'] 
    page = saveii[user_id]['page']
    keyboard = {
        "inline_keyboard": [
            [{"text": "🔍Search Again", "callback_data": "premium_apps"}],
            [{"text": "🔙Back", "callback_data": f"page_{page}_{search_query}"},
            {"text": "🏠 Home", "callback_data": "home"}]
        ]
    }
    
    payload = {
        "chat_id": chat_id,
        "document": file_id,
        "caption": caption,
        "protect_content": protect_content,
        "parse_mode": parse_mode,
        "reply_markup": json.dumps(keyboard)  
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return "OK"
    else:
        return "ER"
async def premiumcall12345(client, query):
  if query.data.startswith("page_"):
        _, page, search_query = query.data.split("_")
        page = int(page)
    
        msg = query.message
        await search_and_send_inline(msg, search_query, page)  
async def premium_app_send(client, query):
      user_id = query.from_user.id  # Get user ID
      user_name = query.from_user.first_name  # Extract user name
      if query.data.startswith("pre_"):
        short_id = query.data[4:]  # "pre_" के बाद का टेक्स्ट निकालें
        file_id = temp_data.get(short_id)  # Short ID से असली File ID प्राप्त करें
        if not file_id:
           await query.answer("File not found!", show_alert=True)
           return
        msg = await query.message.reply_text("Please Wait...")
        await query.message.delete()
        await search_and_send_app(client, msg, file_id)
