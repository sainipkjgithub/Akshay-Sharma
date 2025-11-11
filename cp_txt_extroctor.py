import requests  
import os  
import json  
import re  
from script import BASE_PATH 
async def fetch_classplus_content(token, course_id,   
                             file_path=f"{BASE_PATH}/ClassPlus/classplus_data.txt",   
                             parent_folder_name=None,   # <-- अब ये optional है  
                             server_path="/storage/emulated/0/ClassPlus/ERTSERVER123"):  
    """  
    Classplus API से course content recursively fetch करता है:  
    - सभी video/pdf URLs txt file में save करता है  
    - हर folder का JSON /ERTSERVER/{courseId}-{folderId}.json में save करता है  
    - अगर video URL नहीं है तो thumbnail URL से master.m3u8 generate करता है  
    - Folder path को ' > ' से जोड़ा जाता है  
    - parent_folder_name optional है  
    """  
    headers = {  
        "accept-encoding": "gzip",  
        "accept-language": "EN",  
        "api-version": "35",  
        "app-version": "1.4.73.2",  
        "build-number": "35",  
        "connection": "Keep-Alive",  
        "content-type": "application/json",  
        "device-details": "Xiaomi_Redmi 7_SDK-32",  
        "device-id": "c28d3cb16bbdac01",  
        "host": "api.classplusapp.com",  
        "region": "IN",  
        "user-agent": "Mobile-Android",  
        "webengage-luid": "00000187-6fe4-5d41-a530-26186858be4c",  
        "x-access-token": token  
    }  

    visited_folders = set()  

    # ---------------------------  
    # URL conversion logic  
    # ---------------------------  
    def convert_url(url_val):  
        if not url_val:  
            return None  

        if "media-cdn.classplusapp.com/tencent/" in url_val:  
            return url_val.rsplit('/', 1)[0] + "/master.m3u8"  
        elif "media-cdn.classplusapp.com" in url_val and url_val.endswith('.jpg'):  
            identifier = url_val.split('/')[-3]  
            return f"https://media-cdn.classplusapp.com/alisg-cdn-a.classplusapp.com/{identifier}/master.m3u8"  
        elif "tencdn.classplusapp.com" in url_val and url_val.endswith('.jpg'):  
            identifier = url_val.split('/')[-2]  
            return f"https://media-cdn.classplusapp.com/tencent/{identifier}/master.m3u8"  
        elif "4b06bf8d61c41f8310af9b2624459378203740932b456b07fcf817b737fbae27" in url_val and url_val.endswith('.jpeg'):  
            identifier = url_val.split('/')[-1].split('.')[0]  
            return f"https://media-cdn.classplusapp.com/alisg-cdn-a.classplusapp.com/b08bad9ff8d969639b2e43d5769342cc62b510c4345d2f7f153bec53be84fe35/{identifier}/master.m3u8"  
        elif "cpvideocdn.testbook.com" in url_val and url_val.endswith('.png'):  
            match = re.search(r'/streams/([a-f0-9]{24})/', url_val)  
            video_id = match.group(1) if match else url_val.split('/')[-2]  
            return f"https://cpvod.testbook.com/{video_id}/playlist.m3u8"  
        elif "media-cdn.classplusapp.com/drm/" in url_val and url_val.endswith('.png'):  
            video_id = url_val.split('/')[-3]  
            return f"https://media-cdn.classplusapp.com/drm/{video_id}/playlist.m3u8"  
        elif "https://media-cdn.classplusapp.com" in url_val and ("cc/" in url_val or "lc/" in url_val or "uc/" in url_val or "dy/" in url_val) and url_val.endswith('.png'):  
            return url_val.replace('thumbnail.png', 'master.m3u8')  
        elif "https://tb-video.classplusapp.com" in url_val and url_val.endswith('.jpg'):  
            video_id = url_val.split('/')[-1].split('.')[0]  
            return f"https://tb-video.classplusapp.com/{video_id}/master.m3u8"  
        elif url_val.endswith('.png'):  
            return url_val.rsplit('/', 1)[0] + "/master.m3u8"  
        return url_val  

    # ---------------------------  
    # Verification logic  
    # ---------------------------  
    def verify_video_url(video_url):  
        return True  
        
    def recursive_fetch(course_id, folder_id, folder_path):  
        if (course_id, folder_id) in visited_folders:  
            return  
        visited_folders.add((course_id, folder_id))  

        url = f"https://api.classplusapp.com/v2/course/content/get?courseId={course_id}&folderId={folder_id}"  
        try:  
            response = requests.get(url, headers=headers, timeout=20)  
            response.raise_for_status()  
            data = response.json()  
        except Exception as e:  
            print(f"[⚠️] Error fetching folder {folder_id}: {e}")  
            return  

        # JSON Save
        """
        json_file_name = os.path.join(server_path, f"{course_id}-{folder_id}.json")  
        with open(json_file_name, "w", encoding="utf-8") as jf:  
            json.dump(data, jf, indent=2)  
        print(f"[💾] JSON saved: {json_file_name}")  
        """
        course_content = data.get("data", {}).get("courseContent", [])  
        for item in course_content:  
            name = item.get("name", "").strip()  
            content_type = item.get("contentType")  
            url_item = item.get("url")  
            thumbnail_url = item.get("thumbnailUrl")  
            sub_folder_id = item.get("id")  
            sub_course_id = item.get("contentCourseId", course_id)  

            # VIDEO  
            if content_type == 2:  
                final_url = convert_url(url_item or thumbnail_url)  
                if final_url and verify_video_url(final_url):  
                    # parent path अगर None है तो ' > ' से शुरू मत करो  
                    prefix = f"{folder_path} > " if folder_path else ""  
                    line = f"{prefix}{name} : {final_url}\n"  
                    with open(file_path, "a", encoding="utf-8") as f:  
                        f.write(line)  
                    print(f"[🎥] {line.strip()}")  

            # PDF  
            elif content_type == 3 and url_item:  
                prefix = f"{folder_path} > " if folder_path else ""  
                line = f"{prefix}{name} : {url_item}\n"  
                with open(file_path, "a", encoding="utf-8") as f:  
                    f.write(line)  
                print(f"[📄] {line.strip()}")  

            # SUB-FOLDER  
            elif content_type == 1:  
                new_path = f"{folder_path} > {name}" if folder_path else name  
                recursive_fetch(sub_course_id, sub_folder_id, new_path)  

    # ---------------------------  
    # Start  
    # ---------------------------  
    if os.path.exists(file_path):  
        os.remove(file_path)  

    recursive_fetch(course_id, 0, parent_folder_name)  
