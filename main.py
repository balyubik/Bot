import telebot
import requests
from bs4 import BeautifulSoup as b
import random

bot = telebot.TeleBot('5552649818:AAG9L-J47e35-318I3m3OXJ8HNC_q1xHUis')
url = 'https://boomkids.by/new'
r = requests.get(url)
soup = b(r.text, 'html.parser')
things = soup.find_all('div', class_="card m-0 border-0 rounded product app-card justify-content-between slide pb-2")
print(things)
for n, i in enumerate(things, start=1):
    thingsName = i.find('div', class_='card-body px-2 py-0 text-center').text.strip()
    thingsPrice = i.find('div', class_='d-flex flex-row justify-content-around flex-wrap pb-1' ).text
    thingsPhoto = i.find('a', class_='app-card-img-wrapper link-product no-hover')
    new_things = (f'{n}:  {thingsPhoto} + {thingsPrice} за {thingsName}')
    print(new_things)
clear_things = [i.text for i in things]
#print(clear_things)
@bot.message_handler(commands=['start'])
def start(message):
    site = 'https://boomkids.by/new'
    name = f'Привет, <b>{message.from_user.first_name}</b>. Я бот, который поможет тебе найти новинки в <b><a href=site>Каталоге товаров BoomKids</a></b>. Чтобы посмотреть, что у нас есть, напиши слово - новинка: '
    bot.send_message(message.chat.id, name, parse_mode='html', disable_web_page_preview=False)

@bot.message_handler()
def get_things(message):
    if message.text == 'Новинка' or 'новинка':
        bot.send_message(message.chat.id, random.choice(clear_things))
    else:
        bot.send_message(message.chat.id, 'Введите слово - новинка:')

bot.polling(none_stop=True)