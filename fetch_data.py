from libs.binance_client import Binance
from libs.database import Database

api = Binance(API_KEY='test', API_SECRET='test')

symbols = ['ETHUSDT', 'LTCUSDT', 'XLMUSDT', 'XMRUSDT', 'XEMUSDT']
intervals = ['1h', '1d']

database = Database()

for symbol in symbols:
    for interval in intervals:
        data = api.klines(symbol=symbol, interval=interval, limit=100)
        database.save_data(symbol, interval, data)
