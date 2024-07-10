from telebot.types import InlineKeyboardMarkup
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove



def help_reply_keyboard(help_btn: str):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(help_btn))
    return keyboard


def empty_inline():
    return InlineKeyboardMarkup()


def empty_reply():
    return ReplyKeyboardMarkup()


def remove_reply():
    return ReplyKeyboardRemove()


# TODO: write your keyboards here
