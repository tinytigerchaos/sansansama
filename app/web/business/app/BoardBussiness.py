# coding=utf-8
import pymongo

from app.common.constants import BoardConstants
from app.common.constants import DbConstants
from app.common.constants import CommonConstants
from app.common.util import SimpleUtil
from app.web.dal.DbOperate import DbOperate

db_operate = DbOperate()


class BoardBussiness(object):

    def add_comment(self, comment):
        return db_operate.insert_(
            DbConstants.COMMENT,
            SimpleUtil.convert_to_dict(comment))

    def pick_comments(self, owner):
        res = []
        comments = db_operate.pick_(
            DbConstants.COMMENT, BoardConstants.OWNER, owner)
        for comment in comments.sort(
                BoardConstants.COMMENTTIME,
                pymongo.DESCENDING):
            res.append({BoardConstants.USER: comment[BoardConstants.USER],
                        BoardConstants.COMMENT: comment[BoardConstants.COMMENT]})
        return res

    def add_piece(self, piece):
        return db_operate.insert_(
            DbConstants.PIECE,
            SimpleUtil.convert_to_dict(piece))

    def add_pads(self, pads):
        return db_operate.insert_(
            DbConstants.PADS,
            SimpleUtil.convert_to_dict(pads))

    def pick_pads(self, owner):
        res = []
        pads = db_operate.pick_(
            DbConstants.PADS, BoardConstants.OWNER, owner)
        for pad in pads.comments.sort(
                CommonConstants.TIME,
                pymongo.DESCENDING):
            res.append({BoardConstants.PADNAME: pad[BoardConstants.PADNAME],
                        CommonConstants.TIME: pad[CommonConstants.TIME]})
        return res

    def add_board(self, board):
        return db_operate.insert_(
            DbConstants.BOARD,
            SimpleUtil.convert_to_dict(board))
