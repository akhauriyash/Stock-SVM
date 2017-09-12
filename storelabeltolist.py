from urllib import request
import requests
from bs4 import BeautifulSoup

tickcompile = r'tickset.txt'

def TickGrabber():
    fw = open(tickcompile,'w')
    url = r'https://www.nseindia.com/products/content/derivatives/equities/historical_fo.htm'
    sourcecode = requests.get(url)
    plaintext = sourcecode.text