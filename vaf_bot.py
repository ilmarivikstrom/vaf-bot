#!/usr/bin/python

# -*- coding: utf-8 -*-

import json
import os
import time

import telepot

import cmds
import utils
from repository import Repository


def check_received_message(new_message_data):
    print(json.dumps(new_message_data, indent=4, sort_keys=True))
    message_text = utils.get_message_text(new_message_data)
    repo.insert(new_message_data)

    chat_id = utils.get_chat_id(new_message_data)

    if utils.starts_with(message_text, "/banter"):
        send_audio(chat_id, message_text)

    if utils.starts_with(message_text, "/"):


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


def send_audio(chat_id, message_text):
    reduced_message_text = message_text[len("/banter "):len(message_text)]
    espeak_cmd = "espeak \"" + reduced_message_text + "\" -v fi -w res/wavi.wav"
    os.system(espeak_cmd)

    bot.sendAudio(chat_id, open('res/wavi.wav', 'rb'), title=reduced_message_text)


def main():
    bot.message_loop(check_received_message)
    print("I am listening ...")
    while 1:
        time.sleep(10)


repo = Repository()
bot = telepot.Bot(utils.get_config_value_with_key('API_KEY'))
main()
