import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from AarohiX import app
from random import  choice, randint


@app.on_message(filters.command(["ايدي"], ""))
async def madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.get_chat_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""╭⦿ᚐɴᴧᴍᴇ : {message.from_user.username}
╰⦿ᚐᴜsᴇꝛ : {3}
╭⦿ᚐɪᴅ :  {user_id}
╰⦿ᚐʙɪᴏ : {bio}
⦿ᚐᴄʜᴧᴛ : {group.title}
╰⦿ᚐᴄʜᴧᴛ ɪᴅ : {group.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
