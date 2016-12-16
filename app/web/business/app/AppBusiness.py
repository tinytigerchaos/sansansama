# coding=utf-8
# AppHandler的业务方法
from app.common.constants import CommonConstants
from app.web.dal.DbOperate import DbOperate

db_operate = DbOperate()


class AppBusiness(object):
	def upload_image(self, user, image):
		return db_operate.insert_(user=user, data=image, data_info=CommonConstants.IMAGE)

	def add_article(self, user, article):
		return db_operate.insert_(user=user, data=article, data_info=CommonConstants.ARTICLE)

	def delete_image(self, user, image_info):
		return db_operate.delete_(user=user, data_info=image_info)

	def delete_article(self, user, article_info):
		return db_operate.delete_(user=user, data_info=article_info)
