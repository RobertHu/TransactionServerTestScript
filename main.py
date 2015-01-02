# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import transaction

if __name__ == '__main__':
	tranXml = transaction.createSportTran()
	print tranXml
