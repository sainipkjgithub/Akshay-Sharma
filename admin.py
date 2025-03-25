"""JAY SHREE RAM"""
admins = {6150091802: "Owner", 5943119285: "Admin"}  # Example Admin Dictionary
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton , CallbackQuery, ReplyKeyboardRemove , ForceReply
import time
import json
import requests






cancel12 = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚫Cancel", callback_data="cancel")]])
admin_keyboard  = InlineKeyboardMarkup([
        [InlineKeyboardButton("Upload Premium App", callback_data="adm_upload_premium_app"),
        InlineKeyboardButton("BLOCK USER", callback_data="adm_block_user")],
        [InlineKeyboardButton("Add Admin", callback_data="adm_add_admin")],
        [InlineKeyboardButton("Home", callback_data="home")]
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
def adminCallback(client, callback_query,user_status):
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
      
def admin_session_av(client, message, user_status):
  user_id = message.from_user.id
  user_state = user_status.get(user_id)
  real_msg = user_state.replace("adm_", "", 1) 
  if real_msg == "upload_premium_app":
     message.reply_text("⚠️Please Cancel this Session first!",reply_markup=cancel12)
  elif real_msg == "block_user":
    message.reply_text("⚠️Please Cancel this Session first!",reply_markup=cancel12)
  else:
    message.reply_text(f"There is a Diffrent Session : {real_msg}",reply_markup=cancel12)

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
      msg12 = message.reply_text("Nothing to be Canceled for Admin", reply_markup=ReplyKeyboardRemove())
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
  else:
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      time.sleep(0.7)
      msg12.delete()

def process_adm_text_messages(client,message,user_status,admin_app_details):
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

# API URL
      url = "https://sainipankaj12.serv00.net/App/post.php"
      response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
      print(response.status_code)
      print(response.text)

      message.reply_text(f"""
APP DETAILS 
**APP NAME** : {app_name}
**APP VERSION** : {app_version}
**APP LOGO** : {app_logo}
**APP CATEGORY** : {app_category}
**ABOUT APP** : {app_details}
      """)
      
      
      
      
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