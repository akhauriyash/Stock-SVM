#    -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 14:27:39 2016

@author: akhauri
"""

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


path = r"C:\Users\akhauri\PycharmProjects\Projectattempts\intraQuarter"


def Key_Stats(gather=["Total Debt/Equity",
                      'Trailing P/E',
                      'Price/Sales',
                      'Price/Book',
                      'Profit Margin',
                      'Operating Margin',
                      'Return on Assets',
                      'Return on Equity',
                      'Revenue Per Share',
                      'Market Cap',
                        'Enterprise Value',
                        'Forward P/E',
                        'PEG Ratio',
                        'Enterprise Value/Revenue',
                        'Enterprise Value/EBITDA',
                        'Revenue',
                        'Gross Profit',
                        'EBITDA',
                        'Net Income Avl to Common ',
                        'Diluted EPS',
                        'Earnings Growth',
                        'Revenue Growth',
                        'Total Cash',
                        'Total Cash Per Share',
                        'Total Debt',
                        'Current Ratio',
                        'Book Value Per Share',
                        'Cash Flow',
                        'Beta',
                        'Held by Insiders',
                        'Held by Institutions',
                        'Shares Short (as of',
                        'Short Ratio',
                        'Short % of Float',
                        'Shares Short (prior ']):
    statspath = path+'\_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    #  print(stock_list)
    df = pd.DataFrame(columns = ['Date',
                                 'Unix',
                                 'Ticker',
                                 'Price',
                                 'stock_p_change',
                                 'SP500',
                                 'sp500_p_change',
                                 'Difference',
                                 'DE Ratio',
                                 'Trailing P/E',
                                 'Price/Sales',
                                 'Price/Book',
                                 'Profit Margin',
                                 'Operating Margin',
                                 'Return on Assets',
                                 'Return on Equity',
                                 'Revenue Per Share',
                                 'Market Cap',
                                 'Enterprise Value',
                                 'Forward P/E',
                                 'PEG Ratio',
                                 'Enterprise Value/Revenue',
                                 'Enterprise Value/EBITDA',
                                 'Revenue',
                                 'Gross Profit',
                                 'EBITDA',
                                 'Net Income Avl to Common ',
                                 'Diluted EPS',
                                 'Earnings Growth',
                                 'Revenue Growth',
                                 'Total Cash',
                                 'Total Cash Per Share',
                                 'Total Debt',
                                 'Current Ratio',
                                 'Book Value Per Share',
                                 'Cash Flow',
                                 'Beta',
                                 'Held by Insiders',
                                 'Held by Institutions',
                                 'Shares Short (as of',
                                 'Short Ratio',
                                 'Short % of Float',
                                 'Shares Short (prior ',
                                 'Status'])

                                 
    sp500_df = pd.DataFrame.from_csv("YAHOO-INDEX_GSPC.csv")
    stock_df = pd.DataFrame.from_csv("stockprices.csv")

    ticker_list =[]



    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[-1]
        print(ticker)
        ticker_list.append(ticker)

        #start_stk_val=False
        #start_sp500_val=False


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
                    value_list = []


                    for each_data in gather:
                        try:
                            regex = re.escape(each_data) + r'.*?(\d{1,8}\.\d{1,8}M?B?|N/A)%?</td>'
                            value = re.search(regex, source)
                            value = value.group(1)

                            if "B" in value:
                                value = float(value.replace("B", ""))*1000000000
                            elif "M" in value:
                                value = float(value.replace("M", ""))*1000000
                            value_list.append(value)

                            #  value = float(source.split('Total Debt/Equity (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                        except Exception as e:
                            value = "N/A"
                            value_list.append(value)
                            # try:
                            #   value = float(source.split('Total Debt/Equity (mrq):</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
                            # except Exception as e:
                            #     pass
                        try:
                            sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                            row = sp500_df[(sp500_df.index == sp500_date)]
                            sp500_value = float(row["Adjusted Close"])
                        except:
                            sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                            row = sp500_df[(sp500_df.index == sp500_date)]
                            sp500_value = float(row["Adjusted Close"])
                            
                        one_yr_ltr = int(unix_time + 31536000)
                        
                        try: 
                            sp500_1y = datetime.fromtimestamp(one_yr_ltr).strftime('%Y-%m-%d')
                            row = sp500_df[(sp500_df.index == sp500_1y)]
                            sp500_1y_value = float(row["Adjusted Close"])
                            
                        except Exception as e:

                            try:
                                sp500_1y = datetime.fromtimestamp(one_yr_ltr-259200).strftime('%Y-%m-%d')
                                row = sp500_df[(sp500_df.index == sp500_1y)]
                                sp500_1y_value = float(row["Adjusted Close"])                                
                            except Exception as e:
                                print("SP500 exceptionj", str(e))
                                
                        try: 
                            stkpr_1y = datetime.fromtimestamp(one_yr_ltr).strftime('%Y-%m-%d')
                            row = stock_df[(stock_df.index == stkpr_1y)][ticker.upper()]
                            stkpr_1y_value = round(float(row),2)
                            
                        except Exception as e:

                            try:
                                stkpr_1y = datetime.fromtimestamp(one_yr_ltr-259200).strftime('%Y-%m-%d')
                                row = stock_df[(stock_df.index == stkpr_1y)][ticker.upper()]
                                stkpr_1y_value = round(float(row),2)  
                            except Exception as e:
                                print("stkprice 1yltr", str(e))
                                
                                
                        try: 
                            stkpr = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                            row = stock_df[(stock_df.index == stkpr)][ticker.upper()]
                            stkpr_value = round(float(row),2)
                            
                        except Exception as e:

                            try:
                                stkpr = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                                row = stock_df[(stock_df.index == stkpr)][ticker.upper()]
                                stkpr_value = round(float(row),2)  
                            except Exception as e:
                                print("stkprice 1yltr", str(e))
                        
                                
                    stock_p_change = round((((stkpr_1y_value - stkpr_value)/stkpr_value)*100),2)
                    stock_sp500_change = round((((sp500_1y_value - sp500_value)/sp500_value)*100),2)

                    difference = stock_p_change-stock_sp500_change

                    if difference > 0:
                        status = 'outperform'
                    else:
                        status = 'underperform'

                    if value_list.count("N/A")> 15:
                        pass
                    else:

                        df = df.append({'Date':date_stamp,
                                                'Unix':unix_time,
                                                'Ticker':ticker,
                                                'Price':stkpr_value,
                                                'stock_p_change':stock_p_change,
                                                'SP500':sp500_value,
                                                'sp500_p_change':stock_sp500_change,
                                                'Difference':difference,
                                                'DE Ratio':value_list[0],
                                                'Trailing P/E':value_list[1],
                                                'Price/Sales':value_list[2],
                                                'Price/Book':value_list[3],
                                                'Profit Margin':value_list[4],
                                                'Operating Margin':value_list[5],
                                                'Return on Assets':value_list[6],
                                                'Return on Equity':value_list[7],
                                                'Revenue Per Share':value_list[8],
                                                'Market Cap':value_list[9],
                                                 'Enterprise Value':value_list[10],
                                                 'Forward P/E':value_list[11],
                                                 'PEG Ratio':value_list[12],
                                                 'Enterprise Value/Revenue':value_list[13],
                                                 'Enterprise Value/EBITDA':value_list[14],
                                                 'Revenue':value_list[15],
                                                 'Gross Profit':value_list[16],
                                                 'EBITDA':value_list[17],
                                                 'Net Income Avl to Common ':value_list[18],
                                                 'Diluted EPS':value_list[19],
                                                 'Earnings Growth':value_list[20],
                                                 'Revenue Growth':value_list[21],
                                                 'Total Cash':value_list[22],
                                                 'Total Cash Per Share':value_list[23],
                                                 'Total Debt':value_list[24],
                                                 'Current Ratio':value_list[25],
                                                 'Book Value Per Share':value_list[26],
                                                 'Cash Flow':value_list[27],
                                                 'Beta':value_list[28],
                                                 'Held by Insiders':value_list[29],
                                                 'Held by Institutions':value_list[30],
                                                 'Shares Short (as of':value_list[31],
                                                 'Short Ratio':value_list[32],
                                                 'Short % of Float':value_list[33],
                                                 'Shares Short (prior) ':value_list[34],
                                                'Status':status},
                                               ignore_index=True)
                except Exception as e:
                    pass



    #
    # for ticker in ticker_list144:
    #     try:
    #         plot_df = df[(df['Ticker'] == ticker)]
    #         plot_df = plot_df.set_index(['Date'])
    #
    #         if plot_df['Status'][-1] == "underperform":
    #             color = 'r'
    #         else:
    #             color = 'g'
    #
    #         plot_df['Difference'].plot(label=ticker, color = color)
    #
    #         #plt.legend()
    #     except:
    #         print("exception2" + ticker)
    # plt.show()
    #
    df.to_csv("key_stats_acc_perf_WITH_NA.csv")


Key_Stats()
