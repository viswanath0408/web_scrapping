from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen as uReq
import configparser
import requests
import sys


config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45', 'Compression': 'yes', 'CompressionLevel': '9'}


url = "https://cincinnati.craigslist.org/search/cto"

# res = requests.get(url)
# print (type(res))
#
# res_soup res_soup= bsoup(res, )


# opening the connectionn
uClient = uReq(url)
page_html = uClient.read()
print ("type is " +str(type(page_html)))

# page_soup = bsoup(page_html, 'html.parser')
page_soup = bsoup(page_html, 'lxml')
print (page_soup.title)

#closing the connection
# uClient.closining()