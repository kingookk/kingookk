from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config
from pyrogram.errors import FloodWait




@app.on_message(filters.command(["بوت حذف","رابط الحذف","حذف حساب","عاوز احذف"], ""))
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://telegra.ph/file/7a7e4909d7f78e8d4c685.mp4",
        caption="↢ مع السـلامه غور في داهيه 🤓😹 ❲ [اطغط هنا](https://t.me/LC6BOT) ❳",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["عاوزاتاا انصب","عاوزه اناااصب"], ""))
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://telegra.ph/file/5ec57dbb999310e0470d7.mp4",
        caption="◍ للتنصيب تواصـل مع تيتو ❲ [اطغط هنا](https://t.me/ToPTeto) ❳ \n\n√",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
     )
     
