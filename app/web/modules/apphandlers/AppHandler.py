#coding=utf-8
from app.common.constants import CommonConstants
from app.web.base.handlers.BaseHandlers import AppBaseHandler
from app.web.business.app.AppBusiness import AppBusiness

appbusiness = AppBusiness()

class UploadImageHandler(AppBaseHandler):
	def post(self,user):
		# TODO 完善上传图片接口
		file_metas = self.request.files[CommonConstants.IMAGE]
		image = file_metas[0].get('body')
		appbusiness.upload_image(user,image)

class AddArticleHandler(AppBaseHandler):
	def post(self,user):
		article = self.get_argument(CommonConstants.ARTICLE)
		appbusiness.add_article(user,article)