#coding=utf-8
from app.common.constants import PathConstants
from app.common.constants import CommonConstants
from app.web.base.handlers.BaseHandlers import PageBaseHandler
from app.web.business.page.PageBusiness import PageBussiness

pagebuiness = PageBussiness()

class MainHandler(PageBaseHandler):
	def get(self):
		# self.write("hello !")
		self.render(PathConstants.HTMLS_MODULESUSE + "main.html")


class LoginHandler(PageBaseHandler):
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

		pagebuiness.loginAction(user,passwd)
			# md5 passwd 从数据库内提出用户密码并比较
			# '''
			# 出错则重定向到自己
			# '''
		# logincode = ""

		# 设置用户cookies
		self.set_secure_cookie(CommonConstants.USER, user)
		self.set_secure_cookie(CommonConstants.LOGINCODE, CommonConstants.LOGIN)

		#重定向到用户界面
		self.redirect("/userCenter/" + user )

class UserHandler(PageBaseHandler):
	def get(self,user):
		if user != self.get_current_user():
			self.redirect("/login")
			return
		if self.get_login_code() != CommonConstants.LOGIN:
			self.redirect("/login")
			return

		self.write("welcome  " + user )

		# self.render("user.html")




