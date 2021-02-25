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
        pro_name = soup.select('#itemTitle')
        elems = soup.select('#prcIsum')
        if elems == []:
            elems = soup.select('#mm-saleDscPrc')
        return elems[0].text.strip(), pro_name[0].text.replace('Details about', '').strip()
    elif 'camelcamelcamel.com' in productUrl:
        elems = soup.select('#content > div:nth-child(2) > div.column.column-block.small-12.medium-3.medium-text-right > div:nth-child(1) > div.column.small-8.medium-12 > p > span > span')
        return elems

def print_example():
    print("SUCCESS")
#productUrl = input("Enter Drop\'s product URL: ")

#if productUrl == '':
#    productUrl = input(pyperclip.paste)

#price = getProductPrice(productUrl)
#print('The price on Ebay is',price)