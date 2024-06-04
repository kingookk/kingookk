from pyrogram import Client, filters
from AarohiX import app

@app.on_message(filters.command("الطقس",""))
def weather(client, message):
    try:
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        message.reply_photo(photo=weather_url, caption="إليك الطقس لموقعك")
    except IndexError:
        message.reply_text("يرجى استخدام الامر مثل الطقس نيو يورك")
