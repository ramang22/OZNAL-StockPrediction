import numpy as np
import pandas as pd
import requests
import io
import yfinance as yf
import datetime
import time

class OZNAL_UTIL:

    def downloadNASDAQHistoricalStockData(self, symbol, start, end):
        stock_final = pd.DataFrame()
        try:
            stock = []
            stock = yf.download(symbol,start=start, end=end, progress=False)
            
            if len(stock) == 0:
                None
            else:
                stock['symbol']=symbol
                stock_final = stock_final.append(stock,sort=False)
        except Exception:
            None
        return stock_final

    def getStockSymbols(self, onlySymbols=True):
        # url="https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv"
        # s = requests.get(url).content
        # companies = pd.read_csv(io.StringIO(s.decode('utf-8')))
        url="http://ftp.nasdaqtrader.com/dynamic/SymDir/nasdaqtraded.txt"
        s = requests.get(url).content
        #companies = pd.read_csv(io.StringIO(s.decode('utf-8')))
        read_file = pd.read_csv(url,delimiter="|")
        if onlySymbols:
            return read_file['Symbol'].tolist()
        else:
            return companies 

    def getCryptoSymbols(self):
        return [
            'BTC',
            'ETH',
            'XMR',
            'XRP',
            'LTC',
            'BNB',
            'USDT',
            'DOT',
            'ADA',
            'UNI',
            'LTC',
            'XLM',
            'LINK',
            'BCH',
            'THETA',
            'FIL',
            'USDC',
            'DOGE',
            'WBTC',
            'VET',
            'SOL',
            'EOS',
            'MIOTA',
            'LUNA',
            'BTT'
            'XTZ',
            'ATOM',
            'AVAX',
            'ALGO'
        ]   


