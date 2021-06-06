from flask import Flask, request, abort
from libs.database import Database
import pandas as pd
import pandas_ta as ta
import json

app = Flask(__name__)

@app.route("/indicator")
def get_indicator():
    indicator = request.args.get('indicator')
    period = request.args.get('period', type=int)
    symbol = request.args.get('symbol')
    interval = request.args.get('interval', default='1d')
    candle = 99 - request.args.get('candle', default=0, type=int)

    if (
        not indicator
        or not period
        or not symbol
    ):
        abort(400, 'You should provide all of the folloving required fields with request: "indicator", "period", "symbol".')

    if indicator not in ['EMA', 'RSI']:
        abort(400, 'Invalid indicator. Supported indicators: "EMA", "RSI"')

    if symbol not in ['ETHUSDT', 'LTCUSDT', 'XLMUSDT', 'XMRUSDT', 'XEMUSDT']:
        abort(400, 'Invalid symbol. Supported symbols: "ETHUSDT", "LTCUSDT", "XLMUSDT", "XMRUSDT", "XEMUSDT"')

    if interval not in ['1d', '1h']:
        abort(400, 'Invalid interval. Supported intervals: "1d", "1h"')

    database = Database()
    klines = database.get_data(symbol, interval)
    data_frame = pd.DataFrame.from_records(klines, columns=['timestamp', 'open', 'high', 'low', 'close'])

    if indicator == 'EMA':
        indicator_data = ta.ema(data_frame['close'], length=period).to_dict()
    elif indicator == 'RSI':
        indicator_data = ta.rsi(data_frame['close'], length=period).to_dict()

    return json.dumps({
        'timestamp': klines[candle][0],
        'open': klines[candle][1],
        'high': klines[candle][2],
        'low': klines[candle][3],
        'close': klines[candle][4],
        'indicator': indicator_data[candle],
    })
