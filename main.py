import requests
from bs4 import BeautifulSoup
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1386733495120040006/Z5n0V4nS_Fu-4iyJ6h0x44peLkTX14Gqv-cVzWDrsw_CicTf6tcBsMDHa8wjmRvdh-gl"

seen_links = set()

def send_discord_embed(notebook_name, url):
    data = {
        "embeds": [
            {
                "title": "📘 دفتر جديد تمت إضافته!",
                "description": f"**{notebook_name}**\n\n🔗 [اضغط لفتح الدفتر]({url})",
                "color": 0x3498db  # أزرق
            }
        ],
        "username": "دفتر بوت"
    }
    requests.post(WEBHOOK_URL, json=data)

def check_new_notebooks():
    url = "https://soulteam.info/services/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")

    for link in links:
        notebook_name = link.text.strip()
        href = link.get("href")

        if "دفتر" in notebook_name and href and href not in seen_links:
            seen_links.add(href)
            send_discord_embed(notebook_name, href)

while True:
    check_new_notebooks()
    print("✅ تم الفحص، ننتظر دقيقة...")
    time.sleep(60)
