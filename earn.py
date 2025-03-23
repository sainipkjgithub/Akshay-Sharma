"""Jai Shree Ram """
import requests
import json
url = "https://sainipankaj12.serv00.net/Earn/get_clicks.php?c="  # अपनी API का URL डालें
def earn_Money123GetClick(chat_id, w_click):
  response = requests.get(f"{url}{chat_id}")
  data = response.json()
  w_click1 = w_click
  if w_click1 == "today":
    return data["today_click"]
  elif w_click1 == "total":
    return data["total_clicks"]


links = {
    "1": "https://whoushex.top/4/8943860",
    "2": "https://whoushex.top/4/9113420",
    "3": "https://whoushex.top/4/9111260",
    "4": "https://whoushex.top/4/9111270",
    "5": "https://whoushex.top/4/9111277",
    "6": "https://whoushex.top/4/9109258",
    "7": "https://whoushex.top/4/9111282",
    "8": "https://whoushex.top/4/9111285",
    "9": "https://whoushex.top/4/9111286"
}

def provide_earn_Money_link(chat_id):
    response = requests.get(f"https://sainipankaj12.serv00.net/Earn/chack_link.php?c={chat_id}")
    
    if response.status_code != 200:
        return "Error: Unable to check link availability."
    
    data = response.json()
    
    if data.get("available"):
        return f"https://urlshortner.pkjsaini42.workers.dev/{chat_id}"
    else:
        # चैट आईडी के पहले अंक के अनुसार लिंक चुनना
        first_digit = str(chat_id)[0]
        selected_link = links.get(first_digit, links["9"])  # Default link9
        
        create_response = requests.get(f"https://sainipankaj12.serv00.net/Earn/?c={chat_id}&link={selected_link}")
        
        if create_response.status_code == 200:
            return f"https://urlshortner.pkjsaini42.workers.dev/{chat_id}"
        else:
            return "Error: Unable to create earning link."
term_and_conditions = """
📜 **Terms & Conditions for Earning Program**  

By participating in this program, you agree to the following terms:  

### 🔹 **General Terms**  
1️⃣ **Genuine Traffic Only** – Invalid clicks, bot traffic, VPN/proxy usage, or fraudulent activity will lead to account suspension and earnings forfeiture.  
2️⃣ **Earnings Calculation** – You will earn ₹0.50 per valid click. The CPM (Cost per 1000 clicks) is ₹500.  
3️⃣ **Fair Usage Policy** – Misleading people, spamming, or sharing links in unauthorized places (like restricted groups or illegal websites) is strictly prohibited.  

### 🔹 **Withdrawal & Payment**  
4️⃣ **Minimum Withdrawal Amount** – ₹600  
5️⃣ **Withdrawal Processing Time** – Payouts will be processed within 48-72 hours. However, delays may occur due to verification or technical issues.  
6️⃣ **Payment Method** – Withdrawals will be sent via **UPI, Paytm, Bank Transfer, or any supported payment method**. Ensure correct details to avoid failed transactions.  
7️⃣ **Tax & Deductions** – Any applicable taxes or platform fees will be deducted from your earnings.  

### 🔹 **Account & Policy Violations**  
8️⃣ **Multiple Accounts Not Allowed** – Users cannot create multiple accounts. Detection will result in a permanent ban and loss of earnings.  
9️⃣ **False Claims & Disputes** – Raising fake disputes or providing incorrect information may lead to account suspension.  
🔟 **Right to Terminate** – The platform reserves the right to modify terms, change rates, or terminate accounts if suspicious activity is detected.  

📩 **For support, contact our help desk.**  

✅ Follow the rules, start sharing, and enjoy your earnings! 🚀
"""
def refresh_total_clicks(total_click,Earn_link,today_click):
  return f"""
💰 Earn Money with Telegram! 🤑💸  

Now you can --**make money**-- just by sharing a link!  

🔗 --**Your Earning Link:**--
{Earn_link}  


--**📢 How It Works?  **--
1️⃣ **Share** this link with your friends, family, or social media.  
2️⃣ **Ask them** to open the link.  
3️⃣ **Earn money** for every valid click!  

  

--📊 **Today's Performance**--
🔹 **Clicks Received:** `{today_click}`  
🔹 **Earnings Today:** `₹{today_click * 0.5}`  
🔹 **Current CPM:** `₹500`  

  

--💰 **Total Earnings**--
🔸 **Total Clicks:** `{total_click}`  
🔸 **Total Earned:** `₹{total_click * 0.5}`  
🔸 **Average CPM:** `₹500`  



--**Withdraw Your Earnings!**--
✅ Minimum withdrawal: **₹600**  
✅ Request payout anytime!  

⚠ --**Note:** --Please read our **Terms & Conditions** before using this feature.  

Start sharing and start earning now! 🚀
  """
  
  
