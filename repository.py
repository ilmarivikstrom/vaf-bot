#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import ConfigParser
import mysql.connector

import utils

class Repository:
    def __init__(self):

        self.Connect()

    def Connect(self):
        self.db = mysql.connector.connect(
            host=utils.GetConfigValueWithKey('DB_HOST'),
            user=utils.GetConfigValueWithKey('DB_USER'),
            passwd=utils.GetConfigValueWithKey('DB_PASS'),
            database=utils.GetConfigValueWithKey('DB_NAME')
        )

    def insert(self, newMessageData):
        self.Connect()
        #print(json.dumps(newMessageData, indent=4, sort_keys=True))
        sql = "INSERT INTO received (chatfirst_name, chatid, chattype, chatusername, date, fromfirst_name, fromid, fromis_bot, fromlanguage_code, fromusername, message_id, text) VALUES " + utils.GetMessageValues(
            newMessageData)
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()
