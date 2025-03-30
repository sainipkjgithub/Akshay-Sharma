"""Jai Shree Ram"""
#Version 2.3.4
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton


home_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 Our Telegram Bots", callback_data="our_telegram_bots1"),
         InlineKeyboardButton("🌍 Our Website", url="https://mrsingodiya.ct.ws/")],
        [InlineKeyboardButton("📢 Follow us on Social", callback_data="follow_us"),
         InlineKeyboardButton("💬 Chat With Assistant", callback_data="chat_with_assistant")],
         [InlineKeyboardButton("💰 Earn Money", callback_data="earn_money")],
         [InlineKeyboardButton("Explore More", callback_data="explore_more")],
        [InlineKeyboardButton("❓ Get Help", callback_data="get_help"),
        InlineKeyboardButton("ℹ️ About Us", callback_data="about_us")]
         
    ])
admin_home_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 Our Telegram Bots", callback_data="our_telegram_bots1"),
         InlineKeyboardButton("🌍 Our Website", url="https://mrsingodiya.ct.ws/")],
        [InlineKeyboardButton("📢 Follow us on Social", callback_data="follow_us"),
         InlineKeyboardButton("💬 Chat With Assistant", callback_data="chat_with_assistant")],
         [InlineKeyboardButton("💰 Earn Money", callback_data="earn_money")],
         [InlineKeyboardButton("Explore More", callback_data="explore_more")],
        [InlineKeyboardButton("❓ Get Help", callback_data="get_help"),
        InlineKeyboardButton("ℹ️ About Us", callback_data="about_us")],
        [InlineKeyboardButton("Admin", callback_data="admin_home")]
         
    ])
admin_home = InlineKeyboardMarkup([
        [InlineKeyboardButton("Upload Premium App", callback_data="adm_upload_premium_app")],
        [InlineKeyboardButton("BLOCK USER", callback_data="adm_block_user"),
        InlineKeyboardButton("Add Admin", callback_data="adm_add_admin")],
        [InlineKeyboardButton("ADMINS", callback_data="adm_admins")],
        [InlineKeyboardButton("⚜️Home", callback_data="home")]
    ])
cancel12 = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚫Cancel", callback_data="cancel")]])
help_keyboard =  ReplyKeyboardMarkup(
    [[KeyboardButton("Option 1"), KeyboardButton("Option 2")]],
    resize_keyboard=True
)

wrongbutton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌍 Our Website", url="https://mrsingodiya.blogspot.com")],
        [InlineKeyboardButton("📞 Contact Admin", callback_data="contact_admin"),
        InlineKeyboardButton("🏠Home", callback_data="home")]
         ])
         
contact_admin = InlineKeyboardMarkup([
        [InlineKeyboardButton("Email",url="https://urlshortner.pkjsaini42.workers.dev/Email_Me")],
        [InlineKeyboardButton("Telegram", user_id=6150091802),
        InlineKeyboardButton("🏠Home", callback_data="home")]
         ])
getHelp = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌍 Our Website", url="https://mrsingodiya.blogspot.com/p/contact-us.html"),
         InlineKeyboardButton("📞 Contact Admin", url="https://t.me/aks979")],
         [InlineKeyboardButton("🏠Home", callback_data="home")]
         ])
chat_with_assistant = ReplyKeyboardMarkup(
    [[KeyboardButton("🚫CANCEL")]],
    resize_keyboard=True
)
cancelkro = ReplyKeyboardMarkup(
    [[KeyboardButton("🚫CANCEL")]],
    resize_keyboard=True
)
help_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Contact", user_id=6150091802)]])

def earnMoney(link):
  share_text = "Hello! Please Click on the Link:\n" + link
  encoded_text = share_text.replace("\n", "%0A").replace(" ", "%20")
  share_url = f"https://t.me/share/url?url={encoded_text}"
  return InlineKeyboardMarkup([
         [InlineKeyboardButton("Refresh♻️", callback_data="Refresh_earning"),
         InlineKeyboardButton("🔗 Share Link", url=share_url)],
         [InlineKeyboardButton("Term And Conditions", callback_data="term_and_conditions1"),
         InlineKeyboardButton("Withdraw Your Earning", callback_data="withdrawal")],
         [InlineKeyboardButton("CLOSE 🔒", callback_data="home")]
         
    ])
