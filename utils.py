#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import feedparser
import random
import urllib2

version = "0.4"

def GetRandomLineOfFile(file):
  lines = open(file, 'r').read().splitlines()
  return random.choice(lines)

def GetRobotEmoji():
  return "\xF0\x9F\xA4\x96"

def GetVersion():
  return version

def ParseQuote(line, name=None):
  if(name==None):
    parts = line.split(';');
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

