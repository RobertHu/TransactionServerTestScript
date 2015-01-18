# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

from Test.util import tranUtil
from Test import enum, xmlHelper
import boOrder, boBetType

class Transaction(object):

	def __init__(self):
		self.name = 'Transaction'
		self.orderName = 'Order'
		self.boBetTypeName = 'BOBetType'


	def createOneTransaction(self, root):
		boBetTypeId = self.createBOBetType(root)
		self.createTranCommon(root, boBetTypeId)

	def createTrans(self):
		root = ET.Element('Transactions')
		boBetTypeId = self.createBOBetType(root)
		self.createTranCommon(root, boBetTypeId)
		self.createTranCommon(root, boBetTypeId)
		return root

	def createTranCommon(self, root,boBetTypeId):
		tranElement = ET.SubElement(root,self.name)
		attrs = tranUtil.getTransactionAttrsDict(enum.OrderType.BinaryOption)
		for k, v in attrs.items():
			tranElement.set(k,v)
		orderElement = ET.SubElement(tranElement, self.orderName)
		boOrder.createOpenOrder(orderElement, boBetTypeId)

	def createBOBetType(self, parent):
		betType = ET.SubElement(parent, self.boBetTypeName)
		return boBetType.createXmlNode(betType)
