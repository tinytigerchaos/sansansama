#coding=
class UserPorfile(object):
	username = ""
	userid = 0
	nickname = ""
	age = 0
	sex = ""
	passwd = ""
	def __init__(self):
		# self.nickname = user
		pass

	def setUser(self,username):
		self.username = username

	def setUserId(self,userid):
		self.userid = userid

	def setAge(self,age):
		self.age = age

	def setSex(self,sex):
		self.sex = sex

	def setPasswd(self,passwd):
		self.passwd = passwd

#