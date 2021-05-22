import numpy as np
import pandas as pd
import yfinance as yf
import datetime
import time
import re
import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk.stem import WordNetLemmatizer 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import SQLContext
import pyspark
import sys

import requests
import io
import yfinance as yf

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

sid = SentimentIntensityAnalyzer()
OZNAL = OZNAL_UTIL()
lemmatizer = WordNetLemmatizer()
symbols = OZNAL.getStockSymbols() + OZNAL.getCryptoSymbols()


def getSymbols(text):
    extra_symbols = {
        'bitcoin':'BTC',
        'ethereum':'ETH',
        'dogecoin':'DOGE',
        'ripple':'XRP',
        'monero':'XMR',
        'litecoin':'LTC',
        'cardano':'ADA'
    }
    if text is np.nan:
        return []
    try:
        results = re.findall(r'[a-zA-Z0-9]+', text)
    except:
        return []

    hits = []
    for word in results:
        if word in symbols:
            hits.append(word)
        if word.lower() in extra_symbols.keys():
            hits.append(extra_symbols[word.lower()])

    return list(set(hits))

def processRow(row):
    row_dict = row.asDict()
    text = row_dict['body']
    text = re.sub(r'[,"]', ' ', text) if text else None
    
    sentiment = 0
    if text:
        sentiment = sid.polarity_scores(text)['compound']
        
    row_dict['sentiment'] = sentiment
    row_dict['symbols'] = getSymbols(text)
    row_dict['body'] = text

    return Row(**row_dict)


def processPostRow(row):
    row_dict = row.asDict()
    text = row_dict['selftext']
    text = re.sub(r'[,"]', ' ', text) if text else None
    title = row_dict['title']
    title = re.sub(r'[,"]', ' ', title) if title else None
    
    sentiment = 0
    if text:
        sentiment = sid.polarity_scores(text)['compound']
    elif title:
        sentiment = sid.polarity_scores(title)['compound']
    
    row_dict['sentiment'] = sentiment
    row_dict['symbols'] = getSymbols(text) + getSymbols(title)
    row_dict['selftext'] = text
    row_dict['title'] = title

    return Row(**row_dict)

if len(sys.argv) != 3:
    raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

inputUri=sys.argv[1]
outputUri=sys.argv[2]

spark = SparkSession.builder.appName("WSBAPP").getOrCreate()

data = (
    spark
        .read
        .format("com.databricks.spark.csv")
        .option("quote", "\"")
        .option("escape", "\"")
        .option("multiLine", "true")
        .load(sys.argv[1], format="com.databricks.spark.csv", inferSchema="true", header="true")
)

modified = (
    data
        .rdd
        .map(lambda row: processRow(row))
        .filter(lambda row: row['symbols'])    
)

df = modified.toDF().toPandas()

df.to_csv(sys.argv[2])