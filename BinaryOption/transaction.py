# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

from Test.util import tranUtil
from Test import enum, xmlHelper
import boOrder, boBetType

class Transaction(object):

	def __init__(self, root, boBetTypeId):
		self.name = 'Transaction'
		self.orderName = 'Order'
		self.boBetTypeName = 'BOBetType'
		self.root = root
		self.boBetTypeId = boBetTypeId

	def createForGeneral(self):
		node = self.createNode('General')
		self.createTranCommon(node)

	def createForSort(self):
		node = self.createNode('Sort')
		self.createTranCommon(node)
		self.createTranCommon(node)

	def createHitTran(self):
		node = self.createNode('Hit')
		return self.createTranCommon(node)

	def createCloseTran(self):
		node = self.createNode('Close')
		return self.createTranCommon(node)

	def createTranCommon(self, root):
		tranElement = ET.SubElement(root,self.name)
		attrs = tranUtil.getTransactionAttrsDict(enum.OrderType.BinaryOption)
		for k, v in attrs.items():
			tranElement.set(k,v)
		orderElement = ET.SubElement(tranElement, self.orderName)
		boOrder.createOpenOrder(orderElement, self.boBetTypeId)

	def createNode(self, nodeName):
		return ET.SubElement(self.root, nodeName)
