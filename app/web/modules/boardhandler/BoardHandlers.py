# coding=utf-8
# info:
import tornado

from app.web.base.handlers.BaseHandlers import BaseHandler
from app.common.template.CommentTemplate import CommentTemplate
from app.common.template.PadTemplate import PadTemplate
from app.web.business.app.BoardBussiness import BoardBussiness
from app.common.constants import BoardConstants
from app.common.constants import CommonConstants
from app.common.util import DateUtil

import json


boardBussiness = BoardBussiness()
#
#
#


class AddBoardHandler(BaseHandler):
    # TODO:
    pass

#
#
#


# 添加贴纸板
# parma:padname
# res:返回添加状态
class AddPadHandler(BaseHandler):

    @tornado.web.authenticated
    def post(self):
        res = {}
        pad_name = self.get_argument(BoardConstants.PADNAME)
        user = self.current_user
        pad = PadTemplate()
        pad.set_owner(user)
        pad.set_object_id(user + DateUtil.get_time_now() + pad_name)
        pad.set_time(DateUtil.get_time_now_data())
        pad.set_pad_name(pad_name)
        boardBussiness.add_pads(pad)
        res['status'] = 'ok'

        self.write(json.dumps(res))
        self.flush()
        return

# 提取贴纸板接口
# parma:owner
# res:status
# res:data
class PickPadsHandler(BaseHandler):

    @tornado.web.authenticated
    def post(self):
        res = {}
        owner = self.get_argument(BoardConstants.OWNER)
        res["data"] = boardBussiness.pick_comments(owner)
        res["status"] = "ok"
        self.write(json.dumps(res))
        self.flush()
        return

#
#
#


class AddPieceHandler(BaseHandler):
    # TODO:
    pass

# url:Board/addComment
# parms:comment 评论内容
# parms:objectId 评论自身id
# parms:owner 评论的所有者


class AddCommentHandler(BaseHandler):

    @tornado.web.authenticated
    def post(self):
        res = {}
        user = self.current_user
        comment = self.get_argument(BoardConstants.COMMENT)
        object_id = self.get_argument(
            CommonConstants.USERNAME) + BoardConstants.COMMENT + DateUtil.get_time_now()
        owner = self.get_argument(BoardConstants.OWNER)

        commentOb = CommentTemplate()

        commentOb.set_comment(comment)
        commentOb.set_object_id(object_id)
        commentOb.set_comment_user(user)
        commentOb.set_owner(owner)
        commentOb.set_comment_time(DateUtil.get_time_now_data())
        boardBussiness.add_comment(commentOb)
        res["status"] = "ok"
        res["data"] = {
            BoardConstants.COMMENT: comment,
            BoardConstants.USER: user}
        self.write(json.dumps(res))
        self.flush()
        self.finish()
        return


# 提取评论接口
# parma:owner
# res:status
# res:data
class PickCommentsHandlers(BaseHandler):

    @tornado.web.authenticated
    def post(self):
        res = {}
        owner = self.get_argument(BoardConstants.OWNER)
        res["data"] = boardBussiness.pick_comments(owner)
        res["status"] = "ok"
        self.write(json.dumps(res))
        self.flush()
        return




