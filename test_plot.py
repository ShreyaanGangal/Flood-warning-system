from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np

#dates = [1,2,3,4,5,6,7,8,9]
dates = [matplotlib.dates.date2num(date) for date in np.random.rand(9)]

levels = [-4,-3,-2,-1,0,1,2,3,4]
station = MonitoringStation("Station ID", "Measure ID", "Station", (0,-15), (-2,2),"River ", "Town")


def test_plot_water_levels():
    plt.switch_backend('agg')
    plot_water_levels(station, dates, levels)

    assert len(plt.gca().lines) == 3
    assert plt.gca().get_xlabel() == 'Dates'
    assert plt.gca().get_ylabel() == 'Water Level (m)'

#def test_plot_water_level_with_fit():
 #   p=4
  #  plt.switch_backend('agg')
   # plot_water_level_with_fit(station, dates, levels, p)
    #axes = plt.gca()

    #assert len(axes.lines) == 5
    #assert axes.get_xlabel() == 'Dates'
    #assert axes.get_ylabel() == 'Water Level (m)'
