import requests
import base64
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import InputFile
from io import BytesIO
import asyncio
from Core.Connection import connect_to_uzi_ai
asyncio.run(connect_to_uzi_ai())

BOT_TOKEN = "8367415304:AAHH8LC07H7yqBszmRiRYtLAhl3HS_YxS4g"

def load_api_key():
    try:
        with open("API/api.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("❌ API/api.txt bulunamadı!")
        return None

def generate_image(prompt):
    url = "https://api.openai.com/v1/images/generations"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    data = {"model": "gpt-image-1", "prompt": prompt, "size": "1024x1024"}
    try:
        r = requests.post(url, json=data, headers=headers)
        res = r.json()
        if "data" in res:
            if "b64_json" in res["data"][0]:
                img_bytes = base64.b64decode(res["data"][0]["b64_json"])
                return BytesIO(img_bytes)
            elif "url" in res["data"][0]:
                img_data = requests.get(res["data"][0]["url"]).content
                return BytesIO(img_data)
        print("Image yanıtı beklenmedik formatta:", res)
        return None
    except Exception as e:
        print("Image hatası:", e)
        if "billing_hard_limit" in str(e) or "limit" in str(e):
            return "LIMIT_ERROR"
        return None

# ----- Bot komutları -----
async def start(update, context):
    await update.message.reply_text("Selam! Ben RicoGPT 🤖\nSadece fotoğraf üretebilirim!")

async def mesaj(update, context):
    await update.message.chat.send_action("typing")
    try:
        user_msg = update.message.text.lower()
        if "video" in user_msg:
            await update.message.reply_text("Video üretilme özelliği yoktur! Yakın zamanda gelecektir!")
        elif "fotoğraf" in user_msg or "resim" in user_msg:
            image = generate_image(user_msg)
            if image == "LIMIT_ERROR":
                await update.message.reply_text("Fotoğraf API limiti dolmuş! Lütfen daha sonra deneyin.")
            elif image:
                await update.message.reply_photo(photo=InputFile(image, filename="image.png"))
            else:
                await update.message.reply_text("Fotoğraf oluşturulamadı. Promptu detaylandırmayı deneyin.")
        else:
            await update.message.reply_text("Fotoğraf istemek için 'fotoğraf' veya 'resim' yazınız.")
    except Exception as e:
        print("Mesaj işleme hatası:", e)
        await update.message.reply_text("Hata oldu, API anahtarını veya servisi kontrol et.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, mesaj))
    print("RicoGPT AÇILDI! By Uzi!")
    app.run_polling()

if __name__ == "__main__":
    main()