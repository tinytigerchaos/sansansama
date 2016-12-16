# coding=utf-8

# 基础模板


class BaseTemplate(object):
    # TODO

    # 时间
    time = ""
    # 对象的所有者
    owner = ""
    # 对象自身
    object_id = ""

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_owner(self):
        return self.owner

    def set_owner(self, owner):
        self.owner = owner

    def get_object_id(self):
        return self.object_id

    def set_object_id(self, object_id):
        self.object_id = object_id
