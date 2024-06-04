import requests
from pyrogram import Client
from pyrogram import filters
from AarohiX import app

random_user_api_url = 'https://randomuser.me/api/'

@app.on_message(filters.command("توليد عناوين", prefixes=""))
def generate_fake_user_by_country(client, message):
    country_name = message.text.split("/fake ", maxsplit=1)[1]
    
    response = requests.get(f'{random_user_api_url}?nat={country_name}')
    
    if response.status_code == 200:
        user_info = response.json()['results'][0]
        first_name = user_info['name']['first']
        last_name = user_info['name']['last']
        email = user_info['email']
        country = user_info['location']['country']
        state = user_info['location']['state']
        city = user_info['location']['city']
        street = user_info['location']['street']['name']
        zip_code = user_info['location']['postcode']
        message.reply_text(f"**↢ الاسم :** {first_name} {last_name}\n\n**↢ الدولة :** {country}\n\n**↢ الولاية :** {state}\n\n**↢ المدينة :** {city}\n\n**↢ العنوان :** {street}\n\n**↢ الرمز البريدي :** {zip_code}")
    else:
        message.reply_text(f"↢ فشل في إنشاء معلومات مستخدم مزيفة لـ  {country_name}.")
        
