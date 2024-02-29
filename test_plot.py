from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import matplotlib.pyplot as plt

dates = [1,2,3,4,5,6,7,8,9]
levels = [-4,-3,-2,-1,0,1,2,3,4]
station = MonitoringStation("Station ID", "Measure ID", "Station", (0,-15), (-2,2),"River ", "Town")


def test_plot_water_levels():
    plt.switch_backend('agg')
    plot_water_levels(station, dates, levels)

    assert len(plt.gca().lines) == 3
    assert plt.gca().get_xlabel() == 'Dates'
    assert plt.gca().get_ylabel() == 'Water Level (m)'