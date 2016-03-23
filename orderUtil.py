import datetime
import datetimeHelper
import uuid

timedelta = datetime.timedelta(seconds = 5)
basetime = datetimeHelper.parse('2014-12-30 10:58:19')

def createTemplateDict(tradeOption,isOpen, isBuy,setPrice,lot):
	attrs = {
		'ID': str(uuid.uuid1()),
		'PriceIsQuote': 'false',
		'PriceTimestamp': datetimeHelper.toStandardStr(basetime - timedelta),
		'TradeOption': tradeOption,
		'IsOpen': isOpen,
		'IsBuy': isBuy,
		'SetPrice': setPrice,
		"SetPriceMaxMovePips": '0',
		"DQMaxMove": '10',
		"Lot": lot,
		"LotBalance": lot
	}
	return attrs
