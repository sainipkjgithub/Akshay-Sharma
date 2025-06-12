#Version 2.3.4
import requests
from dotenv import load_dotenv
from pyrogram import Client, filters
import os
load_dotenv()
FILE_CHANNEL_ID = int(os.getenv("FILE_CHANNEL_ID"))
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SEARCH_URL = "https://sainipankaj12.serv00.net/App/index.php?query="
user_status = {}
admin_app_details = {}
user_histories = {}
temp_data = {}
waiting_users = []
active_chats = {}   # {user_id1: user_id2, user_id2: user_id1}
message_map = {}  # {sender_msg_id: receiver_msg_id}
# Dictionary: {user_id: partner_id}
SEARCH_URL = "https://sainipankaj12.serv00.net/App/Pre/get.php?query="
admins = {6150091802: "Owner", 5943119285: "Admin"}  # Example Admin Dictionary
UPLOAD_URL = "https://sainipankaj12.serv00.net/App/Pre/index.php"
API_URL = "https://sainipankaj12.serv00.net/App/Pre/index.php"
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def send_telegram_message(chat_id, text, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()
