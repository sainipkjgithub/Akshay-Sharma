"""
JAY SHREE RAM
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,InputMediaPhoto
import requests
APP_DETAILS_URL = "https://sainipankaj12.serv00.net/App/get.php?app_name="
SEARCH_URL = "https://sainipankaj12.serv00.net/App/index.php?query="


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from script import FILE_CHANNEL_ID



def search_and_send_inline(msg, search_query):
    response = requests.get(SEARCH_URL + search_query)
    if response.status_code != 200:
        msg.edit("Error Searching App")
        return
    
    apps = response.json()
    
    if not apps:
        msg.edit("No App found")
        return

    # 2 कॉलम में बटन दिखाने के लिए लिस्ट को विभाजित करें
    buttons = []
    row = []
    for app in apps:
        row.append(InlineKeyboardButton(app["name"], callback_data=f"pre_{app['name']}"))
        if len(row) == 2:  # 2 कॉलम पूरे होने पर नई रो बनाएँ
            buttons.append(row)
            row = []
    
    # अगर कोई बटन बचा रह जाए तो उसे भी जोड़ें
    if row:
        buttons.append(row)

    msg.edit(
        "Please Choose An App :",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

"""
JAY SHREE RAM
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import requests

APP_DETAILS_URL = "https://sainipankaj12.serv00.net/App/get.php?app_name="

def search_and_send_app(client, msg, app_name):
    response = requests.get(APP_DETAILS_URL + app_name)
    if response.status_code != 200:
        msg.edit("❌ Error: Unable to fetch app details. Please contact the admin.")
        return
    
    try:
        app_json = response.json()
    except ValueError:
        msg.edit("❌ Error: Invalid response from the server. Please contact the admin.")
        return

    if app_json.get("status") != "success" or "data" not in app_json:
        msg.edit("⚠️ No premium app found for your query. Please contact the admin.")
        return

    app_data = app_json["data"]
    file_versions = app_data.get("File ID", [])

    if not file_versions:
        msg.edit("⚠️ No versions available for this app.")
        return

    # 🔹 **Inline Keyboard for Version Selection**
    buttons = [
        [InlineKeyboardButton(f"{file['version']}", callback_data=f"version_{app_name}_{file['version']}")]
        for file in file_versions
    ]

    msg.edit(
        f"📲 **{app_name}**\n\n🔽 Select a version to download:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def send_selected_version(client, callback_query: CallbackQuery):
    data = callback_query.data.split("_")
    if len(data) < 3:
        callback_query.answer("Invalid selection!", show_alert=True)
        return

    app_name = data[1]
    version = data[2]

    # 🔹 Get the selected version details
    response = requests.get(f"{APP_DETAILS_URL}{app_name}&version={version}")
    if response.status_code != 200:
        callback_query.message.edit("❌ Error fetching the version details.")
        return
    
    try:
        version_data = response.json()
    except ValueError:
        callback_query.message.edit("❌ Invalid response from server.")
        return

    if version_data.get("status") != "success":
        callback_query.message.edit("⚠️ This version is not available.")
        return

    file_id = version_data.get("file_id")
    total_downloads = version_data.get("total_downloads")

    if not file_id:
        callback_query.message.edit("⚠️ File not found.")
        return

    details_text = f"""📲 **{app_name}**  
🔹 **Version:** {version}  
📥 **Total Downloads:** {total_downloads}"""

    user_id = callback_query.message.chat.id
    try:
        client.send_document(
            chat_id=user_id,
            document=file_id,
            caption=details_text,
            protect_content=True
        )
        callback_query.answer("📥 Download Started!", show_alert=True)
    except Exception as e:
        callback_query.message.reply_text("⚠️ Requested app not found. Please contact the admin.")
        client.send_message(
            FILE_CHANNEL_ID,
            f" **USER ID**: {user_id} \n\n⚠️ **Error:** {str(e)}"
        )