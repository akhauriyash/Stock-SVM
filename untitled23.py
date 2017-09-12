# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:06:14 2016

@author: akhauri
"""

import bs4 as BeautifulSoup 
import requests
from urllib import request

url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17'

def getdat():
    sourcecode = requests.get(url).text
    asstring = sourcecode
    tablepart = asstring.split("<!-- Main Content End -->")[0]
    finaltable = tablepart.split('td height="8"')[1]
    lines = finaltable.split("\\n")
    desturl = r'csvfile.txt'
    fx = open(desturl, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close
    
getdat()