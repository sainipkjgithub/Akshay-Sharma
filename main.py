"""JAI SHREE RAM"""
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, ReplyKeyboardRemove , ForceReply

from script1 import CALLBACK123, home_keyboard, ReplyMarkup123, startmsg, wrongbutton
from ReplyMarckep import download_any_video,available_boards, chat_with_assistant, cancel12, back_enter_rollnumber, cancelkro ,earnMoney,help_keyboard,explore_more,admin_home_keyboard
from EARN.earn import earn_Money123GetClick,provide_earn_Money_link,term_and_conditions,refresh_total_clicks,refresh_link,refresh_today_clicks,refresh_clicks,withdraw_handler
from aiImageEditor import ai_image_enhancer
from FUNCTIONS.functions import sendAi_message,get_quote, chack_add_user, india_time
from PremiumApps.premium import search_and_send_inline, search_and_send_app ,premiumcall12345,premium_app_send
from ADMIN.admin import admin_session_av, cancle_session_query, cancle_session_msg ,adminCommand,adminCallback,process_adm_photo,process_adm_text_messages,add_admin_temporarily,send_data
from ADMIN.AdmEducation import admin_edu , admin_education1
from start_param import start_params
from createBot import make_a_bot, add_bot_to
from any_chat import any_chat_start,chat_stop_handler, forward_message
import requests
import time
from flask import Flask, request, jsonify
import os
import asyncio
import threading
import json
flask_app = Flask(__name__)
import cp-main
#InlineKeyboardMarkup([[InlineKeyboardButton("⚜Home", callback_data="home")]])
@flask_app.route('/')
def home():
    return "All in one Bot is running."
#########
from script import send_telegram_message




##############₹%%%%^₹%^₹%^
# बॉट के लिए API क्रेडेंशियल्स
import script

# Variables ko local alias banake bind kar lo
app = script.app
FILE_CHANNEL_ID = script.FILE_CHANNEL_ID
API_ID = script.API_ID
API_HASH = script.API_HASH
BOT_TOKEN = script.BOT_TOKEN
SEARCH_URL = script.SEARCH_URL
user_status = script.user_status
admin_app_details = script.admin_app_details
temp_data = script.temp_data
admins = script.admins
user_histories = script.user_histories
UPLOAD_URL = script.UPLOAD_URL
API_URL = script.API_URL
waiting_users = script.waiting_users
active_chats = script.active_chats
message_map = script.message_map


user_board_details = {}

previous_messages = {}
wb_id_dict = {
    "rbse_10": 88,
    "rbse_12": 89,
    "up_10": 100,
    "up_12": 99
}
# Pyrogram बॉट क्लाइंट सेटअप



@app.on_message(filters.command("admin"))
def admin(client, message):
  adminCommand(client,message,admins)

@app.on_message(filters.command("stop") & filters.private & ~filters.me)
async def stop_handler12(client, message):
  await chat_stop_handler(client, message)

@app.on_message(filters.command("broadcast") & filters.user(list(admins.keys())))
def broadcast_reply(client, message: Message):
    try:
        if not message.reply_to_message:
            return message.reply("Please reply to a message to broadcast.")

        res = requests.get("https://sainipankaj12.serv00.net/AkshaySharmaBot/userdetails.json")
        users = res.json()

        success = 0
        failed_users = []

        for user in users:
            try:
                client.copy_message(
                    chat_id=user['user_id'],
                    from_chat_id=message.reply_to_message.chat.id,
                    message_id=message.reply_to_message.id
                )
                success += 1
            except:
                failed_users.append(user)

        # Handle failed users
        for user in failed_users:
            try:
                report_text = f"Failed to send message to user:\nID: `{user['user_id']}`\nName: `{user['first_name']}`"
                send_telegram_message(message.from_user.id, report_text, BOT_TOKEN)

                del_url = f"https://sainipankaj12.serv00.net/AkshaySharmaBot/delete_user.php?user_id={user['user_id']}"
                requests.get(del_url)

            except Exception as e:
                print(f"Failed to report/delete user {user['user_id']}: {e}")

        message.reply(f"Broadcast sent to {success} users. {len(failed_users)} failed.")

    except Exception as e:
        message.reply(f"Error: {e}")

