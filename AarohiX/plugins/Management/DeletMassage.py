from AarohiX import app
from AarohiX.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from AarohiX.utils.admin_check import admin_filter


@app.on_message(filters.command(["حذف", "مسح"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def purge(app: app, msg: Message):
    
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**◍ لا يمكنني مسح الرسالة في مجموعة بدون رابط \n\n √**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        
        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
                
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**◍ اعطيني صلاحيه حذف الرسائل لاستطيع حذف الرساله \n\n √**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**◍ هناك خطأ ارسل نادي المطور \n\n √*")
        count_del_msg = len(message_ids)
        sumit = await msg.reply_text(text=f"◍ تم حذف هذه الرساله بنجاح \n\n √")
        await sleep(3)
        await sumit.delete()
        return
    await msg.reply_text("**◍ قم بعمل ريبلي علي الرساله للحذف \n\n √**")
    return





@app.on_message(filters.command("مسح") & admin_filter)
async def spurge(app: app, msg: Message):

    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**◍ لا يمكنني مسح الرسالة في مجموعة بدون رابط \n\n √**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**◍ لا يمكنني مسح الرسالة في مجموعة بدون رابط \n\n √**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**◍ هناك خطأ ارسل نادي المطور \n\n √")           
            return        
    await msg.reply_text("**◍ هناك خطأ ارسل نادي المطور \n\n √**")
    return


@app.on_message(filters.command(["مسح", "حذف"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def del_msg(app: app, msg: Message):
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**◍ لا يمكنني مسح الرسالة في مجموعة بدون رابط \n\n √**")
        return        
    if msg.reply_to_message:
        await msg.delete()
        await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.reply_to_message.id)
    else:
        await msg.reply_text(text="**◍ ماذا تريد ان تحذف**")
        return

