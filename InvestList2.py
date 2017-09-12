import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import preprocessing
import pandas as pd
from matplotlib import style
import statistics
import warnings
style.use("ggplot")

FEATURES = (['DE Ratio',
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
             'Shares Short (prior) '])


def BuildDataSet():
    data_df = pd.DataFrame.from_csv("key_stats_acc_perf_NO_NA_enhanced.csv")
    warnings.filterwarnings("ignore", category=DeprecationWarning)   

    # data_df = data_df[:100]
    data_df = data_df.reindex(np.random.permutation(data_df.index))
    data_df = data_df.replace("NaN", 0).replace("N/A", 0)

    X = np.array(data_df[FEATURES].values)  # .tolist())  # takes features, converts to values, then to python list

    y = (data_df["Status"]
         .replace("underperform", 0)
         .replace("outperform", 1)
         .values.tolist())


    X = preprocessing.scale(X)
    Z = np.array(data_df[["stock_p_change", "sp500_p_change"]])

    return X, y, Z


def Analysis():
    test_size = 1
    invest_amt = 10000
    total_invests = 0
    if_market = 0
    if_strat = 0
    X, y, Z = BuildDataSet()
    print(len(X))

    clf = svm.SVC(kernel="linear", C=1.0)

    clf.fit(X[:-test_size], y[:-test_size])

    correctcount = 0

    for x in range(1, test_size + 1):
        if clf.predict(X[-x])[0] == y[-x]:
            correctcount += 1

        if clf.predict(X[-x])[0] == 1:
            invest_return = invest_amt + (invest_amt * (Z[-x][0] / 100))
            market_return = invest_amt + (invest_amt * (Z[-x][1] / 100))
            total_invests += 1

            if_market += market_return
            if_strat += invest_return

#    print("Accuracy:", (correctcount / test_size) * 100.00)
#    print("Total trades: ", total_invests)
#    print("Amount invested: ", total_invests*10000)
#    print("ending with Strategy", if_strat)
#    print("ending with market:", if_market)

#    compared = ((if_strat - if_market) / if_market) * 100.0
#    do_nothing = total_invests * invest_amt
#    avg_market = ((if_market - do_nothing)/do_nothing) * 100.0
#    avg_strat = ((if_strat - do_nothing)/do_nothing) * 100.0
    
#    print("Average investment return: ", str(avg_strat)+ "%") 
#    print("Average Market return: ", str(avg_market) + "%")
#    print("compared to market, we earn", str(compared) + "% more")
    data_df = pd.DataFrame.from_csv("key_stats_acc_perf_NO_NA_enhanced.csv")
    data_df = data_df.replace("N/A", 0).replace("NaN", 0)
    X = np.array(data_df[FEATURES].values)
    X = preprocessing.scale(X)
    Z = data_df["Ticker"].values.tolist()
    invest_list = []

    for i in range(len(X)):
        p = clf.predict(X[i])[0]
        if p == 1:
            if Z[i] in invest_list:
                pass
            else:
                invest_list.append(Z[i])
    print(len(invest_list))
    print(invest_list)
    
    # print("Average investment return: ")


# def Randomizing():
#     df = pd.DataFrame({"D1": range(5), "D2": range(5)})
#     df2 = df.reindex(np.random.permutation(df.index))
#
#     print(df2)
#
# Randomizing()
Analysis()