#!/usr/bin/python
# -*- coding: utf-8 -*-


import ConfigParser
import json
import random
import urllib2

VERSION = "0.5"


def get_random_line_of_file(file):
    lines = open(file, 'r').read().splitlines()
    return random.choice(lines)


def get_robot_emoji():
    return "\xF0\x9F\xA4\x96"


def get_version():
    return VERSION


def parse_quote(line, name=None):
    if name is None:
        parts = line.split(';')
        return "_\"" + parts[0] + "\"_" + "  *-" + parts[1] + "*"
    return "_\"" + line + "\"_" + "  *-" + name + "*"


def read_url_and_get_contents(url):
    response = urllib2.urlopen(url)
    data = response.read()
    values = json.loads(data)
    return values["message"]


def get_chat_id(new_message_data):
    return new_message_data['chat']['id']


def get_message_text(new_message_data):
    return new_message_data['text']


def get_message_values(new_message_data, private=True):
    if private:
        values = "("
        values += "\""
        values += new_message_data['chat']['first_name']
        values += "\""
        values += ", "
        values += "\""
        values += str(new_message_data['chat']['id'])
        values += "\""
        values += ", "
        values += "\""
        values += new_message_data['chat']['type']
        values += "\""
        values += ", "
        values += "\""
        values += new_message_data['chat']['username']
        values += "\""
        values += ", "
        values += "\""
        values += str(new_message_data['date'])
        values += "\""
        values += ", "
        values += "\""
        values += new_message_data['from']['first_name']
        values += "\""
        values += ", "
        values += "\""
        values += str(new_message_data['from']['id'])
        values += "\""
        values += ", "
        values += "\""
        values += str(new_message_data['from']['is_bot'])
        values += "\""
        values += ", "
        values += "\""
        values += new_message_data['from']['language_code']
        values += "\""
        values += ", "
        values += "\""
        values += new_message_data['from']['username']
        values += "\""
        values += ", "
        values += "\""
        values += str(new_message_data['message_id'])
        values += "\""
        values += ", "
        values += "\""
        values += new_message_data['text']
        values += "\""
        values += ")"
        return values
    values = "("
    values += "\""
    values += str(new_message_data['chat']['all_members_are_administrators'])
    values += "\""
    values += ", "
    values += "\""
    values += str(new_message_data['chat']['id'])
    values += "\""
    values += ", "
    values += "\""
    values += new_message_data['chat']['title']
    values += "\""
    values += ", "
    values += "\""
    values += new_message_data['chat']['type']
    values += "\""
    values += ", "
    values += "\""
    values += str(new_message_data['date'])
    values += "\""
    values += ", "
    values += "\""
    values += str(new_message_data['entities'][0]['length'])
    values += "\""
    values += ", "
    values += "\""
    values += str(new_message_data['entities'][0]['offset'])
    values += "\""
    values += ", "
    values += "\""
    values += new_message_data['entities'][0]['type']
    values += "\""
    values += ", "
    values += "\""
    values += new_message_data['from']['first_name']
    values += "\""
    values += ", "
    values += "\""
    values += str(new_message_data['from']['id'])
    values += "\""
    values += ", "
    values += "\""
    values += str(new_message_data['from']['is_bot'])
    values += "\""
    values += ", "
    values += "\""
    values += new_message_data['from']['language_code']
    values += "\""
    values += ", "
    values += "\""
    values += new_message_data['from']['username']
    values += "\""
    values += ", "
    values += "\""
    values += str(new_message_data['message_id'])
    values += "\""
    values += ", "
    values += "\""
    values += new_message_data['text']
    values += "\""
    values += ")"
    return values



def starts_with(new_message_data, start):
    if (new_message_data.startswith(start)):
        return True
    return False


def get_config_value_with_key(key):
    config = ConfigParser.ConfigParser()
    config.read("vaf_bot.ini")
    return config.get('Credentials', key)
