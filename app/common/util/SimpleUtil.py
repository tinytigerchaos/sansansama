# coding=utf-8
import hashlib

import jwt

from app.common.constants import CommonConstants


def get_md5(value):
    md5 = hashlib.md5()
    md5.update(value + CommonConstants.ADDMD5)
    return md5.hexdigest()


def convert_to_dict(obj):
    dict_ = {}
    dict_.update(obj.__dict__)
    return dict_


def jwt_encode(info):
    header = {
        "typ": "JWT",
        "alg": "HS256"
    }
    return jwt.encode(headers=header, payload=info, key=CommonConstants.JWTKEY)


def jwt_decode(code):
    return jwt.decode(jwt=code, key=CommonConstants.JWTKEY)
