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


if __name__ == '__main__':
	# openOrderId, xmlTran = transaction.createOpenSportTran()
	# print '-------------open tran----------'
	# print xmlTran
	# print '------------close tran ---------'
	# print transaction.createCloseSportTran(openOrderId)

	facade = boFacade.Facade()
	#print facade.generateBoPolicyDetailXml()
	print facade.generateTwoTranXml()
	#print facade.generateOneTranXml()


