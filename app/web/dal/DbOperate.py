#coding=utf-8
from pymongo import MongoClient
import datetime
from app.common.constants import CommonConstants

client = MongoClient(CommonConstants.MONGODBIP, CommonConstants.MONGDBPORT)

class DbOperate(object):
	def __init__(self):
		self.db = client[CommonConstants.USER]

	def insert_(self,collection,data={}):
		collection = self.db[collection]
		post = data
		post[CommonConstants.TIME] = str(datetime.datetime.now())
		return collection.insert_one(post).inserted_id

	def pick_(self,collection,field,data_info):
		collection = self.db[collection]
		post = {field:data_info}
		return collection.find_one(post)

	def delete_(self,collection,field,data_info):
		collection = self.db[collection]
		post = {field: data_info}
		return collection.remove(post)

	def updata_(self,collection,data_info):
		pass