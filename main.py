# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import transaction


if __name__ == '__main__':
	print transaction.createSportTran()
	print '------------close tran ---------'
	print transaction.createCloseSportTran()