def refresh_link(link):
  return f"""
💰 Earn Money with Telegram! 🤑💸  

Now you can --**make money**-- just by sharing a link!  

🔗 --**Your Earning Link:**--
{link}  


--**📢 How It Works?  **--
1️⃣ **Share** this link with your friends, family, or social media.  
2️⃣ **Ask them** to open the link.  
3️⃣ **Earn money** for every valid click!  

  

--📊 **Today's Performance**--
🔹 **Clicks Received:** `Getting Data...`  
🔹 **Earnings Today:** `...`  
🔹 **Current CPM:** `₹500`  

  

--💰 **Total Earnings**--
🔸 **Total Clicks:** `Refreshing...`  
🔸 **Total Earned:** `...`  
🔸 **Average CPM:** `₹500`  



--**Withdraw Your Earnings!**--
✅ Minimum withdrawal: **₹600**  
✅ Request payout anytime!  

⚠ --**Note:** --Please read our **Terms & Conditions** before using this feature.  

Start sharing and start earning now! 🚀
  """
def refresh_today_clicks(today_click,Earn_link):
  return f"""
💰 Earn Money with Telegram! 🤑💸  

Now you can --**make money**-- just by sharing a link!  

🔗 --**Your Earning Link:**--
{Earn_link}  


--**📢 How It Works?  **--
1️⃣ **Share** this link with your friends, family, or social media.  
2️⃣ **Ask them** to open the link.  
3️⃣ **Earn money** for every valid click!  

  

--📊 **Today's Performance**--
🔹 **Clicks Received:** `{today_click}`  
🔹 **Earnings Today:** `₹{today_click * 0.5}`  
🔹 **Current CPM:** `₹500`  

  

--💰 **Total Earnings**--
🔸 **Total Clicks:** `Getting Data...`  
🔸 **Total Earned:** `...`  
🔸 **Average CPM:** `₹500`  



--**Withdraw Your Earnings!**--
✅ Minimum withdrawal: **₹600**  
✅ Request payout anytime!  

⚠ --**Note:** --Please read our **Terms & Conditions** before using this feature.  

Start sharing and start earning now! 🚀
  """
  
refresh_clicks = f"""
💰 Earn Money with Telegram! 🤑💸  

Now you can --**make money**-- just by sharing a link!  

🔗 --**Your Earning Link:**--
`Getting Link...`  


--**📢 How It Works?  **--
1️⃣ **Share** this link with your friends, family, or social media.  
2️⃣ **Ask them** to open the link.  
3️⃣ **Earn money** for every valid click!  

  

--📊 **Today's Performance**--
🔹 **Clicks Received:** `Refreshing...`  
🔹 **Earnings Today:** `...`  
🔹 **Current CPM:** `₹500`  

  

--💰 **Total Earnings**--
🔸 **Total Clicks:** `Refreshing...`  
🔸 **Total Earned:** `...`  
🔸 **Average CPM:** `₹500`  



--**Withdraw Your Earnings!**--
✅ Minimum withdrawal: **₹600**  
✅ Request payout anytime!  

⚠ --**Note:** --Please read our **Terms & Conditions** before using this feature.  

Start sharing and start earning now! 🚀
"""