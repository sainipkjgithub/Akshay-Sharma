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
from script import FILE_CHANNEL_ID

cancel12 = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚫Cancel", callback_data="cancel")]])
admin_keyboard  = InlineKeyboardMarkup([
        [InlineKeyboardButton("Upload Premium App", callback_data="adm_upload_premium_app")],
        [InlineKeyboardButton("BLOCK USER", callback_data="adm_block_user"),
        InlineKeyboardButton("Add Admin", callback_data="adm_add_admin")],
        [InlineKeyboardButton("⚜️Home", callback_data="home")]
    ])
cancelkro = ReplyKeyboardMarkup(
    [[KeyboardButton("🚫CANCEL")]],
    resize_keyboard=True
)
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
      callback_query.message.reply_text(f"Hey {first_name}, Please send me a App to add that in database.",reply_markup=cancelkro)
      user_status[user_id] = "adm_upload_premium_app"
    elif real_msg =="block_user":
      callback_query.message.reply_text(f"Hey {first_name} , Please Send a User Id to Block him.")
      user_status[user_id] = "adm_block_user_id"
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
        callback_query.message.reply_text(f"Hey {first_name}, You Can't add anyone to admin because you are are not a Parmant admin")
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
      msg12.edit("Hello",reply_markup=admin_keyboard)
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
  else:
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      msg12.edit("Hello",reply_markup=admin_keyboard)
      time.sleep(0.7)
      msg12.delete()

def process_adm_text_messages(client,message,user_status,admin_app_details,admins):
    user_id = message.from_user.id
    user_state = user_status.get(user_id)
    real_msg = user_state.replace("adm_", "", 1) 
    if real_msg == "enter_app_name":
      app_name = message.text
      admin_app_details[user_id]["app_name"] = app_name
      message.reply_text("Version Of app")
      user_status[user_id] = "adm_enter_app_version"
    elif real_msg == "enter_app_version":
      app_version = message.text
      admin_app_details[user_id]["app_version"] = app_version
      message.reply_text("Who Is App Provider..?")
      user_status[user_id] = "adm_enter_app_provider"
    elif real_msg == "enter_app_provider":
      app_provider = message.text
      admin_app_details[user_id]["app_provider"] = app_provider
      message.reply_text("About App...")
      user_status[user_id] = "adm_enter_app_details"
    elif real_msg == "enter_app_details":
      app_details = message.text
      admin_app_details[user_id]["app_details"] = app_details
      message.reply_text("Send me a App logo..")
      user_status[user_id] = "adm_enter_app_logo"
    elif real_msg == "enter_app_category":
      app_category = message.text
      app_details = admin_app_details[user_id]["app_details"]
      file_id = admin_app_details[user_id]["file_id"]
      app_name = admin_app_details[user_id]["app_name"]
      app_version = admin_app_details[user_id]["app_version"]
      app_logo = admin_app_details[user_id]["app_logo"]
      app_provider = admin_app_details[user_id]["app_provider"]
      data = { "App Name": app_name,
      "File ID": file_id,
      "Version": app_version,
     "App Details": app_details,
     "Logo": app_logo,
     "Provider": app_provider,
     "Category": app_category
      }
    
      

      url = "https://sainipankaj12.serv00.net/App/post.php"
      response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
      print(response.status_code)
      print(response.text)
      del user_status[user_id]

      message.reply_text(f"""
APP DETAILS 
**APP NAME** : {app_name}
**APP VERSION** : {app_version}
**APP LOGO** : {app_logo}
**APP CATEGORY** : {app_category}
**ABOUT APP** : {app_details}
      """,reply_markup=ReplyKeyboardRemove())
    elif real_msg == "block_user_id":
      block_user = message.text
      message.reply_text("Thanks For Provide me This Id I am Blocking..")
    elif real_msg == "add_admin":
      add_new_admin(client,message,admins,user_status)




def process_adm_photo(client,message,user_status,admin_app_details, FILE_CHANNEL_ID):
      user_id = message.from_user.id
      user_state = user_status.get(user_id)
      real_msg = user_state.replace("adm_", "", 1) 
      if real_msg =="enter_app_logo":
         forwarded = message.forward(FILE_CHANNEL_ID)
         file_id = forwarded.photo.file_id
         app_logo = f"https://sainipankaj12.serv00.net/TelegramStream.php?file_id={file_id}&file_type=photo"
         admin_app_details[user_id]["app_logo"] = app_logo
         message.reply_text("✅️App Logo Saved.\nNow Provide App category...",reply_markup=cancel12)
         user_status[user_id] = "adm_enter_app_category"
      else:
        message.reply_text("Please Provide A text...")


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
         client.send_message(admin_id,"**Now You are an Admin. Of this Bot**\n\n--Please use-- /admin --command to use admin features!--")
         message.reply_text(f"""
--User Added As an admin successfully:--

**Name :**  {new_admin_first_name}
**User ID :** {admin_id}
**Added By :** [You](tg://user?id={user_id})
  """,reply_markup=admin_keyboard)
        
      
      except Exception as e:
         message.reply(f"⚠️ **Error:** {str(e)}")
      
      
