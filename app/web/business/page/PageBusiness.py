#coding=utf-8
#TODO import ...
from app.common.constants import CommonConstants
from app.common.constants import DbConstants
from app.web.dal.DbOperate import DbOperate
from app.common.util import SimpleUtil
from app.common.util import DateUtil
import datetime


dboperate = DbOperate()

class PageBussiness(object):
	def __init__(self):
		#TODO 初始化
		pass

	def login_action(self, user, passwd):
		try:
			givenpasswd = SimpleUtil.get_md5(passwd)
			turepasswd = dboperate.pick_one(DbConstants.USER, CommonConstants.USERNAME, user)

			if turepasswd and turepasswd[CommonConstants.PASSWD] == givenpasswd:
				return True

			return False
		except EOFError, e:
			print e.message
			return False

	def register_action(self, user):
		return dboperate.insert_(DbConstants.USER, SimpleUtil.convert_to_dict(user))

	def auth_action(self, info={}):
		payload = info
		payload[CommonConstants.ISS] = CommonConstants.SIGNATURE
		payload[CommonConstants.EXP] = DateUtil.get_delay_time_by_hour(2)
		return SimpleUtil.jwt_encode(payload)
