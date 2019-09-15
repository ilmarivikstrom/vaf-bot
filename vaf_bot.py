#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import telepot

import cmds
import utils
from repository import Repository


def check_received_message(new_message_data):
    message_text = utils.get_message_text(new_message_data)
    repo.insert(new_message_data)

    if utils.starts_with_slash(message_text):
        chat_id = utils.get_chat_id(new_message_data)

        if message_text == '/subit':
            send_message_with_styles(chat_id, cmds.subway())
        elif message_text == '/inside':
            send_message_with_styles(chat_id, cmds.inside())
        elif message_text == '/matti':
            send_message_with_styles(chat_id, cmds.matti())
        elif message_text == '/donald':
            send_message_with_styles(chat_id, cmds.donald())
        elif message_text == '/help' or message_text == '/apua':
            send_message_with_styles(chat_id, cmds.help())


def send_message_with_styles(chat_id, message_to_be_sent):
    bot.sendMessage(chat_id, message_to_be_sent, "Markdown")


def main():
    bot.message_loop(check_received_message)
    print("I am listening ...")
    while 1:
        time.sleep(10)


repo = Repository()
bot = telepot.Bot(utils.get_config_value_with_key('API_KEY'))
main()
