import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import time


'''
Auto add to cart program for BestBuy:

https://www.bestbuy.com/site/apple-watch-se-gps-44mm-gold-aluminum-case-with-pink-sand-sport-band-gold/6215917.p?skuId=6215917

1. Use URL to check for availibity.
2a. If its available - add to cart.
2b. If not - recheck every 5 seconds.
3. Sign in if possible.
4. Check out.
'''
RETRY_PERIOD = 5
SUCCESS_STATUS = 200

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
product_url = 'https://www.bestbuy.com/site/apple-watch-se-gps-40mm-silver-aluminum-case-with-white-sport-band-silver/6215915.p?skuId=6215915'
selector = '#fulfillment-add-to-cart-button-27998261 > div > div > div > button'

def main():
    getProduct()

def getProduct():
    page = requests.get(product_url, headers)
    page.raise_for_status()
    if page.status_code == SUCCESS_STATUS:
        print('Connection succesful!!!')
        page_html = bs.BeatifulSoup(page.text, 'html.parser')
        add_to_cart_btn = page_html.select(selector)
        print(add_to_cart_btn)

    else:
        print('Connection failed! Retrying in', RETRY_PERIOD, 'seconds.')

main()