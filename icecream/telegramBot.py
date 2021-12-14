#!/usr/bin/env python3.8
import os
import json
import random as rd
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tokenmenu import token_menu

load_dotenv()

# Bot
tm = token_menu()


def start(bot, update):
    tm.reset()
    tm.restart()
    bot.message.reply_text(main_menu_message(),
                           reply_markup=main_menu_keyboard())


def main_menu(bot, update):
    bot.callback_query.message.edit_text(main_menu_message(),
                                         reply_markup=main_menu_keyboard())


def select_word(bot, update):
    id = int(bot.callback_query.data[1])
    tm.select_word(id)
    bot.callback_query.message.edit_text(main_menu_message(),
                                         reply_markup=main_menu_keyboard())


def more_words(bot, update):
    tm.more_words()
    bot.callback_query.message.edit_text(main_menu_message(),
                                         reply_markup=main_menu_keyboard())


def restart_menu(bot, update):
    tm.restart()
    bot.callback_query.message.edit_text(main_menu_message(),
                                         reply_markup=main_menu_keyboard())


def select_sentence(bot, update):
    tm.execute_sentence()
    selected = tm.select_sentence()
    # bot.callback_query.chat.send_message(selected)
    tm.restart()
    # bot.callback_query.chat.send_message(main_menu_message(),
    #                          reply_markup=main_menu_keyboard())
    bot.callback_query.message.edit_text(main_menu_message(),
                                         reply_markup=main_menu_keyboard())


def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Keyboards
def main_menu_keyboard():
    selected = tm.select_sentence()
    keyboard = [[InlineKeyboardButton(selected, callback_data='s1')],
                # [InlineKeyboardButton('Sentence 2', callback_data='s2')],
                [
                    InlineKeyboardButton(tm.word_list[0].replace("_", " "), callback_data='w0'),
                    InlineKeyboardButton(tm.word_list[1].replace("_", " "), callback_data='w1')
                ],
                [
                    InlineKeyboardButton(tm.word_list[2].replace("_", " "), callback_data='w2'),
                    InlineKeyboardButton(tm.word_list[3].replace("_", " "), callback_data='w3')
                ],
                [
                    InlineKeyboardButton(tm.word_list[4].replace("_", " "), callback_data='w4'),
                    InlineKeyboardButton(tm.word_list[5].replace("_", " "), callback_data='w5')
                ],
                [
                    InlineKeyboardButton('More ⏩', callback_data='more'),
                    InlineKeyboardButton('Restart 🔄', callback_data='restart')
                ]
                ]
    return InlineKeyboardMarkup(keyboard)


# Messages


def main_menu_message():
    # return 'Selected words: {}\nRemoved words:  {}\nQ: {}'.format(tm.selected_words, tm.removed_words, tm.seller_question)
    return '{}{}'.format(tm.seller_question[:1].upper(), tm.seller_question[1:])


# Handlers
updater = Updater(os.environ.get('TELEGRAM_TOKEN'), use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='token_menu'))
updater.dispatcher.add_handler(CallbackQueryHandler(select_word, pattern='^w'))
updater.dispatcher.add_handler(CallbackQueryHandler(select_sentence, pattern='^s'))
updater.dispatcher.add_handler(CallbackQueryHandler(more_words, pattern='^more$'))
updater.dispatcher.add_handler(CallbackQueryHandler(restart_menu, pattern='^restart$'))
updater.dispatcher.add_error_handler(error)

updater.start_polling()
