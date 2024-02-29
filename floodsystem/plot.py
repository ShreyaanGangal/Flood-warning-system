from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates

def plot_water_level_with_fit(station, dates, levels, p):
    
    poly, d0 = polyfit(dates, levels, p)

    typical_low_levels = station.typical_range[0]
    typical_high_levels = station.typical_range[1]
    plt.plot(dates, [typical_low_levels]*len(dates), label = "Typical Low Level", ls = 'dotted')
    plt.plot(dates, [typical_high_levels]*len(dates), label = "Typical High Level", ls = 'dashed')
    plt.plot(dates, levels, label = station.name)

    plt.xlabel("Dates")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title("Water level of" + station.name)
    plt.tight_layout()
    
    x = matplotlib.dates.date2num(dates)
    #d0 is the shift
    x1 = np.linspace(x[0], x[-1], 200)
    plt.plot(x1, poly(x1-d0))
    

    plt.show()
    
#import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    """Displays a plot of the water level data against time for a stations, and includes the typical low and high levels"""
    typical_low_levels = station.typical_range[0]
    typical_high_levels = station.typical_range[1]
    plt.plot(dates, [typical_low_levels]*len(dates), label = "Typical Low Level", ls = 'dotted')
    plt.plot(dates, [typical_high_levels]*len(dates), label = "Typical High Level", ls = 'dashed')
    plt.plot(dates, levels, label = station.name)

    plt.xlabel("Dates")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title("Water level of" + station.name)
    plt.tight_layout()

    plt.show()
