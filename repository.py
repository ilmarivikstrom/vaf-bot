#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import mysql.connector

import utils


class Repository:
    def __init__(self):

        self.connect()

    def connect(self):
        self.db = mysql.connector.connect(
            host=utils.get_config_value_with_key('DB_HOST'),
            user=utils.get_config_value_with_key('DB_USER'),
            passwd=utils.get_config_value_with_key('DB_PASS'),
            database=utils.get_config_value_with_key('DB_NAME')
        )

    def insert(self, new_message_data):
        self.connect()
        #print(json.dumps(newMessageData, indent=4, sort_keys=True))
        sql = "INSERT INTO received (chatfirst_name, chatid, chattype, chatusername, date, fromfirst_name, fromid, fromis_bot, fromlanguage_code, fromusername, message_id, text) VALUES " + utils.get_message_values(
            new_message_data)
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()