follow_us = InlineKeyboardMarkup([
         [InlineKeyboardButton("🌍 Our Website", url="http://mrsingodiya.blogspot.com/")],
         [InlineKeyboardButton("Telegram", url="https://t.me/aibots72"),
         InlineKeyboardButton("YouTube", url="https://youtu.be/eDV_qiXRgr8>")],
         [InlineKeyboardButton("Instagram", callback_data="wrong_socialMedia"),
         InlineKeyboardButton("Facebook", callback_data="wrong_socialMedia")],
         [InlineKeyboardButton("🏠 Home", callback_data="home")]
         
    ])
earn_term = InlineKeyboardMarkup([
         [InlineKeyboardButton("CLOSE 🔒", callback_data="Refresh_earning")]])
follow_us2 = InlineKeyboardMarkup([
         [InlineKeyboardButton("🌍 Our Website", url="https://mrsingodiya.ct.ws/")],
         [InlineKeyboardButton("Telegram", url="https://t.me/aibots72"),
         InlineKeyboardButton("YouTube", url="https://youtu.be/eDV_qiXRgr8")],
         [InlineKeyboardButton("Instagram", callback_data="wrong_socialMedia"),
         InlineKeyboardButton("Facebook", callback_data="wrong_socialMedia")],
         [InlineKeyboardButton("Back", callback_data="earnMoney"),
         InlineKeyboardButton("🏠 Home", callback_data="home")]
         
    ])
wrong_socialMedia = InlineKeyboardMarkup([
         [InlineKeyboardButton("Back", callback_data="follow_us"),
         InlineKeyboardButton("🏠 Home", callback_data="home")]
         ])
  
aboutUs = InlineKeyboardMarkup([[InlineKeyboardButton("CLOSE 🔒", callback_data="home")]])
    
                     
our_telegram_bots1 = InlineKeyboardMarkup([
        [InlineKeyboardButton("AI IMAGE GENERATOR", callback_data="ai_image_generator"),
         InlineKeyboardButton("AI ASSISTENT", callback_data="ai_assistent")],
        [InlineKeyboardButton("AI MOVIE PROVIDER", callback_data="ai_movie_provider"),
        InlineKeyboardButton("Movie PROVIDER", callback_data="movie_provider")],
         [InlineKeyboardButton("UPSC HELPER", callback_data="upsc_helper"),
         InlineKeyboardButton("💰 Earn Money", callback_data="earn_money_bot")],
        [InlineKeyboardButton("BACK", callback_data="home"),
        InlineKeyboardButton("NEXT⏭️", callback_data="our_telegram_bots2")]
    ])
our_telegram_bots2 = InlineKeyboardMarkup([
        [InlineKeyboardButton("SHARE LINK GENERATOR", callback_data="share_link_generator"),
         InlineKeyboardButton("DICTIONARY", callback_data="dictionary_bot")],
        [InlineKeyboardButton("BOARD CLASS RESULT", callback_data="board_class_result"),
        InlineKeyboardButton("DOUBT SOLVER", callback_data="doubt_solver")],
         [InlineKeyboardButton("UPSC HELPER", callback_data="upsc_helper"),
         InlineKeyboardButton("E-PDF HUB", callback_data="e_pdf_hub")],
        [InlineKeyboardButton("⏮️PREVIOUS", callback_data="our_telegram_bots1"),
        InlineKeyboardButton("Back", callback_data="home"),
        InlineKeyboardButton("NEXT⏭️", callback_data="our_telegram_bots3")]
    ])
our_telegram_bots3 = InlineKeyboardMarkup([
        [InlineKeyboardButton("E-PAPER", callback_data="our_telegram_bots3")],
        [InlineKeyboardButton("⏮️PREVIOUS", callback_data="our_telegram_bots2"),
        InlineKeyboardButton("Back", callback_data="home")]
    ])
download_any_video = InlineKeyboardMarkup([
        [InlineKeyboardButton("Let's Fun", callback_data="fun")],
        [InlineKeyboardButton("️🔙Back", callback_data="explore_more"),
        InlineKeyboardButton("🏠Home", callback_data="home")]
    ])
