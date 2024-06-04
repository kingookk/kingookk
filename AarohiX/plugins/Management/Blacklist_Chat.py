"""

COPY KARLO FUCKING BITCHES

"""
import re
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.types import ChatPermissions
from pyrogram.errors import ChatAdminRequired

from AarohiX.utils.Databases.blacklist_db import (
    delete_blacklist_filter,
    get_blacklisted_words,
    save_blacklist_filter,
)
from AarohiX import app
from AarohiX.utils.errors import capture_err
from AarohiX.utils.permission import adminsOnly, list_admins
from AarohiX.misc import SUDOERS as SUDO

__MODULE__ = "Blacklist"
__HELP__ = """
/blacklisted - Get All The Blacklisted Words In The Chat.
/blacklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
/whitelist [WORD|SENTENCE] - Whitelist A Word Or A Sentence.
"""


@app.on_message(filters.command("blacklist") & ~filters.private)
@adminsOnly("can_restrict_members")
async def save_filters(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/blacklist [WORD|SENTENCE]")
    word = message.text.split(None, 1)[1].strip()
    if not word:
        return await message.reply_text("**Usage**\n__/blacklist [WORD|SENTENCE]__")
    chat_id = message.chat.id
    await save_blacklist_filter(chat_id, word)
    await message.reply_text(f"__**Blacklisted {word}.**__")


@app.on_message(filters.command("blacklisted") & ~filters.private)
@capture_err
async def get_filterss(_, message):
    data = await get_blacklisted_words(message.chat.id)
    if not data:
        await message.reply_text("**No blacklisted words in this chat.**")
    else:
        msg = f"List of blacklisted words in {message.chat.title} :\n"
        for word in data:
            msg += f"**-** `{word}`\n"
        await message.reply_text(msg)


@app.on_message(filters.command("whitelist") & ~filters.private)
@adminsOnly("can_restrict_members")
async def del_filter(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/whitelist [WORD|SENTENCE]")
    word = message.text.split(None, 1)[1].strip()
    if not word:
        return await message.reply_text("Usage:\n/whitelist [WORD|SENTENCE]")
    chat_id = message.chat.id
    deleted = await delete_blacklist_filter(chat_id, word)
    if deleted:
        return await message.reply_text(f"**Whitelisted {word}.**")
    await message.reply_text("**No such blacklist filter.**")


# ... (previous code)

@app.on_message(filters.text & ~filters.private, group=8)
@capture_err
async def blacklist_filters_re(client, message):  # Added 'client' argument
    text = message.text.lower().strip()
    if not text:
        return
    chat_id = message.chat.id
    user = message.from_user
    if not user:
        return
    if user.id in SUDO:
        return
    list_of_filters = await get_blacklisted_words(chat_id)
    
    # Pass 'client' to list_admins function
    if user.id in await list_admins(chat_id, client=client):
        return
    
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            try:
                await message.delete()
                await message.chat.restrict_member(
                    user.id,
                    ChatPermissions(all_perms=False),
                    until_date=datetime.now() + timedelta(hours=1),
                )
            except ChatAdminRequired:
                return await message.reply("Please give me admin permissions to blacklist user", quote=False)
            except Exception as err:
                print(f"ERROR Blacklist Chat: ID = {chat_id}, ERR = {err}")
                return
            await app.send_message(
                chat_id,
                f"Muted {user.mention} [`{user.id}`] for 1 hour "
                + f"due to a blacklist match on {word}.",
            )


"""
Copyright (c) 2024 @dil_sagar_121
Copyright (c) 2024 @Alone_Dil_bot
"""
