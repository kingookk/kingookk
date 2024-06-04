from pyrogram import filters, Client
from AarohiX import app
import asyncio
import config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AarohiX.core.call import Dil
from AarohiX.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)


@app.on_message(filters.regex("^مين في الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Dil, message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("https://telegra.ph/file/75764a04cd59c09fe4d3f.mp4"), stream_type=StreamType().pulse_stream)
        text = "↢ الموجودين في الكول 🙄:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut = "↢ موجود فالكول بس فاتح مايك 😒"
            else:
                mut = "↢ موجود بس قافل المايك 🥲😂"
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} - {user.mention} {mut}\n"
        text += f"\n- عددهم : {len(participants)}\n️"  

        # إضافة زر شفاف في الأسفل
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴍᴜꜱɪᴄ ᴜᴘᴅᴀᴛᴇᴅ", url=config.SUPPORT_CHAT)],
        ])      

        await message.reply(f"{text}", reply_markup=inline_keyboard)
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"↢ لازم يكون حد بالكول او مشغلين اغاني")
    except TelegramServerError:
        await message.reply(f"↢ حدث خطأ.")
    except AlreadyJoinedError:
        text = "↢ الي بالكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut = "- موجود بيتنصت عليكم "
            else:
                mut = "- قافل المايك "
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} - {user.mention} {mut}\n"
        text += f"\n- عددهم : {len(participants)}\n️"

        # إضافة زر شفاف في الأسفل
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴍᴜꜱɪᴄ ᴜᴘᴅᴀᴛᴇᴅ", url=config.SUPPORT_CHAT)],
        ])
        await message.reply(f"{text}", reply_markup=inline_keyboard)
