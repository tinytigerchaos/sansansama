#coding=utf-8
import pymongo
from pymongo import MongoClient
from app.common.constants import CommonConstants
from app.common.util import DateUtil

client = MongoClient(CommonConstants.MONGODBIP, CommonConstants.MONGDBPORT)

class DbOperate(object):
	def __init__(self):
		self.db = client[CommonConstants.USER]
		self.db.authenticate(CommonConstants.MONGODBACCOUNT, CommonConstants.MONGDBPASSWD)

	def insert_(self, collection, data={}):
		collection = self.db[collection]
		post = data
		post[CommonConstants.TIME] = DateUtil.get_time_now_data()
		return collection.insert_one(post).inserted_id

	def pick_(self, collection, field, data_info):
		collection = self.db[collection]
		post = {field: data_info}
		return collection.find(post)

	def pick_one(self, collection, field, data_info):
		collection = self.db[collection]
		post = {field: data_info}
		return collection.find_one(post)

	def delete_(self, collection, field, data_info):
		collection = self.db[collection]
		post = {field: data_info}
		return collection.remove(post)

	def updata_(self, collection, data_info):
		pass