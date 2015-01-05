import xml.etree.ElementTree as ET
import uuid
import enum
import datetime
import datetimeHelper
import xmlHelper

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
	xmlHelper.setAttrs(order,attrs)

def createCloseOrder(order, openOrderID):
	attrs = {
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
	xmlHelper.setAttrs(order,attrs)
	orderRelaitonElement = ET.SubElement(order,'OrderRelation')
	setAttrs(orderRelaitonElement, openOrderID)

def setAttrs(orderRelation, openOrderID):
	attrs={
		'OpenOrderID': openOrderID,
		'ClosedLot': '1'
	}
	xmlHelper.setAttrs(orderRelation, attrs)

