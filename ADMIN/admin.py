"""JAY SHREE RAM"""

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton , CallbackQuery, ReplyKeyboardRemove , ForceReply
import time
import json
import requests
from datetime import datetime, timedelta
import asyncio




import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from script import FILE_CHANNEL_ID,admin_app_details,admins
API_URL = "https://sainipankaj12.serv00.net/App/Pre/index.php"
cancel12 = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚫Cancel", callback_data="cancel")]])
admin_keyboard  = InlineKeyboardMarkup([
        [InlineKeyboardButton("Upload App", callback_data="adm_upload_premium_app")],
        [InlineKeyboardButton("BLOCK USER", callback_data="adm_block_user"),
        InlineKeyboardButton("Add Admin", callback_data="adm_add_admin")],
        [InlineKeyboardButton("Education", callback_data="adm_education"),
        InlineKeyboardButton("ADMINS", callback_data="adm_admins")],
        [InlineKeyboardButton("⚜️Home", callback_data="home")]
    ])
cancelkro = ReplyKeyboardMarkup(
    [[KeyboardButton("🚫CANCEL")]],
    resize_keyboard=True
)
upload_premium  = InlineKeyboardMarkup([
        [InlineKeyboardButton("Upload Menually", callback_data="adm_upload_menual")],
        [InlineKeyboardButton("GET FROM CHANNEL", callback_data="adm_get_from_channel")]])
def adminCommand(client,message, admins):
    user_id = message.from_user.id
    if user_id not in admins:
        return message.reply_text("⛔ आपको इस कमांड का उपयोग करने की अनुमति नहीं है!")
    else:
      message.reply_text(f"Welcome {admins[user_id]}, Your Most Welcome",reply_markup=admin_keyboard)
