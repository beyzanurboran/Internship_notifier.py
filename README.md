Youthall Staj İlanları Telegram Botu

Bu Python projesi, Youthall web sitesinden aktif staj ilanlarını çekerek Telegram botu aracılığıyla bildirim olarak göndermektedir.

📌 Özellikler
	•	Web Scraping: Youthall sitesinden aktif staj ilanlarını çeker.
	•	Telegram Bildirimleri: Çekilen ilanları Telegram botu aracılığıyla gönderir.
	•	Otomatik Çalıştırma: Belirli aralıklarla çalıştırılabilir (örn. bir cron job veya scheduler ile).

🛠️ Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki bileşenlerin kurulu olması gerekmektedir:
	•	Python 3.x
	•	requests
	•	BeautifulSoup
	•	python-telegram-bot

Gerekli paketleri yüklemek için: 
pip install requests beautifulsoup4 python-telegram-bot

🔧 Kurulum ve Kullanım
	1.	Telegram Botu Oluşturun:
	•	@BotFather ile yeni bir bot oluşturun.
	•	Size verilen bot token bilgisini kaydedin.
	2.	Chat ID’nizi Öğrenin:
	•	@userinfobot veya başka bir yöntemle chat ID’nizi öğrenin.
	3.	Kod İçerisinde Token ve Chat ID’yi Güncelleyin:
config.py dosyasını oluşturun ve şu şekilde bilgileri ekleyin:

TELEGRAM_BOT_TOKEN = "BOT_TOKENİNİZ"
TELEGRAM_CHAT_ID = "CHAT_IDNİZ"

📚 Kaynaklar
 https://docs.tracardi.com/qa/how_can_i_get_telegram_bot/
 https://youtu.be/I-qI6jeLIsI?si=SLfmRnFVP4aQXIBV
 https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3

⸻

README (English)

Youthall Internship Listings Telegram Bot

This Python project scrapes active internship listings from Youthall and sends them as notifications via a Telegram bot.

📌 Features
	•	Web Scraping: Fetches active internship postings from Youthall.
	•	Telegram Notifications: Sends the collected internship links via a Telegram bot.
	•	Automated Execution: Can be scheduled to run at intervals (e.g., using a cron job or scheduler).

🛠️ Requirements

To run this project, you need:
	•	Python 3.x
	•	requests
	•	BeautifulSoup
	•	python-telegram-bot

Install dependencies using:
pip install requests beautifulsoup4 python-telegram-bot

🔧 Setup & Usage
	1.	Create a Telegram Bot:
	•	Use @BotFather to create a new bot.
	•	Save the bot token provided.
	2.	Get Your Chat ID:
	•	Use @userinfobot or another method to retrieve your chat ID.
	3.	Update Token and Chat ID in the Code:
Create a config.py file and add:
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

📚 Resources
https://docs.tracardi.com/qa/how_can_i_get_telegram_bot/
https://youtu.be/I-qI6jeLIsI?si=SLfmRnFVP4aQXIBV
https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
