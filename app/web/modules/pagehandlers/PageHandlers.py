#coding=utf-8
import tornado
import json
from tornado import gen
from app.common.constants import PathConstants
from app.common.constants import CommonConstants
from app.web.base.handlers.BaseHandlers import BaseHandler
from app.web.business.page.PageBusiness import PageBussiness
from app.common.template import Profile
from app.common.util import SimpleUtil

pagebuiness = PageBussiness()

class MainHandler(BaseHandler):
	def get(self):
		self.render("main.html")


class LoginHandler(BaseHandler):
	def get(self):
		self.render("login.html")


	def post(self):
		user = ''
		passwd = ''
		try:
			user = self.get_argument(CommonConstants.USERNAME)
			passwd = self.get_argument(CommonConstants.PASSWD)
		except:
			self.redirect("/login")
			return
		if user == '' or passwd == '':
			self.redirect("/login")
			return

		if not pagebuiness.login_action(user, passwd):
			self.redirect("/login")
			return

		# 设置用户cookies
		userinfo = {CommonConstants.USERNAME: user}
		self.set_secure_cookie(CommonConstants.AUTH, pagebuiness.auth_action(userinfo))
		#重定向到用户界面
		self.redirect("/userCenter")
		return


class UserHandler(BaseHandler):
	def get(self):
		username = self.current_user

		self.render("userCenter.html", username=username)
		return


class RegisterHandler(BaseHandler):
	def get(self):
		self.render("register.html")

	# @gen.coroutine
	def post(self):
		res = {}
		username = self.get_argument(CommonConstants.USERNAME)
		passwd = self.get_argument(CommonConstants.PASSWD)
		#TODO 校验参数
		#对象赋值
		user = Profile.UserPorfile()
		user.setUser(username)
		user.setPasswd(SimpleUtil.GetMd5(passwd))

		pagebuiness.registerAction(user)
		res['status'] = 'ok'
		self.write(json.dumps(res))
		self.flush()
		self.finish()
		# raise gen.Return(json.dumps(res))
		return


