# -*- coding: utf-8 -*-
import Test.orderUtil as orderUtil
import enum
import xmlHelper
import xml.etree.ElementTree as ET
from . import boBetType

def createOpenOrder(orderElement, betTypeId):
	attrs = orderUtil.createTemplateDict(enum.TradeOption.Better,enum.true, enum.true, '0.9110', '13')
	# betType = ET.SubElement(orderElement, 'BOBetType')
	# boBetTypeId = boBetType.createXmlNode(betType)
	attrs.update(DQMaxMove = '0')
	boAttrs = {
		'BOBetTypeID': betTypeId,
		'BOFrequency': '60', #时间
		'BOOdds': '2.5', #赔率
		'BOBetOption': '1'  #对应买涨还是买跌
	}
	attrs.update(boAttrs)
	xmlHelper.setAttrs(orderElement, attrs)




