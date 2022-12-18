import telebot
import requests
bot = telebot.TeleBot('5833844958:AAHd_AH1y73558v5MUO8QzYQwcbcly2T4DA')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, я бот который может сделать из черно-белой фотографии цветную. Просто отправь мне фото!'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('/path/to/your/file.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'})
    print(r.json())


bot.polling(none_stop=True)

