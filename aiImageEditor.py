"""Jai Shree Ram"""
import requests
import json
import time
def ai_image_bg_remove(image_url):
    response = requests.get(f"https://sainipankaj12.serv00.net/Earn/chack_link.php?c={chat_id}")
    
    if response.status_code != 200:
        return "Error: Unable to check link availability."
    
    data = response.json()
def ai_image_enhancer(image_url,msg):
    response = requests.get(f"https://api.paxsenix.biz.id/tools/enhancer?url={image_url}")
    
    if response.status_code != 200:
        print("Wrong URL or server down")
        msg.edit_text("Something went wrong.Please try again later or contact to admin.")
        return
    data = response.json()
    msg.edit_text("UPLOADING YOUR IMAGE...")
    if "task_url" not in data:
        print("Invalid response format")
        msg.edit_text("⚠️Image upload faild!")
        return
    task_url = data["task_url"]
    # Wait for the task to complete
    msg.edit_text("Upload successful!. Enhancing your Image.\n\n Please Wait...")
    time.sleep(10)
    msg.edit_text("Waiting..")
    time.sleep(10)
    msg.edit_text("Processing your Image...")
    time.sleep(10)
    msg.edit_text("Adding some pixel in Your Image. \n \n Please wait...")
    response1 = requests.get(task_url)
    
    if response1.status_code != 200:
        print("Server down")
        msg.edit_text("Server Faild. Please Contact to the admin OR Try again later!")
        return
    time.sleep(5)
    data = response1.json()
    url = data["url"]
    requests.get(url)
    time.sleep(10)
    stream=f"http://api.mrsingodiya.ct.ws/Image_stream?url={url}"
    msg.edit_text("Uploading to telegram...")
    time.sleep(2)
    return stream