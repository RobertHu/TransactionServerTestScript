# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from Test.util import singleton
import re
from Test import xmlHelper
import os


class Entity(object):

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


class TradePolicyDetail(Entity):

	def __init__(self, headerDict, cols):
		super(TradePolicyDetail, self).__init__(headerDict, cols)

	def toXml(self, parentNode):
		node = ET.SubElement(parentNode, 'TradePolicyDetail')
		attrs = {
			'TradePolicyID': self.getColumnValue('TradePolicyID'),
			'InstrumentID': self.getColumnValue('InstrumentID'),
			'ContractSize': self.getColumnValue('ContractSize')
		}
		columnBoPolicy = self.getColumnValue('BOPolicyID')
		if columnBoPolicy is not None:
			attrs.update(BOPolicyID = columnBoPolicy )
		self.setAttrsToNode(attrs, node)
		return node



class TradePolicy(Entity):

	def __init__(self, headerDict, cols):
		super(TradePolicy, self).__init__(headerDict, cols)

	def toXml(self, parentNode):
		node = ET.SubElement(parentNode, 'TradePolicy')
		attrs = {
			'ID': self.getColumnValue('ID'),
			'Code': self.getColumnValue('Code')
		}
		self.setAttrsToNode(attrs, node)



class Currency(Entity):

	def __init__(self, headerDict, cols):
		super(Currency, self).__init__(headerDict, cols);
		self.id = self.getColumnValue('ID')
		self.code = self.getColumnValue('Code')
		self.decimals = self.getColumnValue('Decimals')


	def toXml(self, parentNode):
		node = ET.SubElement(parentNode, 'Currency')
		attrs = {
			'ID': self.id,
			'Code': self.code,
			'Decimals': self.decimals
		}
		self.setAttrsToNode(attrs, node)
		return node


class CurrencyRate(Entity):

	def __init__(self, headerDict, cols):
		super(CurrencyRate, self).__init__(headerDict, cols)
		self.sourceCurrency = self.getColumnValue('SourceCurrencyID')
		self.targetCurrency = self.getColumnValue('TargetCurrencyID')
		self.rateIn = self.getColumnValue('RateIn')
		self.rateOut = self.getColumnValue('RateOut')

	def toXml(self, parentNode):
		node = ET.SubElement(parentNode, 'CurrencyRate')
		attrs = {
			'SourceCurrencyID': self.sourceCurrency,
			'TargetCurrencyID': self.targetCurrency,
			'RateIn': self.rateIn,
			'RateOut': self.rateOut
		}
		self.setAttrsToNode(attrs, node)
		return node


class Customer(Entity):

	def __init__(self, headerDict, cols):
		super(Customer, self).__init__(headerDict, cols)
		self.id = self.getColumnValue('ID')
		self.name = self.getColumnValue('Name')
		self.publicQuotePolicyId = self.getColumnValue('PublicQuotePolicyID')
		self.privateQuotePolicyId = self.getColumnValue('PrivateQuotePolicyID')

	def toXml(self, parentNode):
		node = ET.SubElement(parentNode, 'Customer')
		attrs = {
			'ID': self.id,
			'Name': self.name,
			'PublicQuotePolicyID': self.publicQuotePolicyId,
			'PrivateQuotePolicyID': self.privateQuotePolicyId
		}
		self.setAttrsToNode(attrs, node)
		return node

class Instrument(Entity):

	def __init__(self, headerDict, cols):
		super(Instrument, self).__init__(headerDict, cols)
		self.id = self.getColumnValue('ID')
		self.code = self.getColumnValue('Code')
		self.category = self.getColumnValue('Category')
		self.beginTime = self.getColumnValue('BeginTime')
		self.endTime = self.getColumnValue('EndTime')
		self.numeratorUnit = self.getColumnValue('NumeratorUnit')
		self.denominator = self.getColumnValue('Denominator')

	def toXml(self, parentNode):
		node = ET.SubElement(parentNode, 'Instrument')
		attrs = {
			'ID': self.id,
			'Code': self.code,
			'Category': self.category,
			'NumeratorUnit': self.numeratorUnit,
			'Denominator': self.denominator,
			'DayOpenTime': self.beginTime,
			'DayCloseTime': self.endTime,
			'CurrencyID': self.getColumnValue('CurrencyID'),
			'IsActive': self.getColumnValue('IsActive')
		}
		self.setAttrsToNode(attrs, node)
		return node




