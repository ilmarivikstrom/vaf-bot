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

    def insert(self, new_message_data, private=True):
        if new_message_data['chat']['type'] == 'group':
            private=False
        self.connect()
        #print(json.dumps(newMessageData, indent=4, sort_keys=True))
        if private:
            sql = "INSERT INTO received_private (chatfirst_name, chatid, chattype, chatusername, date, fromfirst_name, fromid, fromis_bot, fromlanguage_code, fromusername, message_id, text) VALUES " + utils.get_message_values(new_message_data, True)
        else:
            sql = "INSERT INTO received_group (chatall_members_are_administrators, chatid, chattitle, chattype, date, entitieslength, entitiesoffset, entitiestype, fromfirst_name, fromid, fromis_bot, fromlanguage_code, fromusername, message_id, text) VALUES " + utils.get_message_values(new_message_data, False)
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()