@app.on_message(filters.command("start") & ~filters.me)
async def start(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    chack_add_user(user_id, first_name)
    user_name = message.from_user.first_name
    command_args = message.text.split(" ", 1)  # "/start" के बाद के डेटा को अलग करने के लिए
    start_param = command_args[1] if len(command_args) > 1 else None  # "/start" के बाद का डेटा
    
    # **1. अगर कोई विशेष `start_param` नहीं है, तो डिफ़ॉल्ट वेलकम मैसेज भेजें**
    if not start_param:
        if user_status.get(user_id) == "chatting_with_ai":
            return await message.reply_text("⚠️ Please cancel this chat first!", reply_markup=cancel12)
        elif user_status.get(user_id) in ["enter_roll_number", "search_premium_app"]:
            return await message.reply_text("⚠️ Please cancel this session first!", reply_markup=cancel12)
        elif user_status.get(user_id) and user_status[user_id].startswith("adm_"):
            return await admin_session_av(client, message, user_status)
        elif user_id in admins:
            return await message.reply_text(f"Hey Admin [{user_name}](tg://user?id={user_id}), How are you?", reply_markup=admin_home_keyboard)
        else:
            return await message.reply_text(startmsg, reply_markup=home_keyboard)

    elif start_param:
    # **2. अब `start_param` के अलग-अलग प्रकारों को चेक करें**
        if start_param.startswith("admin_138998_"):
          return await add_admin_temporarily(client, message, admins, FILE_CHANNEL_ID)

        else:
          return await start_params(client, message, start_param)

    # **3. यदि कोई मैपिंग नहीं मिली, तो एक डिफ़ॉल्ट मैसेज भेजें**
    return await message.reply_text(f"⚠️ Unknown request: `{start_param}`", reply_markup=home_keyboard)

@app.on_message(filters.command("help") & ~filters.me)
def helpcommand(client, message):
    message.reply_text(
        startmsg,
        reply_markup=help_keyboard
    )
#Admin Education
@app.on_callback_query(filters.regex("^aded_"))
async def admin_education1(client, callback_query):
  await admin_education1(client, callback_query)

@app.on_callback_query(filters.regex("^adm_education"))
async def admin_education(client, callback_query):
  await admin_edu(client, callback_query)
@app.on_callback_query(filters.regex("delete"))
async def delete(client, callback_query):
   await callback_query.message.delete()

@app.on_callback_query(filters.regex("make_bot"))
async def creat_a_bot(client, callback_query):
  await make_a_bot(client, callback_query)

@app.on_callback_query(filters.regex("^any_"))
def any_chat(client, callback_query):
    any_chat_start(client, callback_query)
@app.on_callback_query(filters.regex("^adm_upload_ok_"))
async def admin_callback456(client, callback_query):
    user_id = callback_query.from_user.id
    
    if user_id not in admins:
        return await callback_query.answer("⛔ आपको इस एक्शन की अनुमति नहीं है!", show_alert=True)
    
    callback_data = callback_query.data  # e.g., "adm_upload_ok_file1"
    file_key = callback_data.replace("adm_upload_ok_", "", 1)  # Extracting file_key (e.g., file1, file2)

    if user_id in admin_app_details and file_key in admin_app_details[user_id]:
        file_id = admin_app_details[user_id][file_key]['file_id']
        file_name = admin_app_details[user_id][file_key]['file_name']

        await callback_query.message.edit_text("Please Wait...")
        await send_data(file_id, file_name)
        
        await callback_query.message.edit_text(
            "Uploaded successfully! Thanks for uploading this file. 😊",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🚫Delete", callback_data="delete")],
                [InlineKeyboardButton("⚜ Home", callback_data="home")]
            ])
        )
    else:
        await callback_query.answer("No file details", show_alert=True)
@app.on_callback_query(filters.regex("^withdrawal$"))
def handle_withdraw(client, callback_query):
    withdraw_handler(client, callback_query)  # ✅ Call किया

