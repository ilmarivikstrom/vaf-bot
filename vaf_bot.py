#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import telepot

import cmds
import utils
from repository import Repository

def CheckReceivedMessage(newMessageData):
  messageText = utils.GetMessageText(newMessageData)
  repo.insert(newMessageData)

  if utils.StartsWithSlash(messageText):
    chatID = utils.GetChatID(newMessageData)
    
    if messageText == '/subit':
      SendMessageWithStyles(chatID, cmds.Subway())
    elif messageText == '/inside':
      SendMessageWithStyles(chatID, cmds.Inside())
    elif messageText == '/matti':
      SendMessageWithStyles(chatID, cmds.Matti())
    elif messageText == '/donald':
      SendMessageWithStyles(chatID, cmds.Donald())
    elif messageText == '/help' or messageText == '/apua':
      SendMessageWithStyles(chatID, cmds.Help())


def SendMessageWithStyles(chatID, messageToBeSent):
  bot.sendMessage(chatID, messageToBeSent, "Markdown")

def Main():
  bot.message_loop(CheckReceivedMessage)
  print("I am listening ...")
  while 1:
    time.sleep(10)

repo = Repository()
bot = telepot.Bot(utils.GetConfigValueWithKey('API_KEY'))
Main()
