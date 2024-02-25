import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pprint as pp
import json

url = "https://www.lazada.sg/products/salomon-men-x-ultra-4-mid-gtx-wide-hiking-shoes-black-magnet-pearl-blue-i2021923917-s11023092417.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Asolomon%252Bmen%252Bhiking%252Bshoes%253Bnid%253A2021923917%253Bsrc%253ALazadaMainSrp%253Brn%253Ad362b290d324380069b2669189a739d0%253Bregion%253Asg%253Bsku%253A2021923917_SGAMZ%253Bprice%253A260.1%253Bclient%253Adesktop%253Bsupplier_id%253A1145901015%253Bbiz_source%253Ahttps%253A%252F%252Fwww.lazada.sg%252F%253Bslot%253A3%253Butlog_bucket_id%253A469695%253Basc_category_id%253A4857%253Bitem_id%253A2021923917%253Bsku_id%253A11023092417%253Bshop_id%253A1286631&fastshipping=0&freeshipping=0&fs_ab=2&fuse_fs=&lang=en&location=Singapore&price=260.1&priceCompare=skuId%3A11023092417%3Bsource%3Alazada-search-voucher%3Bsn%3Ad362b290d324380069b2669189a739d0%3BoriginPrice%3A26010%3BvoucherPrice%3A26010%3BdisplayPrice%3A26010%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A1%3BbuyerId%3A0%3Btimestamp%3A1698972139752&ratingscore=3.0&request_id=d362b290d324380069b2669189a739d0&review=2&sale=6&search=1&source=search&spm=a2o42.searchlist.list.i41.9e1c731aramxjM&stock=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

def get_product_price():
    response = requests.get(url, headers=headers)
    text = response.text
    soup = BeautifulSoup(text, "lxml")
    
    search = soup.find('span', class_='pdp-price')
    print(search)


get_product_price()