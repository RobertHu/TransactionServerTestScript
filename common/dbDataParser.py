import re
import os


class Parser(object):

	def __init__(self, dirName):
		self.re =  re.compile('\t')
		self.dir = dirName


	def buildEntitiesCommon(self, fileName, entityCols, entityClass):
		for header, cols in self.loadFromFile(fileName):
			entityCols.append(entityClass(header, cols))

	def loadFromFile(self, fileName):
		filePath = os.path.join(self.dir, fileName)
		f = open(filePath, 'r')
		headerDict = self.parseHeaders(f.readline())
		for line in f:
			if line is not None:
				cols = self.re.split(line)
				yield (headerDict ,cols)

	def parseHeaders(self, headerLine):
		headerCols = self.re.split(headerLine)
		headerDict = dict()
		for n, v in enumerate(headerCols):
			headerDict[v.strip()] = n
		return headerDict



