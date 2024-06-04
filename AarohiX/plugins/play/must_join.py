from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app

@app.on_message(filters.incoming & filters.private, group=-2)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/creativee24":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("creativee24", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/creativee24".isalpha():
                link = "https://t.me/creativee24"
            else:
                chat_info = await bot.get_chat("creativee24")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"**- لطفاً اشترك بالقناة واستخدم البوت .\n- ثم اضغط /start \n- قناة البوت 👾👇🏻\n💎: https://t.me/creativee24**",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("‹ اطغط للانضمام ›", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @creativee24 !")
      
