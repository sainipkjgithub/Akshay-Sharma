import requests 
import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton , CallbackQuery, ReplyKeyboardRemove , ForceReply

bot_details = {}
user_status = script.user_status
async def make_a_bot(client, callback_query):
  user_id = callback_query.from_user.id
  user_status[user_id] = "cb_getting_token"
  first_name =callback_query.from_user.first_name
  await callback_query.message.edit_text(f"Hey {first_name}, Please Provide a telegram bot token. \n get it from @botfather ")

import requests

async def add_bot_to(client, message):
    user_id = message.from_user.id
    user_text = message.text
    user_state = user_status.get(user_id)
    bot_details[user_id] = bot_details.get(user_id, {})
    real_msg = user_state.replace("cb_", "", 1)

    if real_msg == "getting_token":
        bot_details[user_id]['bot_token'] = user_text
        details = fetch_bot_details(user_text)
        if details:
            username = details.get("username")
            first_name = details.get("first_name")
            bot_id = details.get("id")

            bot_details[user_id]['info'] = {
                "username": f"@{username}",
                "database_channel": -1001234567890,  # Set your actual channel ID
                "admins": [user_id],
                "created_at": "2025-05-06T12:00:00Z",
                "restricted_users": []
            }

            await message.reply_text(
                f"Bot Details:\n"
                f"Name: {first_name}\n"
                f"Username: @{username}\n"
                f"ID: {bot_id}\n\nNow please provide a Welcome Message."
            )
            user_status[user_id] = "cb_getting_wlc_msg"
        else:
            await message.reply_text("Invalid bot token or unable to fetch bot details. Please try again.")
    
    elif real_msg == "getting_wlc_msg":
        welcome_msg = user_text
        bot_token = bot_details[user_id].get("bot_token")

        bot_details[user_id]["data"] = {
            "id": "root",
            "name": "Root",
            "description": welcome_msg,
            "type": "folder",
            "folders": [],
            "files": []
        }

        # 1. Add bot via PHP API
        response = requests.post(
            "https://sainipankaj12.serv00.net/BotBuilder/add_new_bot.php",
            json={
                "token": bot_token,
                "info": bot_details[user_id]["info"],
                "data": bot_details[user_id]["data"]
            }
        )

        if response.status_code == 201:
            # 2. Set webhook
            webhook_url = f"https://bot-builder-3vlc.onrender.com/{bot_token}"
            webhook_response = requests.get(f"https://api.telegram.org/bot{bot_token}/setWebhook", params={
                "url": webhook_url
            })

            # 3. Try sending a test message to /start
            send_msg = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", json={
                "chat_id": user_id,
                "text": "I am on! Please /start to manage me."
            })

            if send_msg.status_code == 200:
                await message.reply_text("Bot added successfully. A message has been sent to your bot.")
            else:
                await message.reply_text("Bot added successfully, but couldn't message you from the bot. Please start the bot manually first by clicking it and pressing /start.")

        elif response.status_code == 409:
            await message.reply_text("This bot already exists.")
        else:
            await message.reply_text(f"Failed to add bot. Server response: {response.text}")

        # Clear user session
        user_status.pop(user_id, None)
        bot_details.pop(user_id, None)

def fetch_bot_details(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    response = requests.get(url)
    data = response.json()
    if data.get("ok"):
        return data["result"]
    else:
        return None
