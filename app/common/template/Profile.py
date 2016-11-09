#coding=utf-8
class UserPorfile(object):
	#用户名
	username = ""
	#用户id
	userid = 0
	#昵称
	nickname = ""
	#年龄
	age = 0
	#性别
	sex = ""
	#密码
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