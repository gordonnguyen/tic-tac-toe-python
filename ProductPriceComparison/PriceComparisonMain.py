from getEbayPrice import getProductPrice
import openpyxl



def main():
    watchlist_workbook = openpyxl.load_workbook('ProductWatchList.xlsx')
    sheet = watchlist_workbook.get_sheet_by_name('Sheet1')
    price, pro_name = getProductPrice(sheet['B2'].value)
    print('The price of \"'+pro_name+'\" on Ebay is',price)
    save_price_and_name(price, pro_name, sheet, watchlist_workbook)

def save_price_and_name(price, pro_name, sheet, watchlist_workbook):
    sheet['A2'].value = pro_name
    sheet['C2'].value = price
    watchlist_workbook.save('NewWatchList.xlsx')

main()
