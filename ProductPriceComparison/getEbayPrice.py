import bs4, requests, openpyxl

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def getProductPrice(productUrl):
    res = requests.get(productUrl, HEADERS)
    res.raise_for_status()
    print('Connection Status:',res.status_code)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    if 'ebay.com' in productUrl:
        price_html_selector_list = ['#prcIsum', '#mm-saleDscPrc', '#prcIsum_bidPrice']
        product_name = soup.select('#itemTitle')
        for selector in price_html_selector_list:
            product_price = soup.select(selector)
            if product_price != '':
                break

        #if product_price == []:
        #    product_price = 'No product_price available'
        print(product_price)
        print(product_name[0].text.replace('Details about', '').strip())

        return product_price[0].text.strip(), product_name[0].text.replace('Details about', '').strip()

        #return product_price[0].text.strip(), product_name[0].text.replace('Details about', '').strip()

'''
        if product_price == []:
            product_price = soup.select('#mm-saleDscPrc')
'''
'''
    elif 'camelcamelcamel.com' in productUrl:
        product_price = soup.select('#content > div:nth-child(2) > div.column.column-block.small-12.medium-3.medium-text-right > div:nth-child(1) > div.column.small-8.medium-12 > p > span > span')
        return product_price
'''


#productUrl = input("Enter Drop\'s product URL: ")

#if productUrl == '':
#    productUrl = input(pyperclip.paste)

#product_price = getProductPrice(productUrl)
#print('The product_price on Ebay is',product_price)