@app.on_callback_query(filters.regex("^adm_"))
def admin_callback(client, callback_query):
  adminCallback(client, callback_query,user_status,admins)

@app.on_callback_query(filters.regex("^pre_"))
async def premiumcall(client, query: CallbackQuery):
  await premium_app_send(client, query)
    

@app.on_callback_query(filters.regex("^page_"))
async def premiumcall12(client, query: CallbackQuery):
  await premiumcall12345(client, query)

@app.on_callback_query()
def callback_query(client, query: CallbackQuery):
    import script
    waiting_users = script.waiting_users
    active_chats = script.active_chats
    message_map = script.message_map
    user_status = script.user_status
    user_id = query.from_user.id  # Get user ID
    user_name = query.from_user.first_name  # Extract user name
    if query.data == "chat_with_assistant":
        query.message.edit_text("We are Connecting You to our Ai Assistent...")
        time.sleep(2)
        query.message.delete()
        a=query.message.reply_text(f"Hello {user_name}, How can I assist you today..?",reply_markup=chat_with_assistant)
        user_status[user_id] = "chatting_with_ai"  # Save user status
        #a.delete()
    elif query.data == "download_any_video":
      query.message.edit_text("This Features Is Comming Soon.", reply_markup=download_any_video)
    elif query.data == "earn_money":
      msg1 = query.message.edit_text("Wait Fetching Your Link and Link Details.")
      chat_id = user_id
      earn_link = provide_earn_Money_link(chat_id)
      earnMoney12 = earnMoney(earn_link)
      time.sleep(2)
      msg2 = msg1.edit_text("Wait Fetching Your Link and Link Details..")
      today_click = earn_Money123GetClick(chat_id, "today")
      time.sleep(0.7)
      msg3 = msg2.edit_text("Wait Fetching Your Link and Link Details...")
      earn_link_total_click = earn_Money123GetClick(chat_id, "total")
      time.sleep(0.9)
      msg4 = msg3.edit_text("Wait Fetching Your Link and Link Details")
      msg4.edit_text(f"""
💰 Earn Money with Telegram! 🤑💸  

Now you can --**make money**-- just by sharing a link!  

🔗 --**Your Earning Link:**--
{earn_link}  


--**📢 How It Works?  **--
1️⃣ **Share** this link with your friends, family, or social media.  
2️⃣ **Ask them** to open the link.  
3️⃣ **Earn money** for every valid click!  

  

--📊 **Today's Performance**--
🔹 **Clicks Received:** `{today_click}`  
🔹 **Earnings Today:** `₹{today_click * 0.5}`  
🔹 **Current CPM:** `₹500`  

  

--💰 **Total Earnings**--
🔸 **Total Clicks:** `{earn_link_total_click}`  
🔸 **Total Earned:** `₹{earn_link_total_click * 0.5}`  
🔸 **Average CPM:** `₹500`  



--**Withdraw Your Earnings!**--
✅ Minimum withdrawal: **₹600**  
✅ Request payout anytime!  

⚠ --**Note:** --Please read our **Terms & Conditions** before using this feature.  

Start sharing and start earning now! 🚀
      """,
      reply_markup=earnMoney12)
    elif query.data == "premium_apps":
      query.answer("Redirecting...")
      keyboard = InlineKeyboardMarkup([
       [InlineKeyboardButton("Open Premium Bot", url="https://t.me/apps_premiumBot?start=app")],[InlineKeyboardButton("🔙Back", callback_data="explore_more")]])
      query.edit_message_text("Click below to get Premium Apps:", reply_markup=keyboard)
    elif query.data == "motivational_quota":
      query.message.edit_text("Getting Quota...")
      query.message.edit_text(get_quote(),reply_markup=InlineKeyboardMarkup([
          [InlineKeyboardButton("♻️Refresh", callback_data="motivational_quota")],
          [InlineKeyboardButton("🔙Back", callback_data="explore_more"),
          InlineKeyboardButton("⚜Home", callback_data="home")]
          ])
          )
    elif query.data.startswith("board_result_") and query.data.endswith(("_10", "_12")):
        parts = query.data.split("_")
        board_name = parts[2]  # Extract board name
        class_name = parts[3]  # Extract class (10 or 12)
    
        user_board_details[user_id] = {"board": board_name, "class": class_name}  # Save user board details
        user_status[user_id] = "enter_roll_number"  # Save user status
    
        query.message.delete()
        query.message.reply_text("Please Enter Your Roll Number...",reply_markup=cancelkro)
    elif query.data.startswith("board_result_"):
        board_name = query.data.split("_")[-1]  # Extract board name
        buttons = [
        [InlineKeyboardButton("Class 10", callback_data=f"board_result_{board_name}_10")],
        [InlineKeyboardButton("Class 12", callback_data=f"board_result_{board_name}_12")],
        [InlineKeyboardButton("🔙BACK", callback_data=f"available_boards"),
        InlineKeyboardButton("🏠Home", callback_data="home")]
        ]
        query.message.edit_text("Select your class:", reply_markup=InlineKeyboardMarkup(buttons))
