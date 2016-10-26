#coding=utf-8
import tornado.web

from app.common.constants import CommonConstants


class PageBaseHandler(tornado.web.RequestHandler):

	def initialize(self):
		#TODO 初始化
		pass

	def get_current_user(self):
		return self.get_secure_cookie(CommonConstants.USER)

	def get_login_code(self):
		return self.get_secure_cookie(CommonConstants.LOGINCODE)

class AppBaseHandler(tornado.web.RequestHandler):
	def initialize(self):
		#TODO 初始化
		pass