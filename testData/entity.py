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

	def toXml(self, parentNode):
		node = self.createNode(self.getXmlTagName(), parentNode)
		attrs = self.getAttrDict()
		self.setAttrsToNode(attrs,node)

	def setAttrsToNode(self, attrs, node):
		for k, v in attrs.items():
			node.set(k, v)


	def createNode(self, name, parentNode):
		return ET.SubElement(parentNode, name)


	@abc.abstractmethod
	def getXmlTagName(self):
		return

	@abc.abstractmethod
	def getAttrDict(self):
		return



class Organization(Entity):
	"""docstring for """
	def __init__(self, headerDict, cols):
		super(Organization, self).__init__(headerDict, cols)
			
	def getXmlTagName(self):
		return 'Organization'

	def getAttrDict(self):
		return {
			'ID': self.getColumnValue('ID'),
			'Code': self.getColumnValue('Code')
		}



class OrderType(Entity):
	"""docstring for OrderType"""
	def __init__(self,  headerDict, cols):
		super(OrderType, self).__init__(headerDict, cols)

	def getXmlTagName(self):
		return 'OrderType'

	def getAttrDict(self):
		return {
			'ID': self.getColumnValue('ID'),
			'Code': self.getColumnValue('Code')
		}

class TradeDay(Entity):
	"""docstring for TradeDay"""
	def __init__(self, headerDict, cols):
		super(TradeDay, self).__init__(headerDict, cols)
		
	def getXmlTagName(self):
		return 'TradeDay'

	def getAttrDict(self):
		return {
			'TradeDay': self.getColumnValue('TradeDay'),
			'BeginTime': self.getColumnValue('BeginTime'),
			'EndTime': self.getColumnValue('EndTime'),
			'IsTraded': self.getColumnValue('IsTraded')
		}
