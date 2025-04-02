"""JAI SHREE RAM"""
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, ReplyKeyboardRemove , ForceReply

from script1 import CALLBACK123, home_keyboard, ReplyMarkup123, startmsg, wrongbutton
from ReplyMarckep import download_any_video,available_boards, chat_with_assistant, cancel12, back_enter_rollnumber, cancelkro ,earnMoney,help_keyboard,explore_more,admin_home_keyboard
from EARN.earn import earn_Money123GetClick,provide_earn_Money_link,term_and_conditions,refresh_total_clicks,refresh_link,refresh_today_clicks,refresh_clicks,withdraw_handler
from aiImageEditor import ai_image_enhancer
from FUNCTIONS.functions import sendAi_message,get_quote
from PremiumApps.premium import search_and_send_inline, search_and_send_app ,premiumcall12345,premium_app_send
from ADMIN.admin import admin_session_av, cancle_session_query, cancle_session_msg ,adminCommand,adminCallback,process_adm_photo,process_adm_text_messages,add_admin_temporarily,send_data
from start_param import start_params
import requests
import time
from flask import Flask, request, jsonify
import os
import asyncio
import threading
import json
flask_app = Flask(__name__)
#InlineKeyboardMarkup([[InlineKeyboardButton("⚜Home", callback_data="home")]])
@flask_app.route('/')
def home():
    return "All in one Bot is running."
#########





##############₹%%%%^₹%^₹%^
# बॉट के लिए API क्रेडेंशियल्स
from script import FILE_CHANNEL_ID, API_ID, API_HASH, BOT_TOKEN, SEARCH_URL,user_status,admin_app_details, temp_data,admins,user_histories,UPLOAD_URL, API_URL

user_board_details = {}

previous_messages = {}
wb_id_dict = {
    "rbse_10": 88,
    "rbse_12": 89,
    "up_10": 99,
    "up_12": 100
}
# Pyrogram बॉट क्लाइंट सेटअप
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)



@app.on_message(filters.command("admin"))
def admin(client, message):
  adminCommand(client,message,admins)
    
   # message.reply_text(f"✅ Welcome, {admins[user_id]}!")
@app.on_message(filters.command("start") & ~filters.me)
async def start(client, message):
    user_id = message.from_user.id
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


@app.on_callback_query(filters.regex("delete"))
async def delete(client, callback_query):
   await callback_query.message.delete()
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
      user_status[user_id] = "search_premium_app"
      msg = query.message.reply_text("Provide App Name..", reply_markup=cancelkro)
      query.message.delete()
      previous_messages[query.from_user.id] = msg.id  # 🔄 यहाँ `.message_id` की जगह `.id` करें
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
    if user_status.get(user_id) == "chatting_with_ai":
      answer = sendAi_message(user_id,user_name, user_msg)
      await message.reply_text(answer)
    # WB ID Dictionary for different boards and classes

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
                
                result_link = f"https://sainipankaj12.serv00.net/Result/boardresult.php?tag=raj_10_result&roll_no={roll_no}&year=2024&wb_id={wb_id}&source=3&download"
                
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
                  await a.edit_text(f"Faild to get your result!!. Make sure your provided Roll Number is Correct.")
                
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
    else:
        await message.reply_text("⚠️ Please Select a Valid Option.",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚜Home", callback_data="home")]]))
"""
ON CANCEL msg12
"""
@app.on_message(filters.text & ~filters.me & ~filters.group & ~filters.command("start") & filters.regex(r"^🚫CANCEL$"))
def canclemsg(client: Client, message: Message):
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
def send_telegram_message(chat_id, text, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()




def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

# Function to run Pyrogram bot
def run_bot():
    print("Bot is running...")
    send_telegram_message(FILE_CHANNEL_ID, "BOT STARTED SUCCESSFULLY!", BOT_TOKEN)
    app.run()
    print("\nShutting Down...")
    

# Running Flask and Pyrogram bot concurrently using threads
if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    run_bot()  # This will run the bot after Flask starts
#############
"""
Version 2
"""
