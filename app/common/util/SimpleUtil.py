#coding=utf-8
import hashlib
from app.common.constants import CommonConstants

def GetMd5(value):
	md5 = hashlib.md5()
	md5.update(value + CommonConstants.ADDMD5)
	return md5.hexdigest()
