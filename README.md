# Prerequisites
1. Install all necessary dependencies:
```
$ python -m pip install -r requirements.txt
```

2. Fill the db with data:
```
$ python fetch_data.py
```
3. Run the server:
```
flask run
```

# Api docs
## Indicator

Get indicator for fetched data

```
GET /indicator
```

http://127.0.0.1:5000/indicator?indicator=EMA&period=10&symbol=ETHUSDT


### Parameters

| Name     | Type       | Required | Default value | Description                           |
|----------|------------|----------|---------------|---------------------------------------|
| indicator | `String` | ✅ | ❌ | Supported indicators: "EMA", "RSI" |
| period | `Integer` | ✅ | ❌ | Period of the indicator |
| symbol | `String` | ✅ | ❌ | Supported symbols: "ETHUSDT", "LTCUSDT", "XLMUSDT", "XMRUSDT", "XEMUSDT" |
| interval | `String` | ❌ | "1d" | Supported intervals: "1d", "1h" |
| candle | `Integer` | ❌ | 0 | Candle number (0 - current, 1 - previous, etc.) |

### Success response

#### Success response - `200 - Everything ok`

Json object with following fields:

| Name     | Type       | Description                           |
|----------|------------|---------------------------------------|
| timestamp | `Integer` | Candle timestamp |
| open | `Integer` | Candle open price |
| high | `Integer` | Candle high price |
| low | `Integer` | Candle low price |
| close | `Integer` | Candle close |
| indicator | `Integer` | Candle indicator |

Example response:
```
{
  "timestamp": 1622937600000,
  "open": 2627.63,
  "high": 2745.0,
  "low": 2614.0,
  "close": 2668.16,
  "indicator": 2666.8311334881723
}
```

### Error response

#### Error response - `400`

Missing required field or invalid field value.
