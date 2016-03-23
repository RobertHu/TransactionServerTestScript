import re
import xml.etree.ElementTree as ET
from Test import xmlHelper


class PolicyDetailKey:

	def __init__(self, boPolicyId, boTypeId, frequency):
		self.boPolicyId = boPolicyId
		self.boTypeId = boTypeId
		self.frequency = frequency

	def __str__(self):
		return self.boPolicyId + '   ' + self.boTypeId + '   ' + self.frequency

	def __hash__(self):
		return hash((self.boPolicyId, self.boTypeId, self.frequency))

	def __eq__(self, other):
		return (self.boPolicyId, self.boTypeId, self.frequency) == (other.boPolicyId, other.boTypeId, other.frequency)


class Repository(object):
	_instance = None
	itemcount = 0

	def __new__(class_, *args, **kwargs):
		if not isinstance(class_._instance, class_):
			class_._instance = object.__new__(class_, *args, **kwargs)
		return class_._instance

	def getXml(self, root):
		for v in self.items.itervalues():
			item = ET.SubElement(root, 'BOPolicyDetail')
			self.buildPolicyDetail(v, item)



	def __init__(self):
		self.items = dict()
		self.load()

	def load(self):
		f = open(r'demo\boPolicyDetails.txt')
		for line in f:
			if line:
				cols = re.split('\s+',line)
				key = self.createKey(cols)
				self.add(key, cols)
				self.itemcount += 1
				
	def createKey(self, cols):
		policyId = cols[0]
		betTypeId = cols[1]
		frequency = cols[2]
		return PolicyDetailKey(policyId, betTypeId,frequency)

	def buildPolicyDetail(self, cols, item):
		attrs= {
			'BOPolicyID': cols[0],
			'BOBetTypeID': cols[1],
			'Frequency': cols[2],
			'MinBet': cols[3],
			'MaxBet': cols[4],
			'AutoAcceptMaxBet': cols[5],
			'StepBet': cols[6],
			'Odds': cols[7],
			'CommissionOpen': cols[8],
			'MinCommissionOpen': cols[9]
		}
		for k, v in attrs.items():
			item.set(k,v)


	def add(self, key, policyDetail):
		self.items[key] = policyDetail

	def get(self, key):
		return self.items.get(key)


















