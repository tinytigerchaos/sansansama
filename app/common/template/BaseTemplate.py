#coding=utf-8

#基础模板

class BaseTemplate(object):
	#TODO

	#时间
	time = ""
	#对象的所有者
	owner = ""
	#对象自身
	objectId = ""

	def getTime(self):
		return self.time

	def setTime(self,time):
		self.time = time

	def getOwner(self):
		return self.owner

	def setOwner(self,owner):
		return self.owner

	def getObjectId(self):
		return self.objectId

	def setObjectId(self,objectId):
		self.objectId = objectId
