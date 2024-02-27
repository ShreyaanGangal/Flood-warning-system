from floodsystem.analysis import polyfit
import matplotlib as plt
import numpy as np
import matplotlib.dates

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    
    plt.plot(dates, levels, '.') #plotting original data points
    x = matplotlib.dates.date2num(dates)
    #d0 is the shift
    x1 = np.linspace(x[0], x[-1], 200)
    plt.plot(x1, poly(x1-d0))

    plt.show()
