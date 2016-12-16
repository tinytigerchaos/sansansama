# coding=utf-8
from app.common.constants import CommonConstants
from app.web.base.handlers.BaseHandlers import BaseHandler
from app.web.business.app.AppBusiness import AppBusiness
import tornado.web

appbusiness = AppBusiness()


class UploadImageHandler(BaseHandler):

    def post(self, user):
        # TODO 完善上传图片接口
        file_metas = self.request.files[CommonConstants.IMAGE]
        image = file_metas[0].get('body')
        appbusiness.upload_image(user, image)


class AddArticleHandler(BaseHandler):

    @tornado.web.authenticated
    def post(self):
        article = self.get_argument(CommonConstants.ARTICLE)
        appbusiness.add_article(article)
        return
