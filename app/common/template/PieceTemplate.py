# coding=utf-8
# piece 模板

from app.common.template.BaseTemplate import BaseTemplate


class PieceTemplate(BaseTemplate):
    piece_name = ""

    piece_type = ""

    def get_piece_name(self):
        return self.piece_name

    def set_piece_name(self, piece_name):
        self.piece_name = piece_name

    def get_piece_type(self):
        return self.piece_type

    def set_piece_type(self, piece_type):
        self.piece_type = piece_type
