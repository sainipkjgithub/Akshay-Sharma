"""
JAY SHREE RAM
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,InputMediaPhoto
import requests
APP_DETAILS_URL = "https://sainipankaj12.serv00.net/App/get.php?app_name="
SEARCH_URL = "https://sainipankaj12.serv00.net/App/index.php?query="
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
    details_text = f"""**📲 {app_data.get('App Name', 'Unknown App')}**
🔹 **Version:** {app_data.get('Version', 'N/A')}
📄 **Details:** {app_data.get('App Details', 'No details available')}
📥 **Total Downloads:** {app_data.get('Total Downloads', 1003)}
⚜️ **PROVIDER** : {app_data.get('Provider', 'Mr. Singodiya')}
🏷 **Category:** {app_data.get('Category', 'Unknown')}"""

    msg.edit(details_text)
    file_id = app_data.get("File ID")
    logo_url = app_data.get("Logo")
    if logo_url:
      msg.reply_photo(photo=logo_url, caption="App logo")
    if file_id:
       client.send_document(
    chat_id=msg.chat.id, 
    document=file_id, 
    caption="📥 **Download App**", 
    protect_content=True
)
    else:
      msg.reply_photo("App Not Found. Please Contect To admin...")