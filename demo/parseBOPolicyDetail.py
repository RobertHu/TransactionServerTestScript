import re


if __name__  == '__main__':
	f = open('boPolicyDetails.txt','r')
	for line in f:
		m = re.split('\s+', line)
		print m



