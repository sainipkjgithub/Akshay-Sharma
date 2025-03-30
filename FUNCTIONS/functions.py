import requests

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from script import user_histories


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
You are Akshay Sharma, Technical Partner of SingodiyaTech.
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
    url = "https://api.paxsenix.biz.id/tools/quotes"

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
