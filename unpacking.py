import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from matplotlib.dates import strpdate2num
import time
from functools import reduce

def bytesdate(fmt, encoding = 'utf-8'):
    strconverter = strpdate2num(fmt)
    def bytescoverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytescoverter
    


date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack=True, 
                            delimiter = ',', 
                            converters={0:bytesdate('%Y%m%d%H%M%S')})
avgLine = ((bid+ask)/2)
patternAr = []
performanceAr = []
patForRec = []


def percentChange(startPoint, currentPoint):
    try:
        d = (float(currentPoint)-startPoint)*100.00/abs(startPoint)
        if d == 0.0:
            return 0.00000001
        else:
            return d
    except:
        return 0.00000001
        
def patternStorage():
    patStartTime = time.time()
    x = len(avgLine) - 60
    y = 31
    while y<x:
        pattern = []
        p1 = percentChange(avgLine[y-30], avgLine[y-29])
        p2 = percentChange(avgLine[y-30], avgLine[y-28])
        p3 = percentChange(avgLine[y-30], avgLine[y-27])
        p4 = percentChange(avgLine[y-30], avgLine[y-26])
        p5 = percentChange(avgLine[y-30], avgLine[y-25])
        p6 = percentChange(avgLine[y-30], avgLine[y-24])
        p7 = percentChange(avgLine[y-30], avgLine[y-23])
        p8 = percentChange(avgLine[y-30], avgLine[y-22])
        p9 = percentChange(avgLine[y-30], avgLine[y-21])
        p10 = percentChange(avgLine[y-30], avgLine[y-20])
        p11 = percentChange(avgLine[y-30], avgLine[y-19])
        p12 = percentChange(avgLine[y-30], avgLine[y-18])
        p13 = percentChange(avgLine[y-30], avgLine[y-17])
        p14 = percentChange(avgLine[y-30], avgLine[y-16])
        p15 = percentChange(avgLine[y-30], avgLine[y-15])
        p16 = percentChange(avgLine[y-30], avgLine[y-14])
        p17 = percentChange(avgLine[y-30], avgLine[y-13])
        p18 = percentChange(avgLine[y-30], avgLine[y-12])
        p19 = percentChange(avgLine[y-30], avgLine[y-11])
        p20 = percentChange(avgLine[y-30], avgLine[y-10])
        p21 = percentChange(avgLine[y-30], avgLine[y-9])
        p22 = percentChange(avgLine[y-30], avgLine[y-8])
        p23 = percentChange(avgLine[y-30], avgLine[y-7])
        p24 = percentChange(avgLine[y-30], avgLine[y-6])
        p25 = percentChange(avgLine[y-30], avgLine[y-5])
        p26 = percentChange(avgLine[y-30], avgLine[y-4])
        p27 = percentChange(avgLine[y-30], avgLine[y-3])
        p28 = percentChange(avgLine[y-30], avgLine[y-2])
        p29 = percentChange(avgLine[y-30], avgLine[y-1])
        p30 = percentChange(avgLine[y-30], avgLine[y])
        
        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        try:
            n = reduce(lambda x,y:x+y, outcomeRange)/len(outcomeRange)
        except Exception as e:
            print(str(e))
            n = 0
            
        futureOutcome = percentChange(currentPoint, n)
        while n in (1,30):
            pattern.append(p,n)
            
        
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        

        
        y+=1
        patEndTime = time.time()
    print('Time taken: ', patEndTime-patStartTime)
    print(len(patternAr))
    print(len(performanceAr))
    
def GraphRawFX():
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan = 40, colspan = 40)
    
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)    
    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor = 'c', alpha = 0.5)
        

    #plt.subplots_adjust(bottom = 0.23)
    plt.grid(True)
    plt.show()
    
def currentPattern():

    cp1 = percentChange(avgLine[-11], avgLine[-10])
    cp2 = percentChange(avgLine[-11], avgLine[-9])
    cp3 = percentChange(avgLine[-11], avgLine[-8])
    cp4 = percentChange(avgLine[-11], avgLine[-7])
    cp5 = percentChange(avgLine[-11], avgLine[-6])
    cp6 = percentChange(avgLine[-11], avgLine[-5])
    cp7 = percentChange(avgLine[-11], avgLine[-4])
    cp8 = percentChange(avgLine[-11], avgLine[-3])
    cp9 = percentChange(avgLine[-11], avgLine[-2])
    cp10 = percentChange(avgLine[-11], avgLine[-1])
    
    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)
    
    
def PatternRecognition():
    for eachPattern in patternAr:
        sim1 = 100.00 - abs(percentChange(eachPattern[0], patForRec[0]))
        sim2 = 100.00 - abs(percentChange(eachPattern[1], patForRec[1]))
        sim3 = 100.00 - abs(percentChange(eachPattern[2], patForRec[2]))
        sim4 = 100.00 - abs(percentChange(eachPattern[3], patForRec[3]))
        sim5 = 100.00 - abs(percentChange(eachPattern[4], patForRec[4]))
        sim6 = 100.00 - abs(percentChange(eachPattern[5], patForRec[5]))
        sim7 = 100.00 - abs(percentChange(eachPattern[6], patForRec[6]))
        sim8 = 100.00 - abs(percentChange(eachPattern[7], patForRec[7]))
        sim9 = 100.00 - abs(percentChange(eachPattern[8], patForRec[8]))
        sim10 = 100.00 - abs(percentChange(eachPattern[9], patForRec[9]))
        
        howSim = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10)/10.00
        
        if howSim > 70:
            patdex = patternAr.index(eachPattern)
            
            print('########################################')
            print(patForRec)
            print('========================================')
            print(eachPattern)
            print('----------------------------------------')
            print('predicted outcome', performanceAr[patdex])
            xp = [1,2,3,4,5,6,7,8,9,10]
            fig2 = plt.figure()
            plt.plot(xp,patForRec)
            plt.plot(xp, eachPattern)
            plt.show()
            print('########################################')
    
    
patternStorage()
currentPattern()
PatternRecognition()

    
    
    
    