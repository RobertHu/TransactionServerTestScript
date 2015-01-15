# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import uuid
import xmlHelper

def createXmlNode(item):
	id = str(uuid.uuid1())
	attrs = {
		'ID': id,
		'Code': 'BOBet1',
		'HitCount': '2'   #代表买涨跌，撞中的次数
	}
	xmlHelper.setAttrs(item,attrs)
	return id

