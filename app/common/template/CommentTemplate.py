#coding=utf-8

#评论模板

from app.common.template.BaseTemplate import BaseTemplate

class CommentTemplate(BaseTemplate):

	#评论
	comment = ""


	def getComment(self):
		return self.comment

	def setComment(self,comment):
		self.comment = comment
