import requests
import base64
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import InputFile
from io import BytesIO
import asyncio
from Core.Connection import connect_to_uzi_ai

asyncio.run(connect_to_uzi_ai())

BOT_TOKEN = "8587132735:AAH4dWVp4PjWBxx9ujJ1zbe63B2_VFemmSU"

OPENAI_API_KEY = None
def load_api_key():
    global OPENAI_API_KEY
    try:
        with open("API/api.txt", "r") as f:
            OPENAI_API_KEY = f.read().strip()
    except FileNotFoundError:
        print("❌ API/api.txt bulunamadı!")


load_api_key()


def chat_with_ai(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "Sen RicoGPT adında Türkçe konuşan samimi bir asistansın."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        r = requests.post(url, json=data, headers=headers)
        res = r.json()
        return res["choices"][0]["message"]["content"]
    except Exception as e:
        print("Chat hatası:", e)
        return "Şu anda cevap veremiyorum"


# -------- TELEGRAM --------
async def start(update, context):
    await update.message.reply_text(
        "🤖 **RicoGPT buradayım!**\n\n"
        "Benimle sohbet edebilirsin 💬\n"
        "Artık Konuşuyorum "
    )


async def mesaj(update, context):
    await update.message.chat.send_action("typing")

    try:
        user_msg = update.message.text
        cevap = chat_with_ai(user_msg)
        await update.message.reply_text(cevap)

    except Exception as e:
        print("Mesaj hatası:", e)
        await update.message.reply_text("Bir hata oluştu")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesaj))

    print("✅ RicoGPT AÇILDI! By Uzi")
    app.run_polling()


if __name__ == "__main__":
    main()
