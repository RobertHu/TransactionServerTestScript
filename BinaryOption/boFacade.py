# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import boPolicyDetails, transaction, boBetType
from Test import xmlHelper
from Test.common import dbDataParser
import os



class Facade(dbDataParser.Parser):

	'''提供BO模块的功能入口'''

	_instance = None

	def __new__(class_, *args, **kwargs):
		if not isinstance(class_._instance, class_):
			class_._instance = object.__new__(class_, *args, **kwargs)
		return class_._instance;

	def __init__(self):
		super(Facade,self).__init__(os.path.dirname(__file__))
		self.root = ET.Element('BO')
		self.tran = transaction.Transaction(self.root, '7EF0B4D0-B003-4196-AE57-0ED955CF9A28')

	def generateBoBetTypesXml(self):
		entities = []
		self.buildEntitiesCommon('boBetTypeData.txt', entities, boBetType.BOBetType)
		node = ET.Element('BOBetTypes')
		for m in entities:
			m.toXml(node)
		return xmlHelper.toXml(node)

	def toXml(self):
		self.tran.createForGeneral()
		self.tran.createForSort()
		self.tran.createHitTran()
		self.tran.createCloseTran()
		return xmlHelper.toXml(self.root)


	def generateBoPolicyDetailXml(self):
		detailsElement = ET.Element('BOPolicyDetails')
		boDetailRepository = boPolicyDetails.Repository()
		boDetailRepository.getXml(detailsElement)
		return xmlHelper.toXml(detailsElement)











