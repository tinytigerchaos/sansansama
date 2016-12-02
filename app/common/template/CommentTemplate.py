#coding=utf-8

#评论模板

from app.common.template.BaseTemplate import BaseTemplate

class CommentTemplate(BaseTemplate):

	#评论
	comment = ""

	comment_user = ""

	comment_time = ""

	def get_comment(self):
		return self.comment

	def set_comment(self, comment):
		self.comment = comment

	def get_comment_user(self):
		return self.comment_user

	def set_comment_user(self, comment_user):
		self.comment_user = comment_user

	def get_comment_time(self):
		return self.comment_time

	def set_comment_time(self, comment_time):
		self.comment_time = comment_time
