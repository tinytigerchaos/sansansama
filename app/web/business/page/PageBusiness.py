#coding=utf-8
#TODO import ...
from app.common.constants import CommonConstants
from app.common.constants import DbConstants
from app.web.dal.DbOperate import DbOperate
from app.common.util import SimpleUtil
import datetime


dboperate = DbOperate()

class PageBussiness(object):
	def __init__(self):
		#TODO 初始化
		pass

	def loginAction(self,user,passwd):
		try:
			givenpasswd = SimpleUtil.GetMd5(passwd)
			turepasswd = dboperate.pick_(DbConstants.USER,CommonConstants.USERNAME,user)

			if turepasswd and turepasswd[CommonConstants.PASSWD] == givenpasswd :
				return True

			return False
		except EOFError,e:
			print e.message
			return False


	def registerAction(self,user):
		return dboperate.insert_(DbConstants.USER,SimpleUtil.convert_to_dict(user))


	def authAction(self,info={}):
		payload = info
		payload[CommonConstants.ISS] = CommonConstants.SIGNATURE
		payload[CommonConstants.EXP] = datetime.datetime.now() + datetime.timedelta(hours=2)
		return SimpleUtil.jwtEncode(payload)