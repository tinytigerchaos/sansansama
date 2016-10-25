from app.web.base.BaseHandler import PageBaseHandler
from app.common import commons

class MainHandler(PageBaseHandler):
	def get(self):
		self.render("main.html")


class LoginHandler(PageBaseHandler):
	def get(self):
		self.render("longin.html")

	def post(self):
		user = self.get_argument(commons.USER)
		passwd = self.get_argument(commons.PASSWD)
		# md5 passwd 从数据库内提出用户密码并比较
		'''
		出错则重定向到自己
		'''
		logincode = ""

		# 设置用户cookies
		self.set_secure_cookie(commons.USER,user)
		self.set_secure_cookie(commons.LOGINCODE,logincode)

		#重定向到用户界面
		self.redirect("/user/" + user )

class UserHandler(PageBaseHandler):
	def get(self,user):
		if user != self.get_current_user():
			self.redirect("/login")
			return

		self.render("user.html")




