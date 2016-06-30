import os, requests, bs4

def shareprice(share):

    shareurl = 'http://www.asx.com.au/asx/markets/equityPrices.do?by=asxCodes&asxCodes='+str(share)

    sharehtml = requests.get(shareurl)

    sharesoup = bs4.BeautifulSoup(sharehtml.text,"html.parser")

    shareSoupSelect = sharesoup.select('.last')

    price = shareSoupSelect[0].getText()
    
    price = price.replace('\r','')
    
    price = price.replace('\t','')
    price = price.replace('\n','')
    
    
    return(price)
