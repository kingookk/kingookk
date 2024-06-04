from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["مطور السورس", "مبرمج السورس", "تيتو", "المطور", "مطور"])
)
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/9ccdf1b81efa30d2adb53.mp4",
        caption="• ხ᥆ƚ ძᥱ᥎ᥱᥣ᥆ρᥱᖇ 🇵🇸 \n ━━━━━━━━━━━━ \n• Dev ↦  [₍ ƚ ᥱ ƚ ᥆ || تـيـ ٖ ـتـو ⁾ ↺](https://t.me/topteto) .\n• Bio ↦ أستغفر الله الذي لا إله إلا هو الحي القيوم، وأتوب إليه @T_S_T4.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ძᥱ᥎ᥣ᥆ρᥱᖇ 🇵🇸", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝗖𝗛 🇵🇸", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
