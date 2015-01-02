import xml.etree.ElementTree as ET
import uuid
import enum
import datetime
import datetimeHelper
import order

basetime = datetime.datetime.now()
endtime = basetime + datetime.timedelta(seconds = 1000)


def createCloseSportTran():



def createSportTran():
	tran = createTransactionElement()
	attrs = getTransactionAttrsDict()
	attrs.update(OrderType = enum.OrderType.SpotTrade)
	for k, v in attrs.items():
		tran.set(k,v)
	orderElement = createOrderElement(tran)
	order.createSportOrder(orderElement)
	return ET.tostring(tran, encoding='utf-8', method='xml')

def createTransactionElement():
	return ET.Element('Transaction')

def createOrderElement(tran):
	return ET.SubElement(tran,'Order')


def getTransactionAttrsDict():
	attrs={
		'ID': str(uuid.uuid1()),
		'AccountID': 'B940D4B7-4A4E-46DF-8EA4-77B0C3CC1A6B',
		'OrderType': '',
		'InstrumentID':'33C4C6E2-E33C-4A21-A01A-35F4EC647890',
		'Type': enum.TransactionType.Single,
		'SubType': enum.TransactionSubType.NoneItem,
		'BeginTime': datetimeHelper.toStandardStr(basetime),
		'EndTime': datetimeHelper.toStandardStr(endtime),
		'SubmitTime': datetimeHelper.toStandardStr(basetime),
		'SubmitorID': 'CB58B47D-A705-42DD-9308-6C6B26CE79A7'
	}
