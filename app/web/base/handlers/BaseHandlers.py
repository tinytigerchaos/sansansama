#coding=utf-8
import tornado.web
import time
from app.common.util import SimpleUtil
from app.common.constants import CommonConstants


class BaseHandler(tornado.web.RequestHandler):

	def initialize(self):
		#TODO 初始化
		pass

	def get_current_user(self):
		authinfo = SimpleUtil.jwtDecode(self.get_secure_cookie(CommonConstants.AUTH))
		if authinfo[CommonConstants.ISS] != CommonConstants.SIGNATURE or int(authinfo[CommonConstants.EXP]) < int(time.time()):
			return
		return authinfo[CommonConstants.USERNAME]

# class AppBaseHandler(tornado.web.RequestHandler):
# 	def initialize(self):
# 		#TODO 初始化
# 		pass