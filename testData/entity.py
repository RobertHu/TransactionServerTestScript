import xml.etree.ElementTree as ET
import abc

class Entity(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, headerDict, cols):
		self.headerDict = headerDict
		self.cols = cols

	def getColumnValue(self, colName):
		index = self.headerDict[colName]
		colValue = self.cols[index].strip()
		if colValue == 'NULL':
			return None
		return colValue


	def setAttrsToNode(self, attrs, node):
		for k, v in attrs.items():
			node.set(k, v)

	def createNode(self, name, parentNode):
		return ET.SubElement(parentNode, name)

	@abc.abstractmethod
	def toXml(self, parentNode):
		return



