from app.web.base.BaseHandler import AppBaseHandler
from app.web.business import AppBusiness


appbusiness = AppBusiness()

class UploadImageHandler(AppBaseHandler):
	def post(self, *args, **kwargs):
		# TODO 完善上传图片接口
		user = ''
		image = None
		appbusiness.upload_image(user,image)
		pass

class AddArticleHandler(AppBaseHandler):
	def post(self, *args, **kwargs):
		user = ''
		article = None
		appbusiness.add_article(user,article)
		pass