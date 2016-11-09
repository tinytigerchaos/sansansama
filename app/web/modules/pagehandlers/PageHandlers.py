#coding=utf-8
import tornado
from app.common.constants import PathConstants
from app.common.constants import CommonConstants
from app.web.base.handlers.BaseHandlers import BaseHandler
from app.web.business.page.PageBusiness import PageBussiness
from app.common.template import Profile
from app.common.util import SimpleUtil

pagebuiness = PageBussiness()

class MainHandler(BaseHandler):
	def get(self):
		# self.write("hello !")
		self.render(PathConstants.HTMLS_MODULESUSE + "main.html")


class LoginHandler(BaseHandler):
	def get(self):
		self.render(PathConstants.HTMLS_MODULESUSE + "login.html")

	def post(self):
		user = ''
		passwd = ''
		try:
			user = self.get_argument(CommonConstants.USER)
			passwd = self.get_argument(CommonConstants.PASSWD)
		except:
			self.redirect("/login")
			return
		if user == '' or passwd == '':
			self.redirect("/login")
			return


		if not pagebuiness.loginAction(user,passwd):
			self.redirect("/login")
			return

		# 设置用户cookies
		userinfo = {CommonConstants.USERNAME:user}
		self.set_secure_cookie(CommonConstants.AUTH,pagebuiness.authAction(userinfo))
		#重定向到用户界面
		self.redirect("/userCenter")
		return

class UserHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		user = tornado.escape.xhtml_escape(self.current_user)

		self.write("welcome  " + user )
		return

class RegisterHandler(BaseHandler):
	def get(self):
		self.render(PathConstants.HTMLS_MODULESUSE + "register.html")

	def post(self):
		username = self.get_argument(CommonConstants.USERNAME)
		passwd = self.get_argument(CommonConstants.PASSWD)
		age = self.get_argument(CommonConstants.AGE)

		#TODO 校验参数


		user = Profile.UserPorfile()
		user.setUser(username)
		user.setPasswd(SimpleUtil.GetMd5(passwd))
		user.setAge(age)


		pagebuiness.registerAction(user)
		return