@singleton.singleton
class SettingRepository(object):

	def __init__(self):
		self.re =  re.compile('\t')
		self.dir = os.path.dirname(__file__)
		self.entityCols = []
		self.currencies = []
		self.currencyRates = []
		self.customers = []
		self.instruments = []
		self.tradePolicies = []
		self.tradePolicyDetails = []
		self.entityCols.append(self.currencies)
		self.entityCols.append(self.currencyRates)
		self.entityCols.append(self.customers)
		self.entityCols.append(self.instruments)
		self.entityCols.append(self.tradePolicies)
		self.entityCols.append(self.tradePolicyDetails)
		self.loadEntities()

	def loadEntities(self):
		self.loadCurrency()
		self.loadCurrencyRates()
		self.loadCustomer()
		self.loadInstruments()
		self.loadTradePolicies()
		self.loadTradePolicyDetails()

	def loadCurrency(self):
		for header, cols in self.loadFromFile('currencyData.txt'):
			self.currencies.append(Currency(header, cols))

	def loadCurrencyRates(self):
		for header, cols in self.loadFromFile('currencyRateData.txt'):
			self.currencyRates.append(CurrencyRate(header, cols))

	def loadCustomer(self):
		for header, cols in self.loadFromFile('customerData.txt'):
			self.customers.append(Customer(header, cols))

	def loadInstruments(self):
		for header, cols in self.loadFromFile('instrumentData.txt'):
			self.instruments.append(Instrument(header, cols))

	def loadTradePolicies(self):
		for header, cols in self.loadFromFile('tradePolicyData.txt'):
			self.tradePolicies.append(TradePolicy(header, cols))

	def loadTradePolicyDetails(self):
		for header, cols in self.loadFromFile('tradePolicyDetailData.txt'):
			self.tradePolicyDetails.append(TradePolicyDetail(header, cols))


	def loadFromFile(self, fileName):
		filePath = os.path.join(self.dir, fileName)
		f = open(filePath, 'r')
		headerDict = self.parseHeaders(f.readline())
		for line in f:
			if line is not None:
				cols = self.re.split(line)
				yield (headerDict ,cols)

	def parseHeaders(self, headerLine):
		headerCols = self.re.split(headerLine)
		headerDict = dict()
		for n, v in enumerate(headerCols):
			headerDict[v.strip()] = n
		return headerDict



	def toXml(self):
		root = ET.Element('Settings')
		addMethodRoot = ET.SubElement(root, 'Add')

		for cols in self.entityCols:
			for m in cols:
				m.toXml(addMethodRoot)
		return xmlHelper.toXml(root)


class Setting(object):

	'''产生组装SettingManager所需要的数据'''

	def __init__(self):
		self.root = ET.Element('Setting')
		self.instrumentId = '33C4C6E2-E33C-4A21-A01A-35F4EC647890'
		self.tradePolicyId = '99A5FE24-D8B7-42A2-9DBE-BF1608F82F96'
		self.customerId = 'CB58B47D-A705-42DD-9308-6C6B26CE79A7'
		self.IsMultiCurrency = True
		self.accountCurrencyId = 'F940A509-4ED6-4A92-A6F0-CD9A60601084'
		self.instrumentCurrencyId = '0DA665B5-9AA5-49D7-A301-048F1428CA4A'

	def generateInstrumentData(self):
		node = self.createNode('Instrument')
		attrs = {
			'ID': self.instrumentId,
			'CurrencyID': '0DA665B5-9AA5-49D7-A301-048F1428CA4A',
			'Code': 'AUD',
			'Category': '10',
			'NumeratorUnit': '1',
			'Denominator': '10000'
		}
		self.setAttrsToNode(node, attrs)


	def generateCustomerData(self):
		node = self.createNode('Customer')
		attrs = {
			'ID': self.customerId,
			'PublicQuotePolicyID': 'AD0BEE1C-7E75-4C80-B8FD-920B6B0B0EF2',
			'PrivateQuotePolicyID': 'AD0BEE1C-7E75-4C80-B8FD-920B6B0B0EF2',
			'Name': 'XD02'
		}
		self.setAttrsToNode(node,attrs)

	def generateTradePolicyData(self):
		node = self.createNode('TradePolicy')
		attrs = {
			'ID': self.tradePolicyId,
		}
		self.setAttrsToNode(node,attrs)
		detailNode = this.createNodeWithParent(node,'TradePolicyDetail')
		detailAttrs = {
			'InstrumentID': self.instrumentId,
			'BOPolicyID': '6E0591DD-0F08-4CF3-9336-63A6D7261AE2'
		}
		self.setAttrsToNode(detailNode, detailAttrs)

	def generateAccountData(self):
		node = self.createNode("Account")
		attrs = {
			'ID': 'B940D4B7-4A4E-46DF-8EA4-77B0C3CC1A6B',
			'TradePolicyID': self.tradePolicyId,
			'CustomerID': self.customerId,
			'CurrencyID': 'F940A509-4ED6-4A92-A6F0-CD9A60601084',
			'IsMultiCurrency': 'true'
		}
		self.setAttrsToNode(node, attrs)

	def generateCurrencyRateData(self):
		node = self.createNode('CurrencyRate')
		attrs = {
			''
		}

	def createNode(self, name):
		return ET.SubElement(self.root, name)

	def createNodeWithParent(self, parent, name):
		return ET.SubElement(parent, name)

	def setAttrsToNode(self, node, attrs):
		for k, v in attrs.items():
			node.set(k, v)

