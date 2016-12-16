# coding=utf-8
# info:

from app.common.template.BaseTemplate import BaseTemplate


class PadTemplate(BaseTemplate):
    # TODO:
    pad_name = ""

    def set_pad_name(self, pad_name):
        self.pad_name = pad_name

    def get_pad_name(self):
        return self.pad_name
