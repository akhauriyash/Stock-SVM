#  -*- coding: utf-8 -*-

import requests
import csv

with open('ListOfScrips.csv', newline='') as csvfile:
    datdict = csv.DictReader(csvfile, delimiter=',')

    currow = 0
    numlist = []

    for row in datdict:
        currow += 1
        if currow == 0:
            continue

        numlist.append(row["Security Id"])

for item in numlist:
    store = 'stkdat'+item+'.html'
    fwtemp = open(store, "w")
    url = 'https://in.finance.yahoo.com/q/ks?s='+item+'.NS'
    def spider(urls):
        sourcecode = requests.get(url)
        plaintext = sourcecode.text.encode("utf-8")
        fwtemp.write(str(plaintext))
        fwtemp.close()
    spider(url)