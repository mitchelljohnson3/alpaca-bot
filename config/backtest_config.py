#fetch config
#----------------------------------------------------------------------
#Symbols to analyze, separated by commas
SYMBOLS_TO_TEST = ["AAPL", "TSLA"]
#YEAR-MONTH-DAY Format
DATE_START = "2020-01-01"
DATE_END = "2021-01-01"
#1-10000 [DO NOT CHANGE]
LIMIT = 10000
#1Min, 1Hour, 1Day
TIME_FRAME = "1Day"
#----------------------------------------------------------------------

#analysis config
#----------------------------------------------------------------------
# should candlestick or simplified chart be shown? True = candle, False = simple
CANDLE_OR_SIMPLE = False
# indicators in this list wont be included in the data files
DO_NOT_INCLUDE_IN_DATA = ["EMA12", "EMA26"]
# indicators in this list wont be included in the file name, but will still be in the data files
DO_NOT_INCLUDE_IN_FILENAME = ["EMA12", "EMA26", "MACDSig", "MACDHist", "Split"]
# indicators settings
SMA = []
EMA = []
RSI = True
RSI_PERIOD = 14
MACD = True
#----------------------------------------------------------------------

#backtest config
#----------------------------------------------------------------------

#----------------------------------------------------------------------