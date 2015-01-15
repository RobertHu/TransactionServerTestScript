import xml.etree.ElementTree as ET
import uuid
import enum
import datetime
import datetimeHelper
import order
import xmlHelper
from Test.util import tranUtil

def createCloseSportTran(openOrderId):
	tran = createTransactionElement(enum.OrderType.SpotTrade)
	orderElement = createOrderElement(tran)
	order.createCloseOrder(orderElement, openOrderId)
	return xmlHelper.toXml(tran)



def createOpenSportTran():
	tran = createTransactionElement(enum.OrderType.SpotTrade)
	orderElement = createOrderElement(tran)
	openOrderId = order.createSportOrder(orderElement)
	return (openOrderId, xmlHelper.toXml(tran))



def createTransactionElement(orderType):
	tran = ET.Element('Transaction')
	attrs = tranUtil.getTransactionAttrsDict(orderType)
	for k, v in attrs.items():
		tran.set(k,v)
	return tran


def createOrderElement(tran):
	return ET.SubElement(tran,'Order')


