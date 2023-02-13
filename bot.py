from threading import Thread

import telebot
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from scraper import fetch_data


from config import TELEGRAM_BOT_TOKEN

from commands import bot_commands
from messages import bot_messages

# instanciate telegram tg_bot
bot = telebot.TeleBot(token=TELEGRAM_BOT_TOKEN)

# set bot commands
bot.set_my_commands(commands=bot_commands)

@bot.message_handler(commands=['start', 'iniciar'])
def send_welcome_message(message):
    bot.reply_to(message, text=bot_messages['welcome'])


@bot.message_handler(commands=['precios', 'prices'])
def send_dollar_prices(message):

    monitors = fetch_data()

    txt = ''

    for monitor in monitors:
        txt += f"<b>{monitor['name']}</b>: {monitor['price']}\n{monitor['last_update']}\n\n"

    cid = message.chat.id

    bot.send_message(chat_id=cid, text=txt, parse_mode='html')


@bot.message_handler(commands=['precio', 'price'])
def show_available_monitors(message):
    markup = InlineKeyboardMarkup(row_width=2)

    monitors = fetch_data()
    buttons = []

    for monitor in monitors:
        monitor_button = InlineKeyboardButton(
            text=monitor['name'], callback_data=monitor['name'])
        buttons.append(monitor_button)

    markup.add(*buttons)

    cid = message.chat.id
    bot.send_message(
        chat_id=cid, text='<b>Monitores disponibles</b>:', reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda x: True)
def show_selected_monitor_data(call):
    cid = call.from_user.id

    monitors = fetch_data()

    for monitor in monitors:
        if call.data == monitor['name']:
            text = ''
            text += f"{monitor['name']}: {monitor['price']}"
            bot.send_message(cid, text, parse_mode='html')


@bot.message_handler(commands=['ayuda', 'help'])
def send_help_text(message):
    bot.reply_to(message, text=bot_messages['help'], parse_mode="html")


@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    cid = message.chat.id
    bot.send_message(
        chat_id=cid, text=bot_messages['unknown_command'], parse_mode='html')


def receive_messages():
    bot.infinity_polling()


def run_bot():        
    print('Starting the bot....')
    bot_thread = Thread(target=receive_messages)
    print('Bot is running.')
    bot_thread.start()
