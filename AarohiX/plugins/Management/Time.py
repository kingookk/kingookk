from pyrogram import Client, filters
from datetime import datetime
import pytz
from AarohiX import app


def get_current_time():
    tz = pytz.timezone('Africa/Cairo')  # Setting the timezone to Egypt (Cairo)
    current_time = datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

@app.on_message(filters.command("الساعه كام",prefixes=""))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"الوقت الحالي في القاهره: {time}")
