from pprint import pprint
from bs4 import BeautifulSoup
import requests
from openpyxl import *
from datetime import date
import xlwings
# PATH = "/Users/matthew/Downloads/MarketJournal.xlsx"  # path to excel file
# PATH = "C:/Users/cmb56/Downloads/ECON_256/Market Journal _cmb171.xlsx"
PATH = "source/testFile.xlsx"

SHEET = "Template"  # excel sheet name

wb = load_workbook(PATH)
ws = wb[SHEET]


def get_val(URL, sec):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = str(soup.find(id=sec[2]))
    price = to_float(body[body.index(sec[0]) + sec[1]: body.index("<", body.index(sec[0]) + sec[1])])
    if sec[0] == "ltr":  # check for bonds
        print(str(price) + "%")
        price = price/100  # when excel converts a number to a percent it multiplies it by 100
    else:
        print(str(price))
    return price


def add_to(val, row, col):
    cell = ws.cell(row, col)
    cell.value = val


def get_row():
    today = date.today()
    i = 2
    while i < 59:
        evaluatedWB = xlwings.Book(PATH)
        evaluatedSheet = evaluatedWB.sheets[SHEET]
        if str(evaluatedSheet.range("A"+str(i)).value)[0:10] == str(today):
            evaluatedWB.close()  # closes excel sheet to prevent permission error when writing
            return i
        i += 1
    return -1


def to_float(price):
    while True:
        idx = price.find(',')
        if idx == -1:
            return float(price)
        else:
            price = price[0:idx] + price[idx+1:]


row = get_row()
col = 2
currentPrice = ("data-reactid=\"33\"", 18, 'quote-header-info')
index = currentPrice  # ("47", 4, 'quote-summary')
curr = currentPrice  # ("47", 4, 'quote-summary')
equity = currentPrice  # ("103", 5, 'quote-summary')
commodity = currentPrice  # ("57", 4, 'quote-summary')
crypto = currentPrice  # ("49", 4, 'quote-summary')
bond = ("ltr", 20, 'last_last')
debug = ("textLoc", 0, 'idName')


# Column B
print("EURO/USD:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/EURUSD=X', curr), row, col)  # EURO/USD Exchange Rate
col += 1  # Column C
print("STG/USD:", end=" ")
add_to((get_val('https://finance.yahoo.com/quote/GBPUSD=X', curr)), row, col)  # STG/USD Exchange Rate
col += 1  # Column D
print("USD/YEN:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/JPY=X', curr), row, col)  # USD/YEN Exchange Rate
col += 1  # Column E
print("USD/CNY:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/CNY=X', curr), row, col)  # USD/CNY Exchange Rate
col += 1  # Column F
print("Nikkei:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/^N225', index), row, col)  # Nikkei 225 Index
col += 1  # Column G
print("DAX:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/^GDAXI', index), row, col)  # DAX Performance Index
col += 1  # Column H
print("FTSE:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/^FTSE', index), row, col)  # FTSE 100 Index
col += 1  # Column I
print("DJIA:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/^DJI', index), row, col)  # Dow Jones Industrial Average
col += 1  # Column J
print("S&P:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/^GSPC', index), row, col)  # S&P 500 Index
col += 1  # Column K
print("Japan 10 Year:", end=" ")
add_to(get_val('https://www.investing.com/rates-bonds/japan-10-year-bond-yield', bond), row, col)  # Japan 10 Year Bond
col += 1  # Column L
print("Germany 10 Year:", end=" ")
add_to(get_val('https://www.investing.com/rates-bonds/germany-10-year-bond-yield', bond), row, col)  # Germany 10 Year Bond
col += 1  # Column M
print("UK 10 Year:", end=" ")
add_to(get_val('https://www.investing.com/rates-bonds/uk-10-year-bond-yield', bond), row, col)  # UK 10 Year Bond
col += 1  # Column N
print("US 10 Year:", end=" ")
add_to(get_val('https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield', bond), row, col)  # US 10 Year Bond
col += 1  # Column O
print("Gold:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/GC%3DF', commodity), row, col)  # Gold Futures
col += 1  # Column P
print("Brent Crude:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/BZ=F', commodity), row, col)  # Brent Crude Futures
col += 1  # Column Q
print("Bitcoin:", end=" ")
add_to(get_val('https://finance.yahoo.com/quote/BTC-USD', crypto), row, col)  # Bitcoin

wb.save(PATH)  # LEAVE THIS LINE!


