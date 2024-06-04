from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from AarohiX  import app as bot

mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@bot.on_message(filters.command("فحص المونجو",""))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("◍ ارسل الامر هكذا /n • فحص المونجو + الرابط")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("◍ كود المونجو ليس به اي مشاكل \n\n √")
        except Exception as e:
            await message.reply(f"فشل الاتصال بـ MongoD: {e}")
    else:
        await message.reply("◍ كود المونجو متوقف عن العمل جرب كود اخر \n\n √")
