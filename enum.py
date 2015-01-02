true = 'true'
false = 'false'


class TransactionType:
    Single = '0'
    Pair = '1'
    OneCancelOther = '2'
    #Mapping,
    MultipleClose = '4'
    Assign = '100' #AssigningOrderID == SourceOrderID (id of the order been assigned from)

class TransactionSubType:
    NoneItem = '0'
    Amend = '1' #AssigningOrderID == AmendedOrderId (id of the order been amended)
    IfDone = '2' #AssigningOrderID == IfOrderId (id of the order used as condition)
    Match = '3'  #AssigningOrderID == SourceOrderID (id of the order been split from) NOTE: TransactionType===Single
    Assign = '4' #AssigningOrderID == AssigningOrderID (id of the order been assigned from) //NotImplemented
    Mapping = '5'


class OrderType:
    SpotTrade = '0'
    Limit = '1'
    Market = '2'
    MarketOnOpen = '3'
    MarketOnClose = '4'
    OneCancelOther = '5'
    Risk = '6'
    Stop = '7'
    MultipleClose = '8'
    MarketToLimit = '9'
    StopLimit = '10' 


class TradeOption:
    Invalid = '0'
    Stop = '1'
    Better = '2'