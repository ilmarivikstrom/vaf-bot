#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time

import ConfigParser
import telepot

import cmds

def CheckReceivedMessage(newMessageData):
  messageText = GetMessageText(newMessageData)
  
  if StartsWithSlash(messageText):
    chatID = GetChatID(newMessageData)
    
    if messageText == '/subit':
      SendMessageWithStyles(chatID, cmds.Subway())
    elif messageText == '/inside':
      SendMessageWithStyles(chatID, cmds.Inside())
    elif messageText == '/matti':
      SendMessageWithStyles(chatID, cmds.Matti())
    elif messageText == '/donald':
      SendMessageWithStyles(chatID, cmds.Donald())
    elif messageText == '/kahvit':
      SendMessageWithStyles(chatID, cmds.Kahvit())
    elif messageText == '/help' or messageText == '/apua':
      SendMessageWithStyles(chatID, cmds.Help())

def GetChatID(newMessageData):
  return newMessageData['chat']['id']

def GetMessageText(newMessageData):
  return newMessageData['text']

def StartsWithSlash(newMessageData):
  if(newMessageData[0] == '/'):
    return True
  else:
    return False

def SendMessageWithStyles(chatID, messageToBeSent):
  bot.sendMessage(chatID, messageToBeSent, "Markdown")

def GetAPIKey():
  config = ConfigParser.ConfigParser()
  config.read("vaf_bot.ini")
  return config.get('Credentials', 'API_KEY')

def Main():
  bot.message_loop(CheckReceivedMessage)
  print("I am listening ...")
  while 1:
    time.sleep(10)

bot = telepot.Bot(GetAPIKey())
Main()
