import telebot
import random
from telebot import types

# list of facts
f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# list of funny/useless facts
f = open('joke_facts.txt', 'r', encoding='UTF-8')
j_facts = f.read().split('\n')
f.close()
# list of sayings
f = open('proverb.txt', 'r', encoding='UTF-8')
proverb = f.read().split('\n')
f.close()
# create bot with hash code from BotFather
bot = telebot.TeleBot('5239303003:AAGw2UTfLcwAZQ1vcvTcuIrgFgZRLm70XnI')


# start Bot
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Create buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Факт")
    button2 = types.KeyboardButton("Бесполезный факт")
    button3 = types.KeyboardButton("Поговорка")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(m.chat.id,
                     'Нажми: \nФакт — для получения интересного факта\nБесполезный факт — для получения смешного'
                     ' или бесполезного факта\nПоговорка — для получения народной мудрости', reply_markup=markup)


# Receiving messages from User
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global answer
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Бесполезный факт':
        answer = random.choice(j_facts)
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(proverb)
    # Send a message to the chat
    bot.send_message(message.chat.id, answer)


# launch bot
bot.polling(none_stop=True, interval=0)
