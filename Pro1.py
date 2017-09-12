import pandas as pd
import time
import os
from datetime import datetime
from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")
import re


path = r"C:\Users\akhauri\PyCharmsecondary\intraQuarter"


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    #  print(stock_list)
    df = pd.DataFrame(columns=['Date',
                               'Unix',
                               'Ticker',
                               'DE Ratio',
                               'Price',
                               'stock_p_change',
                               'SP500',
                               'SP500_p_change',
                               'Difference'])

    sp500_df = pd.DataFrame.from_csv("YAHOO-INDEX_GSPC.csv")

    ticker_list =[]


    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[5]
        ticker_list.append(ticker)

        start_stk_val=False
        start_sp500_val=False


        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                #  print(date_stamp, unix_time)
                full_file_path = each_dir+'/'+file
                #  print(full_file_path)
                source = open(full_file_path, 'r').read()
                #  print(source)
                try:
                    value = float(source.split('Total Debt/Equity (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adjusted Close"])
                    except:
                        sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adjusted Close"])
                    stockprice = float(source.split('</small><big><b>')[1].split('</b></big>&nb')[0])
                    #  print(stockprice)

                    if not start_stk_val:
                        start_stk_val = stockprice
                    if not start_sp500_val:
                        start_sp500_val = sp500_value
                    stock_p_change = ((stockprice-start_stk_val)/start_stk_val)*100
                    stock_sp500_change = ((sp500_value-start_sp500_val)/start_sp500_val)*100


                    df = df.append({'Date': date_stamp,
                                    'Unix': unix_time,
                                    'Ticker': ticker,
                                    'DE Ratio': value,
                                    'Price': stockprice,
                                    'stock_p_change': stock_p_change,
                                    'SP500': sp500_value,
                                    'SP500_p_change': stock_sp500_change,
                                    'Difference': stock_p_change-stock_sp500_change}, ignore_index=True)
                except Exception as e:
                    pass

    for ticker in ticker_list:
        try:
            plot_df = df[(df['Ticker'] == ticker)]
            plot_df = plot_df.set_index(['Date'])
            plot_df['Difference'].plot(label=ticker)
            plt.legend()
        except:
            pass
    plt.show()



Key_Stats()
