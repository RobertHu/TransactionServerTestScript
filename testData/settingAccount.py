
import entity


class Account(entity.Entity):

	def __init__(self, header, cols):
		super(Account, self).__init__(header, cols)

	def toXml(self, parentNode):
		node = self.createNode('Account', parentNode)
		attrs = {
			'ID': self.getColumnValue('ID'),
			'TradePolicyID': self.getColumnValue('TradePolicyID'),
			'CustomerID': self.getColumnValue('CustomerID'),
			'CurrencyID': self.getColumnValue('CurrencyID'),
			'Code': self.getColumnValue('Code'),
			'Type': self.getColumnValue('Type'),
			'IsActive': self.getColumnValue('IsActive'),
			'IsTradingAllowed': self.getColumnValue('IsTradingAllowed'),
			'BeginTime': self.getColumnValue('BeginTime'),
			'EndTime': self.getColumnValue('EndTime'),
			'IsAutoClose': self.getColumnValue('IsAutoClose'),
			'IsMultiCurrency': self.getColumnValue('IsMultiCurrency')
		}
		self.setAttrsToNode(attrs, node)
		return node





