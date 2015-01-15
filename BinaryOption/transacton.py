# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

from Test.util import tranUtil
from Test import enum, xmlHelper
import boOrder


def createOpenTransactoin():
	'''创建一个BO单'''
	tranElement = ET.Element('Transaction')
	attrs = tranUtil.getTransactionAttrsDict(enum.OrderType.BinaryOption)
	for k, v in attrs.items():
		tranElement.set(k,v)
	orderElement = ET.SubElement(tranElement, 'Order')
	boOrder.createOpenOrder(orderElement)
	return xmlHelper.toXml(tranElement)

