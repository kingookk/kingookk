import os
import future
import asyncio
import requests
import wget
import time
import yt_dlp
from urllib.parse import urlparse
from AarohiX import app
from pyrogram import Client, filters
from pyrogram.types import Message


# ------------------------------------------------------------------------------- #


                     #   INSTAGRAM REELS LELO SAB  #
        

# ------------------------------------------------------------------------------- #


@app.on_message(filters.command(["انستا"], ["/", "!", "."]))
async def download_instareels(c: app, m: Message):
    try:
        reel_ = m.command[1]
    except IndexError:
        await m.reply_text("أعطني رابطا لتحميل المقطع...")
        return
    if not reel_.startswith("https://www.instagram.com/reel/"):
        await m.reply_text("من أجل الحصول على النتائج الصحيحه ، من الضروري وجود رابط صالح. يرجى تزويدي بالرابط المطلوب.")
        return
    OwO = reel_.split(".",1)
    Reel_ = ".dd".join(OwO)
    try:
        await m.reply_video(Reel_)
        return
    except Exception:
        try:
            await m.reply_photo(Reel_)
            return
        except Exception:
            try:
                await m.reply_document(Reel_)
                return
            except Exception:
                await m.reply_text("أنا غير قادر على الوصول إلى هذه النتيجه.")


@app.on_message(filters.command(["تحميل استوري"], ["/", "!", "."]))
async def instagram_reel(client, message):
    if len(message.command) == 2:
        url = message.command[1]
        response = requests.post(f"https://lexica-api.vercel.app/download/instagram?url={url}")
        data = response.json()

        if data['code'] == 2:
            media_urls = data['content']['mediaUrls']
            if media_urls:
                video_url = media_urls[0]['url']
                await message.reply_video(f"{video_url}")
            else:
                await message.reply("لم يتم العثور على فيديو في الرد. قد يكون الحساب خاصا.")
        else:
            await message.reply("لم يكن الطلب ناجحا.")
    else:
        await message.reply("يرجى تقديم عنوان URL صالح لـ Instagram باستخدام الأمر تحميل استوري..")