####CANCEL MSG HANDEL###    
    elif query.data == "cancel":
      user_id = query.from_user.id
      user_name = query.from_user.first_name
      if user_status.get(user_id) == "chatting_with_ai":
        del user_status[user_id]
        del user_histories[user_id]
        msg12 = query.message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
        time.sleep(0.7)
        msg12.delete()
        query.message.reply_text(startmsg,reply_markup=home_keyboard)
        query.message.delete()
      elif user_status.get(user_id) == "enter_roll_number":
        del user_status[user_id]
        msg12 = query.message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
        time.sleep(0.7)
        msg12.delete()
        board_name = user_board_details[user_id]["board"]
        buttons = [
          [InlineKeyboardButton("Class 10", callback_data=f"board_result_{board_name}_10")],
          [InlineKeyboardButton("Class 12", callback_data=f"board_result_{board_name}_12")],
          [InlineKeyboardButton("🔙BACK", callback_data=f"available_boards"),
          InlineKeyboardButton("🏠Home", callback_data="home")]
          ]
        query.message.reply_text(
         "PLEASE SELECT YOUR CLASS...",
          reply_markup=InlineKeyboardMarkup(buttons))
        del user_board_details[user_id]
        query.message.delete()
      elif user_status.get(user_id) == "download_any_video":
        del user_status[user_id]
      elif user_status.get(user_id) == "any_chat_waiting":
         print(waiting_users)
         waiting_users.remove(user_id)
         del user_status[user_id]
         query.message.delete()
         query.message.reply_text("Searching Stoped!",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙Back", callback_data="explore_more")]]))
      elif user_status.get(user_id) == "any_chat_connected":
        if user_id in active_chats:
            partner_id = active_chats[user_id]
            del active_chats[user_id]
            del active_chats[partner_id]
            del user_status[user_id]
            del user_status[partner_id]
            client.send_message(partner_id, "Chat Stopped by your partner..")
            msg12 = query.message.reply_text("You Stoped this chat!", reply_markup=ReplyKeyboardRemove())
        else:
            query.message.reply("आप किसी से जुड़े नहीं हैं।")
        
        query.message.delete()
      elif user_status.get(user_id) == "search_premium_app":
        del user_status[user_id]
        msg12 = query.message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
        query.message.delete()
        msg12.delete()
        query.message.reply_text(
         "Explore More",
          reply_markup=explore_more)
      elif user_status.get(user_id) and user_status[user_id].startswith("adm_"):
        cancle_session_query(client,query,user_status)
      else:
          query.message.reply_text("⚠️ Nothing to CANCLE. ")
          query.message.delete()
      
    elif query.data=="Refresh_earning":
      user_id = query.from_user.id
      chat_id = user_id
      earn_link = f"https://urlshortner.pkjsaini42.workers.dev/{chat_id}"
      earnMoney12 = earnMoney(earn_link)
      msg1 = query.message.edit_text(refresh_clicks,reply_markup=earnMoney12)
      time.sleep(0.4)
      earn_link_msg = refresh_link(earn_link)
      msg1.edit_text(earn_link_msg,reply_markup=earnMoney12)
      today_click = earn_Money123GetClick(chat_id, "today")
      time.sleep(0.6)
      today_click_msg  = refresh_today_clicks(today_click,earn_link)
      msg1.edit_text(today_click_msg,reply_markup=earnMoney12)
      earn_link_total_click = earn_Money123GetClick(chat_id, "total")
      earn_link_total_click_msg = refresh_total_clicks(earn_link_total_click,earn_link,today_click)
      time.sleep(0.9)
      msg1.edit_text(earn_link_total_click_msg,reply_markup=earnMoney12)
    elif query.data =="home":
      user_id = query.from_user.id
      user_name = query.from_user.first_name
      if user_id in admins:
        query.message.reply_text(f"Hey Admin [{user_name}](tg://user?id={user_id}), How are you", reply_markup=admin_home_keyboard)
      else:
        query.message.reply_text(f"Hey [{user_name}](tg://user?id={user_id}) , Welcome You to SingodiyaTech", reply_markup=home_keyboard)
      query.message.delete()
      
    elif query.data in CALLBACK123:
      if query.data in ReplyMarkup123:
        query.message.edit_text(CALLBACK123[query.data], reply_markup=ReplyMarkup123[query.data])
      else:
        query.message.edit_text(CALLBACK123[query.data])
    else:
        query.message.edit_text("No Data Found For Your Clicked Button. Please Contact to Admin to Support",reply_markup=wrongbutton)
@app.on_message(filters.text & ~filters.me &~filters.group & ~filters.command("start") & ~filters.regex(r"^🚫CANCEL$")
)
async def process_text_messages(client: Client, message: Message):
    user_id = message.from_user.id
    user_msg = message.text
    user_name = message.from_user.first_name
    import script
    user_status = script.user_status
    print(user_status)
    if user_status.get(user_id) == "chatting_with_ai":
      answer = sendAi_message(user_id,user_name, user_msg)
      await message.reply_text(answer)
    # WB ID Dictionary for different boards and classes
    elif user_status.get(user_id) == "any_chat_waiting":
      await message.reply_text("Sorry 😔, We could not get connected you to any partner.\n\n I am searching yet...",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚫Cancel Searching", callback_data="cancel")]]))
    elif user_status.get(user_id) == "any_chat_connected":
      await forward_message(client, message)
    elif user_status.get(user_id) == "enter_roll_number":
        if user_id in user_board_details:
            board = user_board_details[user_id]["board"]
            class_name = user_board_details[user_id]["class"]
            roll_no = user_msg.strip()  # Get user input roll number
        
        # Validate roll number (should be 7 digits and numeric)
            if roll_no.isdigit() and len(roll_no) == 7:
                key = f"{board}_{class_name}"  # Generate key for wb_id
                wb_id = wb_id_dict.get(key, 88)  # Default to 88 if not found

                # Generate result document URL
                if wb_id == 88  :
                  result_link = f"https://sainipankaj12.serv00.net/Result/boardresult.php?tag=raj_10th_result&roll_no={roll_no}&year=2025&wb_id={wb_id}&source=3&download"
                elif wb_id == 89  :
                  result_link = f"https://sainipankaj12.serv00.net/Result/boardresult.php?tag=raj_12th_result&roll_no={roll_no}&year=2025&wb_id={wb_id}&source=3&download"
                a = await message.reply_text(f"Please Wait Getting Your Result Data...")
                # Send document to user
                result_link_view = result_link.replace("download", "see")
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
                data ={
                   "chat_id": user_id,
                    "caption": "Here is your result document.",
                    "document": result_link,
                    "reply_markup": '{"inline_keyboard": [[{"text": "View Online", "web_app": {"url": "' + result_link_view + '"}}]]}'
                       }
                

                #requests.post(url, data=data)
                response = requests.post(url, data=data)
                if response.status_code == 200 and response.json().get("ok"):
                    await a.delete()
                    return
                else:
                  link = "https://sainipankaj12.serv00.net/Result/faild.json"
                  res = requests.get(link).json()

                  if wb_id == 88:
                      msg = res.get("10", "Unknown error.")
                  elif wb_id == 89:
                     msg = res.get("12", "Unknown error.")
                  else:
                      msg = "..."

                  await a.edit_text(f"**Failed to get your result!!**\n{msg}")
                
            else:
                await message.reply_text("Invalid roll number! Please enter a Valid Roll Number." ,reply_markup=back_enter_rollnumber)
        else:
           await message.reply_text("Please select your board and class first.",reply_markup=available_boards)
    elif user_status.get(user_id) == "search_premium_app":
       await client.delete_messages(chat_id=message.chat.id, message_ids=previous_messages[user_id])
       msg= await message.reply_text("Please Wait...",reply_markup=ReplyKeyboardRemove())
       await msg.delete()
       msg = await message.reply_text("Searching app...")
       Search_Query = user_msg
       await search_and_send_inline(msg,Search_Query)
    elif user_status.get(user_id) and user_status[user_id].startswith("adm_"):
      await process_adm_text_messages(client,message,user_status,admin_app_details,admins)
    elif user_status.get(user_id) and user_status[user_id].startswith("cb_"):
      await add_bot_to(client,message)
    else:
        await message.reply_text("⚠️ Please Select a Valid Option.",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚜Home", callback_data="home")]]))
"""
ON CANCEL msg12
"""
@app.on_message(filters.text & ~filters.me & ~filters.group & ~filters.command("start") & filters.regex(r"^🚫CANCEL$"))
def canclemsg(client: Client, message: Message):
    import script
    user_status = script.user_status
    user_id = message.from_user.id
    user_msg = message.text
    user_name = message.from_user.first_name
    if user_status.get(user_id) == "chatting_with_ai":
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      time.sleep(0.7)
      msg12.delete()
      message.reply_text(
        startmsg,
        reply_markup=home_keyboard
    )
      
    elif user_status.get(user_id) == "enter_roll_number":
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      time.sleep(0.7)
      msg12.delete()
      board_name = user_board_details[user_id]["board"]
      buttons = [
        [InlineKeyboardButton("Class 10", callback_data=f"board_result_{board_name}_10")],
        [InlineKeyboardButton("Class 12", callback_data=f"board_result_{board_name}_12")],
        [InlineKeyboardButton("🔙BACK", callback_data=f"available_boards"),
        InlineKeyboardButton("🏠Home", callback_data="home")]
        ]
      del user_board_details[user_id]
      message.reply_text(
       "PLEASE SELECT YOUR CLASS...",
        reply_markup=InlineKeyboardMarkup(buttons))
    
    elif user_status.get(user_id) == "download_any_video":
      del user_status[user_id]
    elif user_status.get(user_id) == "search_premium_app":
      del user_status[user_id]
      msg12 = message.reply_text("Session Canceled!", reply_markup=ReplyKeyboardRemove())
      time.sleep(0.7)
      msg12.delete()
    elif user_status.get(user_id) and user_status[user_id].startswith("adm_"):
      cancle_session_msg(client,message,user_status)
    else:
        message.reply_text("⚠️ Nothing to CANCLE.",reply_markup=ReplyKeyboardRemove())
        message.delete()
        

@app.on_message(filters.private & filters.photo & ~filters.me)
def forward_photo(client, message):
    import script
    user_status = script.user_status
    user_id = message.from_user.id
    if user_status.get(user_id) == "chatting_with_ai":
      message.reply_text("Sorry I can't see your sended Photo",reply_markup=cancel12)
    elif user_status.get(user_id) == "enter_roll_number":
       message.reply_text("⚠️Please Provide a Valid Roll number Or Cancel this session!",reply_markup=cancel12)
    elif user_status.get(user_id) == "search_premium_app":
       message.reply_text("⚠️Please Provide a App name..",reply_markup=cancel12)
    elif user_status.get(user_id) and user_status[user_id].startswith("adm_"):
       process_adm_photo(client,message,user_status,admin_app_details, FILE_CHANNEL_ID)
    else:
      forwarded = message.forward(FILE_CHANNEL_ID)
      file_id = forwarded.photo.file_id
      stream_url = f"https://sainipankaj12.serv00.net/TelegramStream.php?file_id={file_id}&file_type=photo"
      message.reply_text(f"Here is your direct download link :\n \n{stream_url}\n\nThis link is Permanent." )
    
    
@app.on_message(filters.private & filters.document & ~filters.me)
async def get_file_id(client, message):
    import script
    user_status = script.user_status
    user_id = message.from_user.id
    if user_status.get(user_id) == "chatting_with_ai":
      await message.reply_text("Sorry I cant see your sended Document",reply_markup=cancel12)
    elif user_status.get(user_id) == "enter_roll_number":
       await message.reply_text("⚠️Please Provide a Valid Roll number Or Cancel this session!",reply_markup=cancel12)
    elif user_status.get(user_id) == "search_premium_app":
       await message.reply_text("⚠️Please Provide a App name I Will Find Out Premium app for you...",reply_markup=cancel12)
    elif user_status.get(user_id) and user_status[user_id].startswith("adm_"):
      forwarded = await message.copy(FILE_CHANNEL_ID)
      file_id = forwarded.document.file_id
      file_name = forwarded.document.file_name
      user_state = user_status.get(user_id)
      real_msg = user_state.replace("adm_", "", 1) 
      if real_msg =="upload_premium_app":
         await message.reply_text(f"""
Saved Successfully in database : 
**FILE NAME :** `{file_name}`
**FILE ID : ** `{file_id}` .
      """,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙Back", callback_data="adm_upload_premium_app")]]))
         await send_data(file_id, file_name)
         del user_status[user_id]
  
    else:
      if user_id in admins:
         forwarded = await message.copy(FILE_CHANNEL_ID)
         file_id = forwarded.document.file_id
         file_name = forwarded.document.file_name  # फाइल का नाम
      
         if ".apk" in file_name.lower(): 
             if user_id not in admin_app_details:
                 admin_app_details[user_id] = {}  # हर एडमिन के लिए अलग डिक्शनरी
        
             # नई फाइल के लिए अगला क्रमांक निकालें
             file_count = len(admin_app_details[user_id]) + 1
             file_key = f"file{file_count}"

             admin_app_details[user_id][file_key] = {
                 "file_id": file_id,
                 "file_name": file_name
             }
             verify_premium_upload  = InlineKeyboardMarkup([
                [InlineKeyboardButton("Upload Premium App", callback_data=f"adm_upload_ok_{file_key}"),
                InlineKeyboardButton("Don't Upload", callback_data="adm_upload_ar")]])
             await message.reply_text(
                 f"**File Name :**\n `{file_name}`\n\n**File Id** :\n`{file_id}`\n\n UPLOAD THIS APP TO PREMIUM APPS DATABASE",
                 reply_markup=verify_premium_upload
             )
         else:
             await message.reply_text(
                 f"**File Name :**\n `{file_name}`\n\n**File Id :**\n `{file_id}`",
                 reply_markup=home_keyboard
             )
      else:
          await message.reply_text("Unsupport Media Type...",reply_markup=home_keyboard)
def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        return save_path
    return None


def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

def get_bot_info(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("ok"):
            result = data["result"]
            name = result.get("first_name")
            username = result.get("username")
            return name, username
        else:
            return None, "Invalid token or bot not found"
    else:
        return None, f"HTTP error: {response.status_code}"


def run_bot():
    print("Bot is running...")
    name, username = get_bot_info(BOT_TOKEN)
    send_telegram_message(FILE_CHANNEL_ID, f"BOT STARTED SUCCESSFULLY! \n BOT Name : {name}\n Username: @{username}\n Time : {india_time()}", BOT_TOKEN)
    app.run()
    print("\nShutting Down...\n")
    

# Running Flask and Pyrogram bot concurrently using threads
if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    run_bot()  # This will run the bot after Flask starts
#############
"""
Version 2
"""
