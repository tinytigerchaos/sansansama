#coding=utf-8
#TODO import ...
from app.common.constants import CommonConstants
from app.common.util import SimpleUtil
from app.web.dal.DbOperate import DbOperate
dboperate = DbOperate()

class PageBussiness(object):
	def __init__(self):
		#TODO 初始化
		pass

	def loginAction(self,user,passwd):
		try:
			givenpasswd = SimpleUtil.GetMd5(user + passwd)
			turepasswd = dboperate.pick_(CommonConstants.PASSWD,CommonConstants.USER,user)


			if turepasswd and turepasswd[CommonConstants.PASSWD] == givenpasswd :
				self.login(user)
				return [True, user]

			return [False, user]
		except EOFError,e:
			print e.message
			return [True,""]
		#TODO 校验密码

	def login(self,user):
		# TODO:
		# return [False,"login"]
		pass