explore_more = InlineKeyboardMarkup([
        [InlineKeyboardButton("Let's Fun", callback_data="fun"),
        InlineKeyboardButton("Download Any Video", callback_data="download_any_video")],
        [InlineKeyboardButton("AI Image Editor", callback_data="ai_image_editor"),
         InlineKeyboardButton("EDUCATION", callback_data="education")],
         [InlineKeyboardButton("Motivational Quota", callback_data="motivational_quota")],
         [InlineKeyboardButton("Premium Apps", callback_data="premium_apps")],
        [InlineKeyboardButton("🔙Back", callback_data="home")]
    ])
ai_image_editor = InlineKeyboardMarkup([
        [InlineKeyboardButton("Image Enhance", callback_data="Enhance")]])
fun = InlineKeyboardMarkup([
  [InlineKeyboardButton("🏠 Home", callback_data="home")],])
#######

################################_________________________
####### """ EDUCATION """  #########
#_________________
education = InlineKeyboardMarkup([
        [InlineKeyboardButton("SCHOOL", callback_data="school_education")],
        [InlineKeyboardButton("COLLEGE", callback_data="college_education")],
        [InlineKeyboardButton("COMPETITION EXAM", callback_data="competition_exam")],
        [InlineKeyboardButton("🔙Back", callback_data="explore_more"),
        InlineKeyboardButton("🏠 HOME", callback_data="home")]
    ])
school_education = InlineKeyboardMarkup([
        [InlineKeyboardButton("BOARD CLASS RESULT", callback_data="available_boards")],
        [InlineKeyboardButton("Comming Soon...", callback_data="comming_soon")],
        [InlineKeyboardButton("🔙Back", callback_data="education"),
        InlineKeyboardButton("🏠 HOME", callback_data="home")]
    ])
college_education = InlineKeyboardMarkup([
    [InlineKeyboardButton("RAJASTHAN UNIVERSITY", url="https://www.uniraj.ac.in/"),
     InlineKeyboardButton("MAHARANA PRATAP UNIVERSITY", url="http://www.mpuat.ac.in/")],
    
    [InlineKeyboardButton("KOTA UNIVERSITY", url="https://www.uok.ac.in/"),
     InlineKeyboardButton("MOHANLAL SUKHADIA UNIVERSITY", url="https://www.mlsu.ac.in/")],
    
    [InlineKeyboardButton("JNV UNIVERSITY", url="https://www.jnvu.edu.in/"),
     InlineKeyboardButton("SUKHADIA UNIVERSITY", url="https://www.mlsu.ac.in/")],
    
    [InlineKeyboardButton("JAIPUR NATIONAL UNIVERSITY", url="https://www.jnujaipur.ac.in/"),
     InlineKeyboardButton("NIMS UNIVERSITY", url="https://www.nimsuniversity.org/")],
    
    [InlineKeyboardButton("MODY UNIVERSITY", url="https://www.modyuniversity.ac.in/"),
     InlineKeyboardButton("AMITY UNIVERSITY RAJASTHAN", url="https://www.amity.edu/jaipur/")],
    
    [InlineKeyboardButton("🔙Back", callback_data="education"),
     InlineKeyboardButton("🏠 HOME", callback_data="home")]
])

competition_exam = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔙Back", callback_data="education"),
    InlineKeyboardButton("🏠 HOME", callback_data="home")]
])
available_boards = InlineKeyboardMarkup([
        [InlineKeyboardButton("RBSE BOARD", callback_data="board_result_rbse")],
        [InlineKeyboardButton("UP BOARD", callback_data="board_result_up")],
        [InlineKeyboardButton("🔙Back", callback_data="school_education"),
        InlineKeyboardButton("🏠 HOME", callback_data="home")]
    ])
    
    
back_enter_rollnumber = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔙Back", callback_data="cancel"),
    InlineKeyboardButton("🏠 HOME", callback_data="home")]
])
verify_premium_upload  = InlineKeyboardMarkup([
        [InlineKeyboardButton("Upload Premium App", callback_data="adm_upload_ok"),
        InlineKeyboardButton("Don't Upload", callback_data="adm_upload_ar")]])
