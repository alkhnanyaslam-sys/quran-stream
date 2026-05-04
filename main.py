from telethon import TelegramClient, events
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream

API_ID = 38091412
API_HASH = "e182f84704911e253c33b8015b922cdd"
CHAT_ID = -1003373397195
MAKKAH_STREAM = "https://backup.qurango.net/radio/mishary_rashid"

client = TelegramClient("quran_session", API_ID, API_HASH)
app = PyTgCalls(client)

@client.on(events.NewMessage(pattern="/start_quran", chats=CHAT_ID))
async def start_quran(event):
    await event.reply("🕌 جاري تشغيل بث الحرم المكي...")
    app.play(CHAT_ID, MediaStream(MAKKAH_STREAM))
    await event.reply("✅ تلاوة الحرم المكي تُبث الآن 🎙️")

@client.on(events.NewMessage(pattern="/stop_quran", chats=CHAT_ID))
async def stop_quran(event):
    app.leave_group_call(CHAT_ID)
    await event.reply("⏹️ تم إيقاف البث")

client.start()
app.start()
idle()
