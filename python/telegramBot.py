#!/usr/bin/env python3.8
import os
import json
import random as rd
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

load_dotenv()


class token_menu:
    def __init__(self):
        with open("words.json", 'r') as fp:
            self.words = json.load(fp)
        with open("sentences.json", 'r') as fp:
            self.sentences = json.load(fp)
        self.restart()

    def restart(self):
        self.word_list = []
        self.selected_words = []
        self.removed_words = []
        self.sentence = rd.sample(self.sentences, 1)[0]
        self.word_list = self.choose_words()

    def choose_words(self, n=6):
        return rd.sample(self.words, n)

    def sample(self):
        tries = 0
        new_word = rd.choice(self.words)
        while new_word in self.selected_words or new_word in self.removed_words or new_word in self.word_list:
            new_word = rd.choice(self.words)
            tries += 1
            if tries > 500:
                raise Exception("Can't find a new word")
        return new_word

    def select_sentence(self):
        if len(self.selected_words) == 0:
            return rd.choice(self.sentences)
        else:
            max_weight = 0
            current_sentence = self.sentences[0]
            for s in self.sentences:
                weight = 0
                for w in self.selected_words:
                    if w in s[1]:
                        weight += 1
                for w in self.removed_words:
                    if w in s[1]:
                        weight -= .5
                if weight > max_weight:
                    max_weight = weight
                    self.current_sentence = s
            return self.current_sentence

    def select_word(self, id):
        word = self.word_list[id]
        self.word_list[id] = self.sample()
        self.selected_words.append(word)

    def more_words(self):
        self.removed_words += self.word_list
        for n in range(len(self.word_list)):
            self.word_list[n] = self.sample()


# Bot
tm = token_menu()


def start(bot, update):
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
    selected = tm.select_sentence()
    bot.callback_query.chat.send_message(selected[0])
    tm.restart()
    bot.callback_query.chat.send_message(main_menu_message(),
                             reply_markup=main_menu_keyboard())


def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Keyboards
def main_menu_keyboard():
    selected = tm.select_sentence()
    keyboard = [[InlineKeyboardButton(selected[0], callback_data='s1')],
                # [InlineKeyboardButton('Sentence 2', callback_data='s2')],
                [
                    InlineKeyboardButton(tm.word_list[0], callback_data='w0'),
                    InlineKeyboardButton(tm.word_list[1], callback_data='w1')
                ],
                [
                    InlineKeyboardButton(tm.word_list[2], callback_data='w2'),
                    InlineKeyboardButton(tm.word_list[3], callback_data='w3')
                ],
                [
                    InlineKeyboardButton(tm.word_list[4], callback_data='w4'),
                    InlineKeyboardButton(tm.word_list[5], callback_data='w5')
                ],
                [
                    InlineKeyboardButton('More ⏩', callback_data='more'),
                    InlineKeyboardButton('Restart 🔄', callback_data='restart')
                ]
                ]
    return InlineKeyboardMarkup(keyboard)


# Messages


def main_menu_message():
    return 'Selected words: {}\nRemoved words:  {}\nTarget sentence: {}'.format(tm.selected_words, tm.removed_words, tm.sentence[0])


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
