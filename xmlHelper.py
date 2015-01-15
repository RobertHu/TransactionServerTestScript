import xml.etree.ElementTree as ET

def setAttrs(element, attrs):
	for k, v in attrs.items():
		element.set(k,v)

def toXml(element):
	return ET.tostring(element, encoding='utf-8', method='xml')	
