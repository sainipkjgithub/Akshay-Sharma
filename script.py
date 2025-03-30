from dotenv import load_dotenv
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
SEARCH_URL = "https://sainipankaj12.serv00.net/App/Pre/get.php?query="
admins = {6150091802: "Owner", 5943119285: "Admin"}  # Example Admin Dictionary
