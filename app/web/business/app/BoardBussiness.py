# coding=utf-8
import pymongo

from app.common.constants import DbConstants
from app.common.constants import BoardConstants
from app.common.constants import CommonConstants
from app.web.dal.DbOperate import DbOperate
from app.common.util import SimpleUtil

dboperate = DbOperate()


class BoardBussiness(object):
	def add_comment(self, comment):
		return dboperate.insert_(DbConstants.COMMENT, SimpleUtil.convert_to_dict(comment))

	def add_piece(self, piece):
		return dboperate.insert_(DbConstants.PIECE, SimpleUtil.convert_to_dict(piece))

	def add_pads(self, pads):
		return dboperate.insert_(DbConstants.PADS, SimpleUtil.convert_to_dict(pads))

	def add_board(self, board):
		return dboperate.insert_(DbConstants.BOARD, SimpleUtil.convert_to_dict(board))

	def pick_comments(self, owner):
		res = []
		comments = dboperate.pick_(DbConstants.COMMENT, BoardConstants.OWNER, owner)
		for comment in comments.sort(BoardConstants.COMMENTTIME, pymongo.DESCENDING):
			res.append({BoardConstants.USER: comment[BoardConstants.USER],
						BoardConstants.COMMENT: comment[BoardConstants.COMMENT]})
		return res
