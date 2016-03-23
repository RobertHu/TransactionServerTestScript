# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import sys

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
try:
    import Test
except ImportError:
    sys.path.append(os.path.join(ROOT_PATH, '..'))
    import Test

from Test.BinaryOption import boFacade


from Test import transaction
from Test import xmlHelper

from Test.testData import settingData
from testData import settingAccount
from testData import entity


if __name__ == '__main__':
	# openOrderId, xmlTran = transaction.createOpenSportTran()
	# print '-------------open tran----------'
	# print xmlTran
	# print '------------close tran ---------'
	# print transaction.createCloseSportTran(openOrderId)

	# facade = boFacade.Facade()	
	# print facade.generateBoBetTypesXml()
	# print facade.generateBoPolicyDetailXml()
	# print facade.toXml()

	pameters = [('instrumentData.txt', settingData.Instrument)]
	pameters.append(('currencyData.txt', settingData.Currency))
	pameters.append(('currencyRateData.txt', settingData.CurrencyRate))
	pameters.append(('customerData.txt', settingData.Customer))
	pameters.append(('tradePolicyDetailData.txt', settingData.TradePolicyDetail))
	pameters.append(('tradePolicyData.txt', settingData.TradePolicy))
	pameters.append(('accountData.txt', settingAccount.Account))
	pameters.append(('systemParameter.txt', settingData.SystemParameter))
	pameters.append(('organizationData.txt', entity.Organization))
	pameters.append(('orderTypeData.txt', entity.OrderType))
	pameters.append(('tradeDayData.txt', entity.TradeDay))


	SettingRepository = settingData.SettingRepository(pameters)
	print SettingRepository.toXml()

	# openOrderId, tran = transaction.createOpenSportTran()
	#print tran
	#closetran = transaction.createCloseSportTran(openOrderId)
	#print closetran


