import requests
import time

url = "https://mis.kfs.edu.eg/poll_pharm/login.aspx"

def check_server():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    while True:
        try:
            # verify=False لتجاهل مشكلة شهادة الأمان SSL
            response = requests.get(url, headers=headers, verify=False, timeout=10)
            
            # 200 تعني أن الموقع يعمل بنجاح
            if response.status_code == 200:
                print(f"[Success] الموقع يعمل الآن! كود الحالة: {response.status_code}")
                # هنا ممكن تضيف صوت تنبيه أو تخليه يبعتلك إيميل
                break
            else:
                print(f"[Wait] الموقع ما زال لا يستجيب بشكل صحيح. كود الحالة: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"[Error] تعذر الاتصال بالسيرفر حالياً.")

        # هام جداً: الانتظار 60 ثانية لتجنب الحظر
        time.sleep(60)

if __name__ == "__main__":
    # إخفاء تحذيرات SSL المزعجة في التيرمنال
    requests.packages.urllib3.disable_warnings()
    print("جاري مراقبة الموقع...")
    check_server()