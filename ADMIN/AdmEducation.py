"""Jai Shree Ram"""
"""AdmEducation"""
# aded_ Callback_data handler ...
"""@app.on_callback_query(filters.regex("adm_education"))
async def admin_education(client, callback_query):"""
import sys
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton , CallbackQuery, ReplyKeyboardRemove , ForceReply
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import script 
admins = script.admins
adm_education =  InlineKeyboardMarkup([
        [InlineKeyboardButton("Edit Board Result", callback_data="aded_board_result")],
        [InlineKeyboardButton("🔙Back", callback_data="admin")]])

async def admin_edu(client, callback_query):
  user_id = callback_query.from_user.id
  first_name =callback_query.from_user.first_name
  if user_id not in admins:
    return await callback_query.message.edit_text(f"Hey {first_name}, You are Not a admin of this bot You can't Use it.")
  await callback_query.message.edit_text(f"Hello {first_name} 👋, Please Select What's on your Mind.",reply_markup=adm_education)
  
async def admin_education1(client, callback_query):
    user_id = callback_query.from_user.id
    first_name =callback_query.from_user.first_name
    if user_id not in admins:
      return callback_query.answer("⛔ Denied access", show_alert=True)
    callback_data = callback_query.data 
    real_msg = callback_data.replace("aded_", "", 1)
    if real_msg =="board_result":
      return callback_query.answer("Thanks", show_alert=True)