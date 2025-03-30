import requests
from bs4 import BeautifulSoup

# Telegram Bot Token ve Chat ID
TELEGRAM_BOT_TOKEN = "Your token"
TELEGRAM_CHAT_ID = "your chat id"


URL = "https://www.youthall.com/tr/talent-programs/?page=1&order=6"

def get_talent_programs():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        programs = soup.find_all("div", class_="y-talent box_hover border-line-light-blue shadow-light")
        program_list = []

        for program in programs:
            title_element = program.find("div", class_="y-talent_title")
            title = title_element.find("label").get_text(strip=True)
            link_element = program.find("a", href= True)
            link = "https://www.youthall.com" + link_element["href"]
            program_list.append(f"{title}\n{link}")

        return program_list

    return []

def send_telegram_notification(message):
    telegram_api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(telegram_api_url, json=payload)
    print(f"Bildirim Gönderildi: {message}")
    print(f"Status Code: {response.status_code}")
    print(response.json())

programs = get_talent_programs()
if programs:
    for program in programs:
        send_telegram_notification(program)
else:
    send_telegram_notification("Yeni yetenek programı bulunamadı!")
