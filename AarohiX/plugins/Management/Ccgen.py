from SafoneAPI import SafoneAPI
from AarohiX import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
api = SafoneAPI()

@app.on_message(filters.command(["فيزا وهميه", "ccgen"], [".", "", "/"]))
async def gen_cc(client, message):
    if len(message.command) < 2:
        return await message.reply_text("من فضلك أعطني البن")

    try:
        await message.delete()
    except:
        pass

    aux = await message.reply_text("جاري توليد البطاقه...")
    bin = message.text.split(None, 1)[1]

    if len(bin) < 6:
        return await aux.edit("البن خطأ")

    try:
        resp = await api.ccgen(bin, 10)
        cards = resp.liveCC

        regenerate_button = InlineKeyboardButton(
            "√ʀᴇɢᴇɴᴇʀᴀᴛᴇ¹", callback_data=f"regenerate_{bin}"
        )
        keyboard = InlineKeyboardMarkup([[regenerate_button]])

        await aux.edit(
            f"""
هـذه بعض البطاقات الائتمانيه ✅

╭✠╼━━━━━━❖━━━━━━━✠╮ 

{cards[0]}\n{cards[1]}\n{cards[2]}
{cards[3]}\n{cards[4]}\n{cards[5]}
{cards[6]}\n{cards[7]}\n{cards[8]}
{cards[9]}\n
╰✠╼━━━━━━❖━━━━━━━✠╯

⦿ البن: `{resp.results[0].bin}`
⦿ وقت الاستخراج: {resp.took}\n\n @WX_PM""",
            reply_markup=keyboard,
        )

    except Exception as e:
        return await aux.edit(f"خطأ: {e}.")

@app.on_callback_query(filters.regex(r"regenerate_"))
async def regenerate_cc(client, callback_query):
    bin_to_regenerate = callback_query.data.split("_")[1]

    try:
        resp = await api.ccgen(bin_to_regenerate, 10)
        cards = resp.liveCC

        await callback_query.edit_message_text(
            f"""
هـذه بعض البطاقات الائتمانيه ✅

╭✠╼━━━━━━❖━━━━━━━✠╮ 

{cards[0]}\n{cards[1]}\n{cards[2]}
{cards[3]}\n{cards[4]}\n{cards[5]}
{cards[6]}\n{cards[7]}\n{cards[8]}
{cards[9]}\n
╰✠╼━━━━━━❖━━━━━━━✠╯

⦿ البن: `{resp.results[0].bin}`
⦿ وقت الاستخراج: {resp.took}\n\n @WX_PM""",
        )

    except Exception as e:
        await callback_query.edit_message_text(f"Error: {e}.")
