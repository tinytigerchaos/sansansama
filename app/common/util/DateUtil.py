import datetime

def getDelayTimeByHour(hours):
	return datetime.datetime.now() + datetime.timedelta(hours)

def getTimeNow():
	return str(datetime.datetime.now())

