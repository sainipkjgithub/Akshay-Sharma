"""Jai Baba Ki"""
import script 
waiting_users = script.waiting_users
active_chats = script.active_chats
message_map = script.message_map
user_status = script.user_status
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, ReplyKeyboardRemove , ForceReply
def any_chat_start(client, callback_query):
    import script
    user_status = script.user_status
    print("any :",user_status )
    user_id = callback_query.from_user.id
    message = callback_query.message

    if user_id in active_chats:
        client.send_message(user_id, "आप पहले से किसी से जुड़े हुए हैं।")
        return

    # Bot चेक करके ही connect करें
    while waiting_users:
        partner_id = waiting_users.pop(0)
        partner = client.get_users(partner_id)
        if not partner.is_bot:
            break
    else:
        partner_id = None

    if partner_id:
        active_chats[user_id] = partner_id
        active_chats[partner_id] = user_id

        client.send_message(partner_id, "You have successfully connected.",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⛔️ Disconnecte Partner", callback_data="cancel")]]))
        client.send_message(user_id, "You have successfully connected.",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚫Stop", callback_data="cancel")]]))
        user_status[user_id] = "any_chat_connected"
        user_status[partner_id] = "any_chat_connected"
    else:
        waiting_users.append(user_id)
        user_status[user_id] = "any_chat_waiting"
        client.send_message(user_id, "Searching for a partner...",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚫Cancel Searching", callback_data="cancel")]]))
        print(waiting_users)
#@app.on_message(filters.command("stop") & filters.private & ~filters.me)
async def chat_stop_handler(client, message):
    user_id = message.from_user.id

    if user_id in active_chats:
        partner_id = active_chats[user_id]
        del active_chats[user_id]
        del user_status[user_id]
        del active_chats[partner_id]
        del user_status[partner_id]

        await client.send_message(partner_id, "Chat Stopped by your partner..")
        await message.reply("आपने चैट समाप्त कर दी है।")
    else:
        await message.reply("आप किसी से जुड़े नहीं हैं।")

#@app.on_message(filters.private & ~filters.me & ~filters.command(["start", "stop"]))
async def forward_message(client, message):
    user_id = message.from_user.id

    if user_id not in active_chats:
        await message.reply("You are not connected yet to anyone..",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚫Stop Searching", callback_data="cancel")]]))
        return

    partner_id = active_chats[user_id]
    reply_to_id = None

    if message.reply_to_message:
        original_msg_id = message.reply_to_message.id

        # reverse lookup भी शामिल किया है
        if original_msg_id in message_map:
            reply_to_id = message_map[original_msg_id]

    # पार्टनर को भेजें message
    sent = await client.send_message(
        partner_id,
        message.text,
        reply_to_message_id=reply_to_id if reply_to_id else None
    )

    # दोनों दिशाओं का mapping करें
    message_map[message.id] = sent.id
    message_map[sent.id] = message.id
