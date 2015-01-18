# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import boPolicyDetails, transaction
from Test import xmlHelper



class Facade(object):

	'''提供BO模块的功能入口'''

	_instance = None

	def __new__(class_, *args, **kwargs):
		if not isinstance(class_._instance, class_):
			class_._instance = object.__new__(class_, *args, **kwargs)
		return class_._instance;

	def __init__(self):
		self.root = ET.Element('BO')
		self.transaction = transaction.Transaction()

	def generateOneTranXml(self):
		self.transaction.createOneTransaction(self.root)
		return xmlHelper.toXml(self.root)

	def generateTwoTranXml(self):
		result = self.transaction.createTrans()
		return xmlHelper.toXml(result)


	def generateBoPolicyDetailXml(self):
		detailsElement = ET.Element('BOPolicyDetails')
		boDetailRepository = boPolicyDetails.Repository()
		boDetailRepository.getXml(detailsElement)
		return xmlHelper.toXml(detailsElement)











