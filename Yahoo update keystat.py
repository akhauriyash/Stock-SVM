# -*- coding: utf-8 -*-
import urllib.request
import os

path = r"C:\Users\akhauri\PycharmProjects\Projectattempts\intraQuarter"
fwdpath = r"C:\Users\akhauri\ML stk analysis\stkfwd"

def Check_Yahoo():
    fwdpath = r"C:\Users\akhauri\ML stk analysis\stkfwd"
    statspath = path + '\_KeyStats'
    ticklist = []
    stock_list = [x[0] for x in os.walk(statspath)]
    fl = os.listdir(fwdpath)
    for n in fl:
        n = n.replace(r"C:\Users\akhauri\ML stk analysis\stkfwd", "")
        n = n.replace(r".html", "")
        ticklist.append(n.upper())
    print(ticklist)


    for e in stock_list:
        e = e.replace(r"C:\Users\akhauri\PycharmProjects\Projectattempts\intraQuarter\_KeyStats", "")
        e = e.replace("\\", "")
        e = e.upper()
        if e in ticklist: 
            print("passing ", e)
            pass
        else:
            try:
                link = "https://in.finance.yahoo.com/q/ks?s=" + e
                response = urllib.request.urlopen(link).read()
                print("DOING: " + str(e))
                save = r"C:\Users\akhauri\ML stk analysis\stkfwd"+ "\\" + str(e) + ".html"
                store = open(save, "w")
                store.write(str(response))
                store.close()
                
            except Exception as e:
                print("OHNO" + str(e))

        

Check_Yahoo()