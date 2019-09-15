#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

import utils


def subway():
    current_day = datetime.datetime.today().weekday()
    subs_of_the_day = ["Ma: Kana Fajita", "Ti: Tonnikala", "Ke: Kananrinta",
                       "To: Italian B.M.T. eli se paras", "Pe: Vegepihvi",
                       "La: American Steakhouse Melt", "Su: Kinkku"]
    subway_message = ""
    for day in range(0, len(subs_of_the_day)):
        if day == current_day:
            subway_message += "*" + subs_of_the_day[day] + "*"
        else:
            subway_message += subs_of_the_day[day]
        subway_message += "\n"
    return subway_message


def inside():
    line = utils.get_random_line_of_file('res/inside.txt')
    quote = utils.parse_quote(line)
    return quote


def matti():
    line = utils.get_random_line_of_file('res/matti.txt')
    quote = utils.parse_quote(line, "Profeetta Nykänen")
    return quote


def donald():
    line = utils.read_url_and_get_contents("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
    quote = utils.parse_quote(line, "Donald Trump")
    return quote


def help():
    return (utils.get_robot_emoji() +
            " *Väf-bot versio " + utils.get_version() + "* " + utils.get_robot_emoji() +
            "\n\n*Komennot:*\n/subit\tSubilista\n"
            "/inside\tInsideläppä\n"
            "/matti\tOppia profeetalta\n"
            "/donald\tDon't stump the Trump\n\n"
            "GitHub repo\thttps://git.io/v7VKt")
