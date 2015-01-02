import xml.etree.ElementTree as ET
import uuid
import enum
import datetime
import datetimeHelper

timedelta = datetime.timedelta(seconds = 5)
basetime = datetime.datetime.strptime('2014-12-30 10:58:19', '%Y-%m-%d %H:%M:%S')

def createSportOrder(order):
	attrs = {
		'ID': str(uuid.uuid1()),
		'PriceIsQuote': 'false',
		'PriceTimestamp': datetimeHelper.toStandardStr(basetime - timedelta),
		'TradeOption': str(enum.TradeOption.Better),
		'IsOpen': enum.true,
		'IsBuy': enum.true,
		'SetPrice': str(0.9110),
		"SetPriceMaxMovePips": str(10),
		"DQMaxMove": str(10),
		"Lot": str(2)
	}
	for k, v in attrs.items():
		order.set(k,v)

def createCloseOrder(order):
	atts = {
		'ID': str(uuid.uuid1()),
		'PriceIsQuote': 'false',
		'PriceTimestamp': datetimeHelper.toStandardStr(basetime - timedelta),
		'TradeOption': str(enum.TradeOption.Better),
		'IsOpen': enum.false,
		'IsBuy': enum.false,
		'SetPrice': str(0.9110),
		"SetPriceMaxMovePips": str(10),
		"DQMaxMove": str(10),
		"Lot": str(1)
	}
	for k, v in atts.items():
		order.set(k,v)

def createOrderRelation(orderRelation):
	atts={
	
	}

