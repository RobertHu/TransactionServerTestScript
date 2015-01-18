# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import uuid
import xmlHelper

def createXmlNode(item):
	id = '7EF0B4D0-B003-4196-AE57-0ED955CF9A28'
	attrs = {
		'ID': id,
		'Code': 'BOBet01',
		'HitCount': '1'   #代表买涨跌，撞中的次数
	}
	xmlHelper.setAttrs(item,attrs)
	return id

