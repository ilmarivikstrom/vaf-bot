#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

import utils

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
  line = utils.GetRandomLineOfFile('res/inside.txt')
  quote = utils.ParseQuote(line)
  return quote

def Matti():
  line = utils.GetRandomLineOfFile('res/matti.txt')
  quote = utils.ParseQuote(line, "Profeetta Nykänen")
  return quote

def Donald():
  line = utils.ReadURLAndGetContents("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
  quote = utils.ParseQuote(line, "Donald Trump")
  return quote

def Help():
  return (utils.GetRobotEmoji() +
         " *Väf-bot versio " + utils.GetVersion() + "* " + utils.GetRobotEmoji() +
         "\n\n*Komennot:*\n/subit\tSubilista\n"
         "/inside\tInsideläppä\n"
         "/matti\tOppia profeetalta\n"
         "/donald\tDon't stump the Trump\n\n"
         "GitHub repo\thttps://git.io/v7VKt")