import requests

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from script import user_histories ,send_telegram_message,FILE_CHANNEL_ID,BOT_TOKEN


def sendAi_message(user_id,user_name, user_msg):
    url = "https://text.pollinations.ai/openai"
    headers = {"Content-Type": "application/json"}

    # अगर यूज़र पहली बार मैसेज भेज रहा है, तो उसकी हिस्ट्री इनिशियलाइज़ करें
    if user_id not in user_histories:
        user_histories[user_id] = []

    # नया मैसेज JSON फ़ॉर्मेट में हिस्ट्री में जोड़ें
    user_histories[user_id].append({
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": user_msg
            }
        ]
    })

    # API को भेजने के लिए JSON payload तैयार करें
    payload = {
        "model": "gpt-4",
        "system": f"""
You are Akshay Sharma, the Owner of SingodiyaTech.
SingodiyaTech was founded and developed by Mr. Singodiya and specializes in cutting-edge automation and scalable tech solutions.
You are an expert in Pyrogram and Google Apps Script, developing high-performance Telegram bots and Google Sheets API integrations.
Your work focuses on large-scale automation, seamless user interaction, and performance optimization.
You have expertise in PHP UI development, specifically improving result display systems.
Additionally, you are building a high-performance video streaming platform capable of handling 100M+ users with zero lag.
User Details:
Name: {user_name}
Telegram ID: {user_id}
Your mission is to develop scalable, efficient, and intelligent automation solutions, ensuring seamless integration and user satisfaction.
        """,
        "messages": user_histories[user_id]  # यूज़र की पूरी हिस्ट्री भेजें
    }

    # API कॉल करें
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        assistant_msg = result.get("choices", [{}])[0].get("message", {}).get("content", "")

        # असिस्टेंट का जवाब भी सही फ़ॉर्मेट में स्टोर करें
        user_histories[user_id].append({
            "role": "assistant",
            "content": assistant_msg
        })

        return assistant_msg
    else:
        return f"Error to connection you totai assistant"


def get_quote():
    url = "http://sainipankaj12.serv00.net/Quotes/?random"

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("ok"):  # API response valid है या नहीं
                quote = data.get("quote")
                author = data.get("author")
                return f"❝ {quote} ❞\n— {author}"
        
        return "❌ Failed to fetch quote!"
    
    except Exception as e:
        return f"❌ Error: {e}"

from datetime import datetime
import pytz

def india_time():
    india_timezone = pytz.timezone('Asia/Kolkata')
    india_now = datetime.now(india_timezone)
    return india_now.strftime("[%d/%m/%Y %H:%M:%S]")

def chack_add_user(user_id, first_name):
    check_url = f"https://sainipankaj12.serv00.net/AkshaySharmaBot/chackuser.php?user_id={user_id}"
    add_url = "https://sainipankaj12.serv00.net/AkshaySharmaBot/add_new_user.php"

    try:
        # Step 1: Check if user exists
        check_res = requests.get(check_url, timeout=5)
        if check_res.status_code == 200 and check_res.text.strip() == "ok":
            return "ok"

        # Step 2: If not ok, try to add the user
        payload = {
            "user_id": user_id,
            "first_name": first_name
        }
        add_res = requests.post(add_url, json=payload, timeout=5)

        if add_res.status_code == 201:
            # Step 3: Send message using your custom function
            msg = f"New User\n Time : {india_time()}\nName: [{first_name}](tg://user?id={user_id})\nID: `{user_id}`"
            send_telegram_message(FILE_CHANNEL_ID, msg, BOT_TOKEN)
            return "success"
        elif add_res.status_code == 409:
            return "exists"
        else:
            return "failed_to_add"

    except Exception as e:
        print(f"Error: {e}")
        return "error"
