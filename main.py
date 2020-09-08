from pprint import pprint
from bs4 import BeautifulSoup
import requests
from openpyxl import *
from datetime import date
import xlwings
import config
# PATH = "/Users/matthew/Downloads/MarketJournal.xlsx"  # path to excel file
# PATH = "C:/Users/cmb56/Downloads/ECON_256/Market Journal _cmb171.xlsx"
PATH = "source/testFile.xlsx"

SHEET = "Template"  # excel sheet name

# To add to what is collected, create an ID for asset and add to asset_info in config
# then add it to INPUT_ORDER below

# order that data will be input into spreadsheet, starting with column B
# leave empty strings to start at columns beyond B
INPUT_ORDER = ("EURO/USD", "STG/USD", "USD/YEN",  "USD/CNY", "NIKKEI",
               "DAX", "FTSE", "DJIA", "S&P", "JAPAN10YR", "GERMANY10YR",
               "UK10YR", "US10YR", "GOLD", "BRENT_CRUDE", "BITCOIN")


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

for asset in INPUT_ORDER:
    print(asset, end=" ")
    assetInfo = config.get_asset_info(asset)
    add_to(get_val(assetInfo[0], assetInfo[1]), row, col)
    col +=1
notes = input("Please enter Daily Notes (Hit enter to leave blank): ")
add_to(notes, row, col)
wb.save(PATH)


