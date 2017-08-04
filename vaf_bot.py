#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import ConfigParser
import telepot

import commands

def CheckReceivedMessage(message):
  chatID = GetChatID(message)
  givenCommand = GetGivenCommand(message)
  
  if StartsWithSlash(givenCommand):
    if givenCommand == '/subit':
      SendMessageWithStyles(chatID, commands.Subway())
    elif givenCommand == '/inside':
      SendMessageWithStyles(chatID, commands.Inside())
    elif givenCommand == '/matti':
      SendMessageWithStyles(chatID, commands.Matti())
    elif givenCommand == '/donald':
      SendMessageWithStyles(chatID, commands.Donald())
    elif givenCommand == '/help' or givenCommand == '/apua':
      SendMessageWithStyles(chatID, commands.Help())

def GetChatID(message):
  return message['chat']['id']

def GetGivenCommand(message):
  return message['text']

def StartsWithSlash(message):
  if(message[0] == '/'):
    return True
  else:
    return False

def SendMessageWithoutStyles(chatID, messageToBeSent):
  bot.sendMessage(chatID, messageToBeSent)

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
