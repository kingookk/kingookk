import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**صلي علي اشرف الخلق محمد ﷺ**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("حكمه"),
        ("اغاني")
    ],
    
    [
        ("اقتباس"),
        ("شعر")
    ],
    [
        ("صور")
    ],
   
    [
        ("لو خيروك"),
        ("هيدرات")
    ],
    [
        ("يوت")
    ],
    [
        ("صور شباب"),
        ("صور بنات")
    ],
    [
        ("اذكار")
    ],
    [
        ("غنيلي"),
        ("تلاوات")
    ],
    [
        ("الشيخ نقشبندي"),
        ("متحركه")
        
    ],
    [
        ("لو خيروك"),
        ("احساب العمر")
    ],    
 [
        
             ("اضـف البـوت لمجموعـتك ✅")
        
    ],    
  
]

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اضـف البـوت لمجموعـتك ✅") & filters.group)
async def down(client, message):
          m = await message.reply("**- بخدمتك حجي خفيت الازرار\n- اذا تريد تطلعها مرة ثانية اكتب الاوامر**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("اضـف البـوت لمجموعـتك ✅"))
def reply_to_HEY(Client, message):
    message.reply_video(
        video=f"https://telegra.ph/file/dcfb16b43f82c3a82c2aa.mp4",
        caption=f"""↞ شكرا الاضافتي الي مجموعتك سوف اعمل بدون توقف \n↞ استمتع بمميزات لاحصر لها \n- فقط قم باضافتي من هنا ❄️👇""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ضيف البوت لمجموعتـك🎄", url=f"https://t.me/{app.username}?startgroup=true"),
            ]
         ]
     )
  )

#write by teto @G_7_Rr
