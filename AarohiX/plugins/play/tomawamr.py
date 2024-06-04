from pyrogram.types import CallbackQuery
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto


@app.on_message(
    filters.command("الاوامر", "")
)
async def cr_source(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/dcfb16b43f82c3a82c2aa.mp4",
        caption=f"""**↢ اهلا يا {message.from_user.mention} في قائمه الاوامر اختار ما تريد من الاسفل 👇
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𝗦𝗼𝘂𝗥𝗰𝗲", url=f"https://t.me/source_av"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def crusage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**اهلا بك في قائمه الاوامر**
╮⦿ اهلا هذه قائمه اوامر المجموعات
│᚜⦿ كتم او الغاء كتم
│᚜⦿ المكتومين
│᚜⦿ منع تصفيه (قم برفع الادمنيه من بوت ) 
│᚜⦿ رابط الدعوه
╯⦿ نادي المطور

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="ch"), 
                    
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**اهلا بك في قائمه الاوامر**
╮⦿ اهلا هذه قائمه اوامر القنوات
│᚜⦿ تشغيل + اسم الاغنيه
│᚜⦿ فيديو + اسم الاغنيه (معطل مؤقتا)
╯⦿ جاري تحديث قائمه الاونلين
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="adm"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def c_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**اهلا بك في قائمه الاوامر**
╮⦿ اهلا هذه قائمه مميزات البوت
│᚜⦿ تفعيل الاذان
│᚜⦿ اسكرين + رابط الموقع
│᚜⦿ مين في الكول
│᚜⦿ مهنتي
│᚜⦿ قول
│᚜⦿ اوقات الصلاه 
│᚜⦿ كت كويت - احرف - حكمه
│᚜⦿ اسمي
│᚜⦿ منع الكلام السئ (الميزه تتفعل تلقائي)
│᚜⦿ تحويل الملصق (لتحويل الملصق الي صوره)
│᚜⦿ رابط الحذف 
│᚜⦿ الساعه كام 
│᚜⦿ نسبه الرجوله
│᚜⦿ نكته - لو خيروك
│᚜⦿ زخرفه
│᚜⦿ الطقس
│᚜⦿ تفعيل الاذكار
│᚜⦿ رفع وتنزيل (عره - رقاصه - عره)
╯⦿ لعبه البنك
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="gr"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://telegra.ph/file/dcfb16b43f82c3a82c2aa.mp4",
        caption=f"""**↢ اهلا يا {message.from_user.mention} في قائمه الاوامر اختار ما تريد من الاسفل 👇**""",),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𝗦𝗼𝘂𝗥𝗰𝗲", url=f"https://t.me/source _av"),
                ],

            ]

        ),

    )
