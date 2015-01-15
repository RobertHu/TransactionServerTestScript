# -*- coding: utf-8 -*-
import uuid
import datetime
from Test import enum, datetimeHelper

def getTransactionAttrsDict(orderType, ):
	'''创建Transaction的公共模板'''
	
	basetime = datetime.datetime.now()
	endtime = basetime + datetime.timedelta(seconds = 5000)
	attrs={
		'ID': str(uuid.uuid1()),
		'AccountID': 'B940D4B7-4A4E-46DF-8EA4-77B0C3CC1A6B',
		'OrderType': orderType,
		'InstrumentID':'33C4C6E2-E33C-4A21-A01A-35F4EC647890',
		'Type': enum.TransactionType.Single,
		'SubType': enum.TransactionSubType.NoneItem,
		'BeginTime': datetimeHelper.toStandardStr(basetime),
		'EndTime': datetimeHelper.toStandardStr(endtime),
		'SubmitTime': datetimeHelper.toStandardStr(basetime),
		'SubmitorID': 'CB58B47D-A705-42DD-9308-6C6B26CE79A7'
	}
	return attrs

