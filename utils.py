#!/usr/bin/python
# -*- coding: utf-8 -*-


import ConfigParser
import feedparser
import json
import random
import urllib2

version = "0.5"

def GetRandomLineOfFile(file):
  lines = open(file, 'r').read().splitlines()
  return random.choice(lines)

def GetRobotEmoji():
  return "\xF0\x9F\xA4\x96"

def GetVersion():
  return version

def ParseQuote(line, name=None):
  if(name==None):
    parts = line.split(';')
    return "_\"" + parts[0] + "\"_" + "  *-" + parts[1] + "*"
  else:
    return "_\"" + line + "\"_" + "  *-" + name + "*"

def ReadURLAndGetContents(url):
  response = urllib2.urlopen(url)
  data = response.read()
  values = json.loads(data)
  return values["message"]

def URLToRSSFeed(url):
  return feedparser.parse(url)


def GetChatID(newMessageData):
  return newMessageData['chat']['id']

def GetMessageText(newMessageData):
  return newMessageData['text']

def GetMessageValues(newMessageData):
  values = "("
  values += "\""
  values += newMessageData['chat']['first_name']
  values += "\""
  values += ", "
  values += "\""
  values += str(newMessageData['chat']['id'])
  values += "\""
  values += ", "
  values += "\""
  values += newMessageData['chat']['type']
  values += "\""
  values += ", "
  values += "\""
  values += newMessageData['chat']['username']
  values += "\""
  values += ", "
  values += "\""
  values += str(newMessageData['date'])
  values += "\""
  values += ", "
  values += "\""
  values += newMessageData['from']['first_name']
  values += "\""
  values += ", "
  values += "\""
  values += str(newMessageData['from']['id'])
  values += "\""
  values += ", "
  values += "\""
  values += str(newMessageData['from']['is_bot'])
  values += "\""
  values += ", "
  values += "\""
  values += newMessageData['from']['language_code']
  values += "\""
  values += ", "
  values += "\""
  values += newMessageData['from']['username']
  values += "\""
  values += ", "
  values += "\""
  values += str(newMessageData['message_id'])
  values += "\""
  values += ", "
  values += "\""
  values += newMessageData['text']
  values += "\""
  values += ")"
  return values

def StartsWithSlash(newMessageData):
  if(newMessageData[0] == '/'):
    return True
  else:
    return False

def GetAPIKey():
  config = ConfigParser.ConfigParser()
  config.read("vaf_bot.ini")
  return config.get('Credentials', 'API_KEY')
