import datetime

def toStandardStr(dt):
	return dt.strftime('%Y-%m-%d %H:%M:%S')


def parse(strDT):
	return datetime.datetime.strptime(strDT, '%Y-%m-%d %H:%M:%S')