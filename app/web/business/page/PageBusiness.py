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
			turepasswd = dboperate.pick_(CommonConstants.PASSWD,user)
			if givenpasswd == turepasswd:
				return self.login(user)
		except:
			return [False,""]
		#TODO 校验密码

	def login(self,user):
		return [True,"login"]