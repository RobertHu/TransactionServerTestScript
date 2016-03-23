# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from Test.util import singleton
import re
from Test import xmlHelper
import os
import abc
import settingAccount
import entity

from Test.common import dbDataParser


class TradePolicyDetail(entity.Entity):

	def __init__(self, headerDict, cols):
		super(TradePolicyDetail, self).__init__(headerDict, cols)

	def getXmlTagName(self):
		return 'TradePolicyDetail'

	def getAttrDict(self):
		return {
		'TradePolicyID': self.getColumnValue('TradePolicyID'),
		'InstrumentID': self.getColumnValue('InstrumentID'),
		'ContractSize': self.getColumnValue('ContractSize')
		}




class TradePolicy(entity.Entity):

	def __init__(self, headerDict, cols):
		super(TradePolicy, self).__init__(headerDict, cols)

	def getXmlTagName(self):
		return 'TradePolicy'

	def getAttrDict(self):
		return {
			'ID': self.getColumnValue('ID'),
			'Code': self.getColumnValue('Code')
		}




class Currency(entity.Entity):

	def __init__(self, headerDict, cols):
		super(Currency, self).__init__(headerDict, cols);
		self.id = self.getColumnValue('ID')
		self.code = self.getColumnValue('Code')
		self.decimals = self.getColumnValue('Decimals')


	def getXmlTagName(self):
		return 'Currency'

	def getAttrDict(self):
		return {
			'ID': self.id,
			'Code': self.code,
			'Decimals': self.decimals
		}

class SystemParameter(entity.Entity):

	def __init__(self, headerDict, cols):
		super(SystemParameter, self).__init__(headerDict, cols);

	def getXmlTagName(self):
		return 'SystemParameter'

	def getAttrDict(self):
		return	{
			'TradeDayBeginTime': self.getColumnValue('TradeDayBeginTime'),
			'MooMocAcceptDuration': self.getColumnValue('MooMocAcceptDuration'),
			'MooMocCancelDuration': self.getColumnValue('MooMocCancelDuration'),
			'DQDelayTimeOption': self.getColumnValue('DQDelayTimeOption'),
			'PlaceCheckType': self.getColumnValue('PlaceCheckType'),
			'NeedsFillCheck': self.getColumnValue('NeedsFillCheck'),
			'CanDealerViewAccountInfo': self.getColumnValue('CanDealerViewAccountInfo'),
			'UseNightNecessaryWhenBreak': self.getColumnValue('UseNightNecessaryWhenBreak'),
			'BalanceDeficitAllowPay': self.getColumnValue('BalanceDeficitAllowPay'),
			'IncludeFeeOnRiskAction': self.getColumnValue('IncludeFeeOnRiskAction'),
			'IncludeFeeOnRiskAction': self.getColumnValue('IncludeFeeOnRiskAction'),
			'EnableExportOrder': self.getColumnValue('EnableExportOrder'),
			'EnableEmailNotify': self.getColumnValue('EnableEmailNotify'),
			'EmailNotifyChangePassword': self.getColumnValue('EmailNotifyChangePassword'),
			'CurrencyRateUpdateDuration': self.getColumnValue('CurrencyRateUpdateDuration'),
			# 'DefaultQuotePolicyId': self.getColumnValue('DefaultQuotePolicyId'),
			'MaxPriceDelayForSpotOrder': self.getColumnValue('MaxPriceDelayForSpotOrder'),
			'RiskActionOnPendingConfirmLimit': self.getColumnValue('RiskActionOnPendingConfirmLimit'),
			'LmtQuantityOnMaxLotChange': self.getColumnValue('LmtQuantityOnMaxLotChange'),
			'STPAtHitPriceOption': self.getColumnValue('STPAtHitPriceOption'),
			'EvaluateIfDonePlacingOnStpConfirm': self.getColumnValue('EvaluateIfDonePlacingOnStpConfirm')
		}




class CurrencyRate(entity.Entity):

	def __init__(self, headerDict, cols):
		super(CurrencyRate, self).__init__(headerDict, cols)
		self.sourceCurrency = self.getColumnValue('SourceCurrencyID')
		self.targetCurrency = self.getColumnValue('TargetCurrencyID')
		self.rateIn = self.getColumnValue('RateIn')
		self.rateOut = self.getColumnValue('RateOut')

	def getXmlTagName(self):
		return 'CurrencyRate'

	def getAttrDict(self):
		return {
			'SourceCurrencyID': self.sourceCurrency,
			'TargetCurrencyID': self.targetCurrency,
			'RateIn': self.rateIn,
			'RateOut': self.rateOut
		}


class Customer(entity.Entity):

	def __init__(self, headerDict, cols):
		super(Customer, self).__init__(headerDict, cols)
		self.id = self.getColumnValue('ID')
		self.name = self.getColumnValue('Name')
		self.publicQuotePolicyId = self.getColumnValue('PublicQuotePolicyID')
		self.privateQuotePolicyId = self.getColumnValue('PrivateQuotePolicyID')

	def getXmlTagName(self):
		return 'Customer'

	def getAttrDict(self):
		return {
			'ID': self.id,
			'Name': self.name,
			'PublicQuotePolicyID': self.publicQuotePolicyId,
			'PrivateQuotePolicyID': self.privateQuotePolicyId
		}

class Instrument(entity.Entity):

	def __init__(self, headerDict, cols):
		super(Instrument, self).__init__(headerDict, cols)
		self.id = self.getColumnValue('ID')
		self.code = self.getColumnValue('Code')
		self.category = self.getColumnValue('Category')
		self.beginTime = self.getColumnValue('BeginTime')
		self.endTime = self.getColumnValue('EndTime')
		self.numeratorUnit = self.getColumnValue('NumeratorUnit')
		self.denominator = self.getColumnValue('Denominator')
		self.category = self.getColumnValue('Category')

	def getXmlTagName(self):
		return "Instrument"

	def getAttrDict(self):
		return {
			'ID': self.id,
			'Code': self.code,
			'Category': self.category,
			'NumeratorUnit': self.numeratorUnit,
			'Denominator': self.denominator,
			'DayOpenTime': self.beginTime,
			'DayCloseTime': self.endTime,
			'CurrencyID': self.getColumnValue('CurrencyID'),
			'IsActive': self.getColumnValue('IsActive'),
			'Category': self.category
		}



class  SettingParameter(object):
	"""docstring for  SettingParameter"""
	def __init__(self, fileName, modelClass):
		super(SettingParameter, self).__init__()
		self.fileName = fileName
		self.modelClass = modelClass
		self.models = []



class SettingRepository(dbDataParser.Parser):

	def __init__(self, parameters):
		super(SettingRepository, self).__init__(os.path.dirname(__file__))
		self.settingParameters = self.loadSettingParameters(parameters)
		self.loadEntities()

	def loadSettingParameters(self, parameters):
		result = []
		for eachParameter in parameters:
			fileName, modelClass = eachParameter
			result.append(SettingParameter(fileName,modelClass))
		return result

	def loadEntities(self):
		for eachParameter in self.settingParameters:
			self.buildEntitiesCommon(eachParameter.fileName, eachParameter.models, eachParameter.modelClass)

	def toXml(self):
		root = ET.Element('Settings')
		addMethodRoot = ET.SubElement(root, 'Add')

		for eachParameter in self.settingParameters:
			for eachModel in eachParameter.models:
				eachModel.toXml(addMethodRoot)
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

