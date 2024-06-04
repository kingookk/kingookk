import asyncio
import random
from AarohiX.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from AarohiX import app
from config import *

bot_name = {}
botname = {}

name = "رودينا"

@app.on_message(filters.command(["تعيين اسم البوت"])& filters.private & SUDOERS, group=39)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id,"ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

ahmedteto_responses = [
    "اسمي {name} يصحبي",
    "يسطا قولتلك اسمي {name} الاه",
    "يا أجمل من نطق اسمي على لسانه ♡",
    "وش رايك فاللي يناديني بوت ؟ 🦦",
    "اؤمر سهيله شتريد؟❤️🥺",
    "يعم والله بحبك بس ناديلي ب {name}",
    "تعرف بالله هحبك أكتر لو ناديتلي {name}",
    "اي ي معلم مين مزعلك",
    "متصلي على النبي كدا",
    "مش فاضيلك نصايح وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج على أخوك",
    "ثانيه واحده بتشقط وجى🙄",
    "شكلها منكدا عليك وجاي تطلعهم علينا",
    "ها شتبي مليون مره اسمي {name}",
]

@app.on_message(filters.command(["بوت", "البوت","افاتار"], ""), group=39)
async def ahmedteto_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(ahmedteto_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("ضـيف الـبوت لمجموعتـك🎄", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])

    await message.reply_text(
       text=f"[{bar}](https://t.me/{bot_username}?startgroup=True)",
       disable_web_page_preview=True,
        reply_markup=keyboard
)
