#coding=utf-8
#piece 模板

from app.common.template.BaseTemplate import BaseTemplate

class PieceTemplate(BaseTemplate):
	pieceName = ""

	pieceType = ""

	def getPieceName(self):
		return self.pieceName

	def setPieceName(self, pieceName):
		self.pieceName = pieceName

	def getPieceType(self):
		return self.pieceType

	def setPieceType(self, pieceType):
		self.pieceType = pieceType