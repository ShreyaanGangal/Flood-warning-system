import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit


def run():
    """Plots the water levels over the past 10 days for the 5 stations at which the relative water level is greatest."""
    stations = build_station_list()
    update_water_levels(stations)
    wanted_stations = stations_highest_rel_level(stations, 5)

    for station in wanted_stations:
        stat = station[0]
        dt = 2
        dates, levels = fetch_measure_levels(
            stat.measure_id, dt=datetime.timedelta(days=dt))
        p = 4
        if dates and levels:
            plot_water_level_with_fit(stat, dates, levels, p)
        else:
            print("No date for" + ' ' + stat.name)
     #   plot_water_level_with_fit(stat, dates, levels,p)

if __name__ == '__main__':
    run()   

