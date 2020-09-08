currentPrice = ("data-reactid=\"33\"", 18, 'quote-header-info')
index = currentPrice  # ("47", 4, 'quote-summary')
curr = currentPrice  # ("47", 4, 'quote-summary')
equity = currentPrice  # ("103", 5, 'quote-summary')
commodity = currentPrice  # ("57", 4, 'quote-summary')
crypto = currentPrice  # ("49", 4, 'quote-summary')
bond = ("ltr", 20, 'last_last')
debug = ("textLoc", 0, 'idName')

EURO_USD = ('https://finance.yahoo.com/quote/EURUSD=X', curr)
STG_USD = ('https://finance.yahoo.com/quote/GBPUSD=X', curr)
USD_YEN = ('https://finance.yahoo.com/quote/JPY=X', curr)
USD_CNY = ('https://finance.yahoo.com/quote/CNY=X', curr)
NIKKEI = ('https://finance.yahoo.com/quote/^N225', index)
DAX = ('https://finance.yahoo.com/quote/^GDAXI', index)
FTSE = ('https://finance.yahoo.com/quote/^FTSE', index)
DJIA = ('https://finance.yahoo.com/quote/^DJI', index)
SNP = ('https://finance.yahoo.com/quote/^GSPC', index)
JAPAN10YR = ('https://www.investing.com/rates-bonds/japan-10-year-bond-yield', bond)
GERMANY10YR = ('https://www.investing.com/rates-bonds/germany-10-year-bond-yield', bond)
UK10YR = ('https://www.investing.com/rates-bonds/uk-10-year-bond-yield', bond)
US10YR = ('https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield', bond)
GOLD = ('https://finance.yahoo.com/quote/GC%3DF', commodity)
BRENT_CRUDE = ('https://finance.yahoo.com/quote/BZ=F', commodity)
BITCOIN = ('https://finance.yahoo.com/quote/BTC-USD', crypto)

asset_info = {"EURO/USD": EURO_USD, "STG/USD": STG_USD, "USD/YEN": USD_YEN,  "USD/CNY": USD_CNY, "NIKKEI": NIKKEI,
              "DAX": DAX, "FTSE": FTSE, "DJIA": DJIA, "S&P": SNP, "JAPAN10YR": JAPAN10YR, "GERMANY10YR": GERMANY10YR,
              "UK10YR": UK10YR, "US10YR": US10YR, "GOLD": GOLD, "BRENT_CRUDE": BRENT_CRUDE, "BITCOIN": BITCOIN}


def get_asset_info(name):
    for assetName, assetInfo in asset_info.items():
        if assetName == name:
            return assetInfo
    print(name + " does not exist in this database")

