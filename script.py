"""Jai Shree Ram"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from ReplyMarckep import home_keyboard, getHelp, earnMoney, aboutUs, wrongbutton, our_telegram_bots1, our_telegram_bots2, our_telegram_bots3, wrong_socialMedia, follow_us, follow_us2,fun,explore_more,college_education, school_education, education, competition_exam, contact_admin, available_boards,earn_term,admin_home
from EARN.earn import term_and_conditions
about_text="""
Hello, I am Akshay Sharma. I am a Technical Partner of Mr. Singodiya.  
I am an all-in-one virtual system designed for **education, image editing, automation, earning, and AI-based solutions**.  
My goal is to simplify complex tasks and enhance productivity through smart technology.
I am built to handle multiple domains efficiently, including content creation, AI-powered automation, and smart integrations.  
With advanced algorithms and intelligent processing, I help users achieve their goals faster and more effectively.  
Innovation and optimization are at the core of my functionality, making tasks easier and more efficient.
"""
startmsg = "Welcome To Singodiya Tech."
admin_home_msg = "Hey Admin Please select a option below"
close_for_bots1 = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔒 CLOSE", callback_data="our_telegram_bots1")]
    ])
close_for_bots2 = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔒 CLOSE", callback_data="ourclose_for_bots2")]
    ])
close_for_bots3 = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔒 CLOSE", callback_data="our_telegram_bots3")]
    ])
CALLBACK123 = {
  "get_help": "Contect Admin to get help",
  "about_us":about_text,
  "contact_admin":"Please Select Contact Method.",
  "home":startmsg,
  "admin_home":admin_home_msg,
  "fun":"This Feature Will Come with next update. STAY TUNNED...",
  "explore_more":"Explore More Features With these Options..",
  "education":"Please Select Your Education Type..",
  "term_and_conditions1":term_and_conditions,
  "school_education":"Select What to do next",
  "available_boards":"Please Select Your Board..",
  "college_education":"Please Select your University. ",
  "competition_exam":"There is no content Please wait for next update...",
  
  "follow_us":"Follow Us using Following Links",
  "follow_us2":"Follow Us using Following Links",
  "our_telegram_bots1":"Welcome to **SingodiyaTech** Here is the More Telegram Bots for Free to use",
  "our_telegram_bots2":"""
  Welcome to **SingodiyaTech** Here is the More Telegram Bots for Free to use
  """,
  "our_telegram_bots3":"MORE **Bots** Comming Soon. Stay Connected...",
  "wrong_socialMedia":"Your Selected Social Media is Not Available This time. We don't have any account on this Social Media. Please Try Again after Few Days",
  "ai_image_generator": "[AI Image Generator](https://t.me/Image_generate1bot) एक स्मार्ट टूल है, जो आर्टिफिशियल इंटेलिजेंस की मदद से आपके बताए गए विवरण के आधार पर उच्च-गुणवत्ता वाली इमेज बनाता है। यह क्रिएटिव आर्टिस्ट, डिज़ाइनर और कंटेंट क्रिएटर्स के लिए एक उपयोगी टूल हो सकता है।\nhttps://t.me/Image_generate1bot\nhttps://t.me/Image_generate1bot ",
  
  "ai_assistent": "AI Assistant एक इंटेलिजेंट चैटबॉट है, जो आपके सवालों के जवाब देने, डेली टास्क में मदद करने और इंफॉर्मेशन प्रोवाइड करने के लिए डिज़ाइन किया गया है। यह आपको टेक्नोलॉजी, एजुकेशन, हेल्थ और अन्य विषयों पर सहायक जानकारी प्रदान कर सकता है।",
  
  "ai_movie_provider": "AI Movie Provider एक ऑटोमेटेड सर्विस है, जो आपको फिल्मों की सिफारिश देता है और आपकी पसंद के आधार पर मूवी सजेस्ट करता है। यह नए रिलीज़, ट्रेंडिंग फिल्में और आपके पसंदीदा जॉनर के आधार पर कस्टमाइज्ड मूवी सजेशन प्रदान करता है।",
  
  "upsc_helper": "UPSC Helper उन छात्रों के लिए डिज़ाइन किया गया है, जो UPSC और अन्य सरकारी परीक्षाओं की तैयारी कर रहे हैं। यह टूल महत्वपूर्ण अध्ययन सामग्ी, करंट अफेयर्स, नोट्स और प्रैक्टिस क्वेश्चन उपलब्ध कराता है, जिससे छात्रों को अपनी तैयारी में मदद मिलती है।",
  
  "earn_money_bot": "Earn Money बॉट विभिन्न ऑनलाइन तरीकों से पैसे कमाने के सुझाव देता है। यह फ्रीलांसिंग, इन्वेस्टमेंट, एफिलिएट मार्केटिंग और अन्य ऑनलाइन बिज़नेस आइडियाज से जुड़ी जानकारी प्रदान करता है।"
}
ReplyMarkup123 = {
  "get_help":getHelp,
  "our_telegram_bots1":our_telegram_bots1,
  "our_telegram_bots2":our_telegram_bots2,
  "our_telegram_bots3":our_telegram_bots3,
  "about_us":aboutUs,
  "contact_admin":contact_admin,
  "home":home_keyboard,
  "admin_home":admin_home,
  "wrong_socialMedia":wrong_socialMedia,
  "follow_us":follow_us,
  "follow_us2":follow_us2,
  "fun":fun,
  "explore_more":explore_more,
  "education":education,
  "school_education":school_education,
  "college_education":college_education,
  "competition_exam":competition_exam,
  "available_boards" : available_boards,
  "term_and_conditions1":earn_term,
  "ai_image_generator": close_for_bots1,
  "ai_assistent": close_for_bots1,
  "ai_movie_provider" : close_for_bots1,
  "upsc_helper" : close_for_bots1,
  "earn_money_bot": close_for_bots1
  
  
  
  
  }
wrongbutton =wrongbutton
