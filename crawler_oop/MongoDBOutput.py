# -*- coding: utf-8 -*-

import pymongo

class MongoDBOutput(object):   

    def __init__(self, db_name, collection_name):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client[db_name]
        self.collection = self.client.db[collection_name]
    def insert_to_mongo(self, data):
        if data is None:
            return
        self.collection.insert(data)        




























