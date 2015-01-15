import xml.etree.ElementTree as ET
import uuid
import enum
import datetime
import datetimeHelper
import xmlHelper
import orderUtil

def createSportOrder(order):
	attrs = orderUtil.createTemplateDict(enum.TradeOption.Better,enum.true,enum.true, '0.9110', '2')
	xmlHelper.setAttrs(order,attrs)
	return attrs['ID']

def createCloseOrder(order, openOrderID):
	attrs = orderUtil.createTemplateDict(enum.TradeOption.Better, enum.false, enum.false,'0.9110', '1')
	xmlHelper.setAttrs(order,attrs)
	orderRelaitonElement = ET.SubElement(order,'OrderRelation')
	setAttrs(orderRelaitonElement, openOrderID)

def setAttrs(orderRelation, openOrderID):
	attrs={
		'OpenOrderID': openOrderID,
		'ClosedLot': '1'
	}
	xmlHelper.setAttrs(orderRelation, attrs)

