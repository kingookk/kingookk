import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(filters.new_chat_photo)
async def caesarphoto(client, message):
    chat_id = message.chat.id
    photo = await client.download_media(message.chat.photo.big_file_id)
    await client.send_photo(chat_id=chat_id, photo=photo, caption=f"↢ المستخدم  :{message.from_user.mention} \n قام بتغيـرر صوره المجمـوعه \n√")

@app.on_message(filters.command(["قفل الروابط","تعطيل الروابط"],""))
async def block_links(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in link_lock:
            return await message.reply_text(f"يا {message.from_user.mention} الروابط مقفلة من قبل")
        link_lock.append(message.chat.id)
        return await message.reply_text(f"تم قفل الروابط \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.command(["فتح الروابط","تغعيل الروابط"],""))
async def unblock_links(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in link_lock:
            return await message.reply_text(f"يا {message.from_user.mention} الروابط مفتوحة من قبل")
        link_lock.remove(message.chat.id)
        return await message.reply_text(f"تم فتح الروابط \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.text & filters.regex(r'https?://\S+'))
async def delete_links(client:Client, message:Message):
    if message.chat.id in link_lock:
        await message.delete()
