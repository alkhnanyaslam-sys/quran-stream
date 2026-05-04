import os
import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

API_ID = 38091412
API_HASH = "e182f84704911e253c33b8015b922cdd"
BOT_TOKEN = os.getenv("BOT_TOKEN")
STREAM_URL = "https://backup.qurango.net/radio/mishary_rashid"

app = Client("quran_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)
active_streams = {}

@app.on_message(filters.command("start"))
async def start_stream(client, message):
    chat_id = message.chat.id
    if chat_id in active_streams:
        await message.reply("🔴 البث مشغل بالفعل!")
        return
    try:
        await call_py.join_group_call(chat_id, MediaStream(STREAM_URL))
        active_streams[chat_id] = True
        await message.reply("✅ تم بدء بث الحرم المكي 🕌")
    except Exception as e:
        await message.reply(f"❌ خطأ: {str(e)}")

@app.on_message(filters.command("stop"))
async def stop_stream(client, message):
    chat_id = message.chat.id
    if chat_id not in active_streams:
        await message.reply("🔴 لا يوجد بث نشط!")
        return
    try:
        await call_py.leave_group_call(chat_id)
        del active_streams[chat_id]
        await message.reply("⏹️ تم إيقاف البث")
    except Exception as e:
        await message.reply(f"❌ خطأ: {str(e)}")

async def main():
    async with app:
        print("🤖 البوت يعمل...")
        await asyncio.sleep(float('inf'))

asyncio.run(main())
