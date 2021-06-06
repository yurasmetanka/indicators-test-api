import sqlite3
import json

class Database:
    def __init__(self, filename = 'data.db'):
        self.connection = sqlite3.connect('tmp/' + filename)
        self.__createTable()

    def __del__(self):
        self.connection.close()

    def __createTable(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS klines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                interval TEXT,
                time_open INTEGER,
                price_open REAL,
                price_high REAL,
                price_low REAL,
                price_close REAL,
                volume REAL,
                time_close INTEGER,
                quote_asset_volume REAL,
                trades_number INTEGER,
                taker_base REAL,
                taker_quote REAL
            );
        ''')
        self.connection.commit()
        cursor.close()

    def save_data(self, symbol, interval, klines):
        cursor = self.connection.cursor()

        for kline in klines:
            self.__add_kline(cursor, symbol, interval, kline)

        cursor.close()

    def __add_kline(self, cursor, symbol, interval, kline):
        cursor.execute(
            '''
                INSERT INTO klines (
                    symbol,
                    interval,
                    time_open,
                    price_open,
                    price_high,
                    price_low,
                    price_close,
                    volume,
                    time_close,
                    quote_asset_volume,
                    trades_number,
                    taker_base,
                    taker_quote
                ) 
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);
            ''',
            (
                symbol,
                interval,
                kline[0],
                kline[1],
                kline[2],
                kline[3],
                kline[4],
                kline[5],
                kline[6],
                kline[7],
                kline[8],
                kline[9],
                kline[10],
            )
        )
        self.connection.commit()

    def get_data(self, symbol, interval, limit=100):
        cursor = self.connection.cursor()
        cursor.execute(
            '''
                SELECT
                    time_open,
                    price_open,
                    price_high,
                    price_low,
                    price_close
                FROM klines
                WHERE
                    symbol=? AND
                    interval=?
                ORDER BY time_open ASC
                LIMIT ?;
            ''',
            [symbol, interval, limit]
        )
        klines = cursor.fetchall()
        self.connection.commit()
        cursor.close()

        return klines
