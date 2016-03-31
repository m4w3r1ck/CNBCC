print "Initiating..."

import pandas
import matplotlib.pyplot as plt
import numpy as np
import datetime


#%%

def relative_strength(prices, n=14):
    """
    compute the n period relative strength indicator
    http://stockcharts.com/school/doku.php?id=chart_school:glossary_r#relativestrengthindex
    http://www.investopedia.com/terms/r/rsi.asp
    """

    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi

def t2d(x):
    "Prevede datum z txt na datetime"
    d = [int(e) for e in x.split(".")]
    return datetime.datetime(d[2],d[1], d[0])
    
class UpdateLim(object):
    def __init__(self, h=500, w=500, niter=50, radius=2., power=2):
        self.height = h
        self.width = w
        self.niter = niter
        self.radius = radius
        self.power = power
        
    def __call__(self, ax):
        print "Update"
        #ax2.ylim()
        print ax
        ax.figure.canvas.draw_idle()
        
nearest = lambda mlist, num: min(mlist, key=lambda x:abs(x-num))

#%%
print "Reading data"
data = pandas.read_excel("DATA.xls")
today = datetime.date.today()# .strftime("%d.%m.%Y")
ld = t2d(data["Datum"].iloc[-1]).date()
td = ld-today
#==============================================================================
if (ld != today and today.isocalendar()[2]<6) or (td < datetime.timedelta(-3) and today.isocalendar()[2]>5):
     print "Updating data..."
     try:
         d = pandas.read_csv(  "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/rok.txt?rok=2016" , sep="|", decimal=",", parse_dates=True)
 
         data = data.append(d).drop_duplicates()
         data.to_excel("DATA.xls","RAW")
     except Exception, msg:
         print msg
         pass
 
#==============================================================================
#%%

#%%
print "Ploting..."
class ChartMaker(object):
    def __init__(self,**args):
        self.fig, self.ax = plt.subplots(3, sharex=True)
        
    def __call__(self, ax): 
        x,y = [int(round(e)) for e in ax.get_xlim()]
        l = self.ax[1].get_lines()[0]
        mx = list(l._x).index(nearest(l._x, x))
        my = list(l._x).index(nearest(l._x, y))        
        v = l._y[mx:my]
        self.ax[1].set_ylim(min(v)*1.1,max(v)*1.1)

    def get_fig(self):
        return self.fig  
        
    def get_currencies(self):
        a = [e[-3:] for e in data.keys()[:-1]]
        a.sort()
        return a
                
    def draw(self, mena = "RUB"):
        print "Calculating data..."
        mena = data.keys()[[mena in e for e in data.keys()].index(True)]
        y = data[mena]
        #x = range(len(y))
        #x = pandas.to_datetime( data["Datum"] )
        x = [t2d(e) for e in data["Datum"]]

        macd = pandas.ewma(y,8) - pandas.ewma(y,26)
        signal = pandas.ewma(macd,span=9)
        indicator = np.array(macd-signal)
        rsi = relative_strength(y)

        (ax1, ax2,ax3) = self.ax
        [e.hold(True) for e in self.ax]
        [e.grid(True) for e in self.ax]
        p = round(100-y.values[-2]/y.values[-1]*100,2)
        ax1.set_title(mena+" CZK %s %s"%(list(data["Datum"])[-1], list(data[mena])[-1])+" %.2f%%"%p)
        ax1.plot_date(x,y,'k-')
        ax1.plot(x,pandas.ewma(y,12),'r-')
        ax1.plot(x,pandas.ewma(y,26),'g-')
        ax1.plot(x,pandas.stats.moments.rolling_median(y,50) )
        ax1.callbacks.connect('xlim_changed', self) #DrawEvent
        ax1.callbacks.connect('DrawEvent', self)        
        
        #ax2.subplot(4,1,3, sharex=True) # MACD
        p = round(100-indicator[-2]/indicator[-1]*100,2)
        ax2.set_title("%.4f, %.2f%%"%(indicator[len(x)-1], p))
        ax2.plot(x,macd)
        ax2.plot(x,signal)
        ax2.fill_between(x, indicator, 0, indicator>0, color='green',alpha=0.2,interpolate=True)
        ax2.fill_between(x, indicator, 0, indicator<0, color='red',alpha=0.2,interpolate=True)
        ax2.plot(x,indicator,color='black')
        ax2.plot(x,[0]*len(x),color='black',alpha=0.6)
        
        #plt.subplot(4,1,4, shar) #RSI
        ax3.set_title("%.2f"%rsi[-1])
        ax3.plot(x,[70]*len(x),color='black',alpha=0.6)
        ax3.plot(x,[30]*len(x),color='black',alpha=0.6)
        ax3.plot(x,[50]*len(x),color='black',alpha=0.3)
        ax3.fill_between(x, rsi, 70, rsi>70, color='red',alpha=0.2,interpolate=True)
        ax3.fill_between(x, rsi, 30, rsi<30, color='green',alpha=0.2,interpolate=True)
        ax3.plot(x,rsi)
        
        self.fig.autofmt_xdate()
        #self.fig.tight_layout()


if __name__ == "__main__":
    cm = ChartMaker()
    cm.draw()
    plt.show()
