import datetime

def get_delay_time_by_hour(hours):
	return datetime.datetime.now() + datetime.timedelta(hours)

def get_time_now():
	return str(datetime.datetime.now())

def get_time_now_data():
	return datetime.datetime.now()

