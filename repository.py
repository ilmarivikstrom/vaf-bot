#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import ConfigParser
import mysql.connector

import utils

class Repository:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read("vaf_bot.ini")

        self.Connect()

    def Connect(self):
        self.db = mysql.connector.connect(
            host=self.config.get('Credentials', 'DB_HOST'),
            user=self.config.get('Credentials', 'DB_USER'),
            passwd=self.config.get('Credentials', 'DB_PASS'),
            database=self.config.get('Credentials', 'DB_NAME')
        )

    def insert(self, newMessageData):
        self.Connect()
        print(json.dumps(newMessageData, indent=4, sort_keys=True))
        sql = "INSERT INTO received (chatfirst_name, chatid, chattype, chatusername, date, fromfirst_name, fromid, fromis_bot, fromlanguage_code, fromusername, message_id, text) VALUES " + utils.GetMessageValues(
            newMessageData)
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()