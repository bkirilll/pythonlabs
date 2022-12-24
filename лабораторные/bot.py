import telebot
import requests
import shutil
bot = telebot.TeleBot('5833844958:AAHd_AH1y73558v5MUO8QzYQwcbcly2T4DA')
url = "https://api.deepai.org/api/colorizer"
headers = {'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, я бот который может сделать из черно-белой фотографии цветную. Просто отправь мне фото!'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    data={
            'photo': message.text,
        }
    
    response_url = requests.post(url, data, headers=headers).json()["output_url"]
    img = requests.get(response_url,  stream=True)

    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(img.raw, out_file)
        
    photo = open('img.png', 'rb')
    bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True)

