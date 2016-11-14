#coding=utf-8

from app.common.constants import DbConstants
from app.web.dal.DbOperate import DbOperate
from app.common.util import SimpleUtil
dboperate = DbOperate()

class BoardBussiness(object):

	def addComment(self,comment):
		return  dboperate.insert_(DbConstants.COMMENT,SimpleUtil.convert_to_dict(comment))

	def addPiece(self,piece):
		return dboperate.insert_(DbConstants.PIECE,SimpleUtil.convert_to_dict(piece))

	def addPads(self,pads):
		return dboperate.insert_(DbConstants.PADS,SimpleUtil.convert_to_dict(pads))

	def addBoard(self,board):
		return dboperate.insert_(DbConstants.BOARD,SimpleUtil.convert_to_dict(board))