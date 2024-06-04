from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import  BOT_USERNAME
from AarohiX import app
import requests

@app.on_message(filters.command("اكتبلي",""))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "انتظر من فضلك...,\n\nجاري كتابة النص الخاص بك...")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
✨ بواسطـه : [˹ᴍᴜꜱɪᴄ ✘ ᴛᴇᴛᴏ˼ 🫧](https://t.me/{BOT_USERNAME})
🥀 لــ : {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)

mod_name = "اكتبلي"

help = """

 اعطيني شئ لاكي اكتبه علي ورقه

- مثال اكتبلي + اسمك
 """
