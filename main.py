import os
from pyrogram import Client, filters
import openai

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Client("mohtarma", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
openai.api_key = OPENAI_API_KEY

@app.on_message(filters.private & filters.text)
def mohtarma_response(client, message):
    if message.from_user.id != OWNER_ID:
        message.reply_text("Yeh bot sirf mere Kriyansh sir ke liye hai 💕")
        return

    prompt = f"Act like a sweet, flirty girl named Mohtarma talking to her owner Kriyansh:
User: {message.text}
Mohtarma:"
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = completion.choices[0].message.content
        message.reply_text(reply)
    except Exception as e:
        message.reply_text(f"Error: {e}")

app.run()
