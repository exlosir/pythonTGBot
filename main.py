import telebot
import get_weather
from telebot import apihelper


Germany_proxy = 'socks5://login:pass@5.189.131.241:443'
proxy = 'socks5://login:pass@140.82.20.93:1080'
Ukraine_proxy = 'socks5://login:pass@80.252.241.107:1080'

bot = telebot.TeleBot("674981466:AAEp_Xcm0l0iRuSQtWfZr3EieLW3Sf-Yeb0")
apihelper.proxy = {'https': Ukraine_proxy}


@bot.message_handler(commands=['time'])
def send_message(message):
    from datetime import datetime
    bot.send_message(message.chat.id, "Время и дата на сервере - {0} {1}".format(datetime.now().date().strftime("%d.%m.%Y"), datetime.now().time().strftime("%H:%M")))


@bot.message_handler(commands=['start'])
def send_message(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_murkup.row('/start', '/weather', '/time')
    bot.send_message(message.chat.id, '... ', reply_markup=user_murkup)


@bot.message_handler(commands=['weather'])
def send_message(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_murkup.row('Уфа', 'Москва', 'Казань')
    user_murkup.row('Санкт-Петербург', 'Туймазы', 'Октябрьский')
    user_murkup.row('/stop')
    # get_weather.get_weather(get_weather.get_html('https://yandex.ru/pogoda/moscow/'))
    bot.send_message(message.chat.id, 'Выберите город... ',reply_markup=user_murkup)

@bot.message_handler(content_types=['text'])
def gw(message):
    cities = {
        'Уфа': 'ufa',
        'Октябрьский': 'oktyabrsky',
        'Туймазы': 'tuymazy',
        'Москва': 'moscow',
        'Казань': 'kazan',
        'Санкт-Петербург': 'saint-petersburg',
    }
    if message.text in cities:
        bot.send_message(message.chat.id, get_weather.get_weather(get_weather.get_html('https://yandex.ru/pogoda/{0}/'.format(cities[message.text]))))
        # print('https://yandex.ru/pogoda/{0}/'.format(cities[message.text]))

@bot.message_handler(commands=['stop'])
def back(message):
    hide_markup = telebot.types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "...",reply_markup=hide_markup)


bot.polling(none_stop=True, interval=0)

