# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import uuid
import xmlHelper

from Test.testData import entity


class BOBetType(entity.Entity):

	def __init__(self, header, cols):
		super(BOBetType, self).__init__(header, cols)

	def toXml(self, parentNode):
		node = self.createNode('BOBetType', parentNode)
		attrs = {
			'ID': self.getColumnValue('ID'),
			'Code': self.getColumnValue('Code'),
			'HitCount': self.getColumnValue('HitCount')
		}
		self.setAttrsToNode(attrs, node)
		return node
