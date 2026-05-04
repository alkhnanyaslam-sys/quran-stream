from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream.audio import AudioPiped

API_ID = 38091412
API_HASH = "e182f84704911e253c33b8015b922cdd"
CHAT_ID = -1003373397195
MAKKAH_STREAM = "https://backup.qurango.net/radio/mishary_rashid"

client = Client("quran_session", api_id=API_ID, api_hash=API_HASH)
app = PyTgCalls(client)

@client.on_message(filters.command("start_quran") & filters.chat(CHAT_ID))
async def start_quran(c, message):
    await message.reply("🕌 جاري تشغيل بث الحرم المكي...")
    await app.join_group_call(
        CHAT_ID,
        InputAudioStream(AudioPiped(MAKKAH_STREAM))
    )
    await message.reply("✅ تلاوة الحرم المكي تُبث الآن 🎙️")

@client.on_message(filters.command("stop_quran") & filters.chat(CHAT_ID))
async def stop_quran(c, message):
    await app.leave_group_call(CHAT_ID)
    await message.reply("⏹️ تم إيقاف البث")

client.start()
app.start()
idle()
