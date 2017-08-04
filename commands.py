#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time
import datetime
import json
import urllib2

version = "0.3.1"

def Clock():
  return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def Subway():
  currentDay = datetime.datetime.today().weekday()
  subsOfTheDay = ["Ma: Kana Fajita", "Ti: Tonnikala", "Ke: Kananrinta",
                  "To: Italian B.M.T. eli se paras", "Pe: Vegepihvi",
                  "La: American Steakhouse Melt", "Su: Kinkku"]
  subwayMessage = ""
  for day in range(0, len(subsOfTheDay)):
    if day == currentDay:
      subwayMessage += "*"+ subsOfTheDay[day] + "*"
    else:
      subwayMessage += subsOfTheDay[day]
    subwayMessage += "\n"
  return subwayMessage

def Inside():
  line = GetRandomLineOfFile('res/inside.txt')
  quote = ParseQuote(line)
  return quote

def Matti():
  line = GetRandomLineOfFile('res/matti.txt')
  quote = ParseQuote(line, "Profeetta Nykänen")
  return quote

def Donald():
  line = ReadUrlAndGetContents("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
  quote = ParseQuote(line, "Donald Trump")
  return quote

def Help():
  return (GetRobotEmoji() +
         " *Väf-bot versio " + version + "*" + GetRobotEmoji() +
         "\n\n*Komennot:*\n/subit\tSubilista"
         "\n/inside\tInsideläppä\n"
         "/matti\tOppia profeetalta\n"
         "/donald\tDon't stump the Trump")

def ReadUrlAndGetContents(url):
  response = urllib2.urlopen(url)
  data = response.read()
  values = json.loads(data)
  return values["message"]

def GetRandomLineOfFile(file):
  lines = open(file, 'r').read().splitlines()
  return random.choice(lines)

def ParseQuote(line, name=None):
  if(name==None):
    parts = line.split(';');
    return "_\"" + parts[0] + "\"_" + "  *-" + parts[1] + "*"
  else:
    return "_\"" + line + "\"_" + "  *-" + name + "*"

def GetRobotEmoji():
  return "\xF0\x9F\xA4\x96"
