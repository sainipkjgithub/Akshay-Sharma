from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,InputMediaPhoto, CallbackQuery,ReplyKeyboardMarkup,KeyboardButton



chat_with_assistant = ReplyKeyboardMarkup(
    [[KeyboardButton("🚫CANCEL")]],
    resize_keyboard=True
)

async def start_params(client, message, start_param):
    if start_param.startswith("request_"):
            request_type = start_param.replace("request_", "", 1).replace('_', ' ').title()
            return await message.reply_text(f"🎬 You requested: `{request_type}`\n\nFetching details...")
    elif start_param =="chatting_with_ai":
        await message.reply_text("We are Connecting You to our Ai Assistent...")
        time.sleep(2)
        await message.delete()
        a=await message.reply_text(f"Hello {user_name}, How can I assist you today..?",reply_markup=chat_with_assistant)
        user_status[user_id] = "chatting_with_ai"
    elif start_param == "rj_result_2025":
        buttons = [
        [InlineKeyboardButton("Class 10", callback_data=f"board_result_rbse_10")],
        [InlineKeyboardButton("Class 12", callback_data=f"board_result_rbse_12")],
        [InlineKeyboardButton("🔙BACK", callback_data=f"available_boards"),
        InlineKeyboardButton("🏠Home", callback_data="home")]
        ]
        await message.reply_text("Chack Your Result in a few Clicks.\n**Rajasthan Board**\nSelect your class:", reply_markup=InlineKeyboardMarkup(buttons))