def adminCallback(client, callback_query,user_status,admins):
    user_id = callback_query.from_user.id
    first_name =callback_query.from_user.first_name
    if user_id not in admins:
        return callback_query.answer("⛔ आपको इस एक्शन की अनुमति नहीं है!", show_alert=True)
    callback_data = callback_query.data  # e.g., "adm_upload_premium_app"
    real_msg = callback_data.replace("adm_", "", 1)  # Removes "adm_" prefix
    #callback_query.message.reply_text(f"🔹 Real Message: {real_msg}")
    if real_msg =="upload_premium_app":
      callback_query.message.edit_text(f"Hey {first_name}, How do you want to add premium app",reply_markup=upload_premium)
    elif real_msg == "get_from_channel":
      callback_query.message.edit_text(f"Hey {first_name}, Please send me Channel Id Without @ .",reply_markup=cancelkro)
      user_status[user_id] = "adm_upload_app_from_channel"
    elif real_msg =="upload_menual":
      callback_query.message.reply_text(f"Hey {first_name}, Please send me a App to add that in database.",reply_markup=cancelkro)
      user_status[user_id] = "adm_upload_premium_app"
    elif real_msg =="block_user":
      callback_query.message.reply_text(f"Hey {first_name} , Please Send a User Id to Block him.")
      user_status[user_id] = "adm_block_user_id"
    elif real_msg == "admins":
        admin_list = "🔹 **Admins List** 🔹\n\n"

        for user_id, role in admins.items():
           user = client.get_users(user_id)  # Telegram से यूज़रनेम प्राप्त करें
           user_name = user.first_name if user.first_name else "Unknown"
           admin_list += f"**{role}** : [{user_name}](tg://user?id={user_id})\n"
        callback_query.message.edit_text(admin_list,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CLOSE 🔒", callback_data="admin_home")]]))
    elif real_msg =="add_admin":
      if admins[user_id] == "Temp Admin":
        callback_query.message.reply_text(f"Hey {first_name}, You Can't Add anyone to the admin.!")
      elif admins[user_id] == "Admin":
        callback_query.message.reply_text(f"Hey {first_name}, Please Send me user id to add admin!",reply_markup=cancelkro)
        user_status[user_id] = "adm_add_admin"
      elif admins[user_id] == "Owner":
        callback_query.message.reply_text(f"Hey {first_name}, Please Send me user id to add admin!",reply_markup=cancelkro)
        user_status[user_id] = "adm_add_admin"
      else:
        callback_query.message.edit_text(f"Hey {first_name}, You Can't add anyone to admin because you are are not a Parmant admin")
    
    elif real_msg =="upload_ar":
      callback_query.message.edit_text("Not Sending...",reply_markup=admin_keyboard)
      del admin_app_details[user_id]
    
async def admin_session_av(client, message, user_status):
    user_id = message.from_user.id
    user_state = user_status.get(user_id)
    real_msg = user_state.replace("adm_", "", 1)

    if real_msg == "upload_premium_app":
        await message.reply_text("⚠️Please Cancel this Session first!", reply_markup=cancel12)
    elif real_msg == "block_user":
        await message.reply_text("⚠️Please Cancel this Session first!", reply_markup=cancel12)
    else:
        await message.reply_text(f"There is a Session : {real_msg} \n**Please Cancel this session first!", reply_markup=cancel12)
        
def cancle_session_query(client,query,user_status):
  message=query.message
  user_id = query.from_user.id
  user_state = user_status.get(user_id)
  real_msg = user_state.replace("adm_", "", 1) 
  if real_msg == "upload_premium_app":
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      time.sleep(0.7)
      msg12.delete()
  elif real_msg == "block_user":
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      time.sleep(0.7)
      msg12.delete()
  else:
      del user_status[user_id]
      msg12 = message.reply_text("SESSION Canceled", reply_markup=ReplyKeyboardRemove())
      msg12.reply_text("Hello Admin Session Cancled Now Choose Next Option..",reply_markup=admin_keyboard)
      time.sleep(0.7)
      msg12.delete()

def cancle_session_msg(client,message,user_status):
  user_id = message.from_user.id
  user_state = user_status.get(user_id)
  real_msg = user_state.replace("adm_", "", 1) 
  if real_msg == "upload_premium_app":
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      time.sleep(0.7)
      msg12.delete()
  elif real_msg == "block_user":
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      time.sleep(0.7)
      msg12.delete()
  elif real_msg.startswith("enter_app"):
     del admin_app_details[user_id]
     msg12.edit("Hello Admin Session Cancled Now Choose Next Option..",reply_markup=admin_keyboard)
  else:
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      msg12.reply_text("Hello Admin Session Cancled Now Choose Next Option..",reply_markup=admin_keyboard)
      time.sleep(0.7)
      msg12.delete()

import re

# Helper function to extract channel username and message ID from a Telegram link
def extract_from_link(link):
    match = re.match(r'https://t\.me/([\w\d_]+)/(\d+)', link)
    if match:
        return match.group(1), int(match.group(2))
    return None, None

async def process_adm_text_messages(client, message, user_status, admin_app_details, admins):  
    user_id = message.from_user.id  
    user_text = message.text.strip()  
    user_state = user_status.get(user_id)  
    real_msg = user_state.replace("adm_", "", 1)

    if real_msg == "upload_app_from_channel":  
        username, msg_id = extract_from_link(user_text)
        if not username or not msg_id:
            await message.reply_text("❌ Invalid link! Please send a valid Telegram message link like:\n`https://t.me/channel/1234`")
            return
        try:  
            chat = await client.get_chat(username)
            await message.reply_text(f"""This Channel Details :  
📢 **{chat.title}**  
🆔 ID: `{chat.id}`  
👤 Members: {chat.members_count if chat.members_count else 'Unknown'}  
📜 Description: {chat.description if chat.description else 'No Description'}  
  
Now send me the **LAST message link**...  
            """)  
            user_status[user_id] = "adm_channel_last_id"  
            admin_app_details[user_id] = {
                'channel_id': chat.id,
                'channel_username': username,
                'first_id': msg_id
            }
        except Exception as e:  
            await message.reply_text("Failed to fetch channel details.")
  
    elif real_msg == "channel_last_id":
        username, msg_id = extract_from_link(user_text)
        if not username or not msg_id:
            await message.reply_text("❌ Invalid link! Please send a valid Telegram message link like:\n`https://t.me/channel/5678`")
            return
        admin_app_details[user_id]['last_id'] = msg_id
        await message.reply_text(f"✅ Last Message ID saved: {msg_id} \n\nNow saving files to database...")
        await fetch_and_save_files(client, user_id, message)
        del user_status[user_id]
def process_adm_photo(client,message,user_status,admin_app_details, FILE_CHANNEL_ID):
      user_id = message.from_user.id
      user_state = user_status.get(user_id)
      real_msg = user_state.replace("adm_", "", 1)
      message.reply_text("Please Provide A text...")



async def send_data(file_id, file_name):
    data = {
        "file_id": file_id,
        "file_name": file_name
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        response_json = response.json()  # API का JSON रिस्पॉन्स
        
        if response.status_code == 200 and response_json.get("success") is True:
            print(f"Sent: {file_name} - OK")
            return "OK"
        else:
            print(f"Sent: {file_name} - ER")
            return "ER"

    except Exception as e:
        print(f"Error sending {file_name}: {e}")
        return "ER"

async def fetch_and_save_files(client, user_id, message):
    try:
        details = admin_app_details.get(user_id, {})  
        source_channel = details.get('channel_id')
        target_channel = FILE_CHANNEL_ID  # Private Channel ID
        first_msg_id = details.get('first_id')
        last_msg_id = details.get('last_id')

        if not source_channel or not target_channel or not first_msg_id or not last_msg_id:
            return await message.reply_text("❌ Missing required details!")

        total_files = last_msg_id - first_msg_id + 1  
        saved_files = 0
        skipped_files = 0
        error_count = 0

        status_msg = await message.reply_text(
            f"📢 **Processing Started**\n\n"
            f"📂 **Total Files to Process:** {total_files}\n"
            f"📥 **Saved Files:** {saved_files}\n"
            f"⏭ **Skipped Files:** {skipped_files}\n"
            f"⚠ **Errors Encountered:** {error_count}"
        )

        for index, msg_id in enumerate(range(first_msg_id, last_msg_id + 1), start=1):
            try:
                fetched_message = await client.get_messages(source_channel, msg_id)  

                if fetched_message and fetched_message.document:
                    file_name = fetched_message.document.file_name

                    if file_name.endswith(".apk"):  # ✅ सिर्फ .apk फाइल ही सेव करें
                        copied_msg = await fetched_message.copy(target_channel)  # ✅ Forward Without Tag
                        file_id = copied_msg.document.file_id
                        
                        response = await send_data(file_id, file_name)  # ✅ File ID सेव करें

                        if response == "OK":
                            saved_files += 1
                        else:
                            error_count += 1  # अगर API से "OK" न मिले तो एरर काउंट बढ़ाएं

                        await asyncio.sleep(3)  
                    else:
                        skipped_files += 1  # .apk न होने पर स्किप करें

                else:
                    skipped_files += 1  
                
            except Exception as e:
                print(f"Skipping message {msg_id} due to error: {e}")
                error_count += 1  
                continue  

            if index % 50 == 0 or index == total_files:  
                await status_msg.edit(
                    f"📢 **Processing Update**\n\n"
                    f"📂 **Total Files to Process:** {total_files}\n"
                    f"📥 **Saved Files:** {saved_files}\n"
                    f"⏭ **Skipped Files:** {skipped_files}\n"
                    f"⚠ **Errors Encountered:** {error_count}"
                )

        await status_msg.edit(
            f"✅ **Processing Completed!**\n\n"
            f"📂 **Total Files Processed:** {total_files}\n"
            f"📥 **Successfully Saved:** {saved_files}\n"
            f"⏭ **Skipped Files:** {skipped_files}\n"
            f"⚠ **Errors Encountered:** {error_count}"
        )

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")

async def add_admin_temporarily(client, message,admins,FILE_CHANNEL_ID):
    if not message.text.startswith("/start admin_138998_"):
        return
    user_id = message.from_user.id
    
    try:
        parts = message.text.split("_")
        if len(parts) != 3:
            await message.reply("⚠️Password Changed! Your Provider Password Is Wrong!")
            return
        
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        current_time_str = parts[2]  # Extract time from command

        # Validate time format (HHMM)
        if len(current_time_str) != 4 or not current_time_str.isdigit():
            await message.reply("⚠️Password Changed! Your Provider Password Is Wrong!")
            return

        hh, mm = int(current_time_str[:2]), int(current_time_str[2:])
        if hh < 0 or hh > 23 or mm < 0 or mm > 59:
            await message.reply("⚠️Password Changed! Your Provider Password Is Wrong!")
            return

        # Get current time in HHMM format (12-hour format)
        now = datetime.now()
        current_hhmm = now.strftime("%H%M")  # 24-hour format
        
        # Compare entered time with current time
        if current_time_str != current_hhmm:
              await message.reply("⚠️Password Changed! Your Provider Password Is Wrong!")
              return

        if user_id in admins:
            await message.reply("You are already an admin!")
        else:
          
        # Add user as admin for 15 minutes
          admins[user_id] = "Temp Admin"
          await client.send_message(FILE_CHANNEL_ID, f"""
--A New TEMP ADMIN ADDED SUCCESSFULLY.--
**ID :** `{user_id}` 
**Name :** {user_name}
""")
          await message.reply("✅ **You are now an admin for 15 Minuts.**")

        # Remove user from admin list after 15 minutes
          await asyncio.sleep(900)  # 900 seconds = 15 minutes
          admins.pop(user_id, None)
          await message.reply("❌ **Your 15 Minuts Has completed You are  no longer admin!**")

    except Exception as e:
        await client.send_message(FILE_CHANNEL_ID, f" **USER ID **: {user_id} \n\n⚠️ **Error:** {str(e)}")

def add_new_admin(client,message,admins,user_status):
      admin_id = message.text
      user_id = message.from_user.id
      first_name = message.from_user.first_name
      try:
         user =  client.get_users(admin_id)  
         new_admin_first_name = user.first_name  # First Name एक्सट्रैक्ट करो
         if int(admin_id) in admins:
            message.reply(f"{new_admin_first_name} is already an admin!")
            return
         admins[int(admin_id)] = "Admin_added"
         del user_status[user_id]
         client.send_message(FILE_CHANNEL_ID, f"""
--User Added As an admin successfully:--

**Name :**  {new_admin_first_name}
**User ID :** {admin_id}
**Added By :** [{first_name}](tg://user?id={user_id})
  """)
         client.send_message(admin_id,"**Now You are an Admin. Of this Bot**\n\n--Please use-- /admin --command to use admin features!--",reply_markup=admin_keyboard)
         message.reply_text(f"""
--User Added As an admin successfully:--

**Name :**  {new_admin_first_name}
**User ID :** {admin_id}
**Added By :** [You](tg://user?id={user_id})
  """,reply_markup=admin_keyboard)
        
      
      except Exception as e:
         message.reply(f"⚠️ **Error:** {str(e)}")
      
      
