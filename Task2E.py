import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def run():
    """Plots the water levels over the past 10 days for the 5 stations at which the relative water level is greatest."""
    stations = build_station_list()
    update_water_levels(stations)
    wanted_stations = stations_highest_rel_level(stations, 5)

    for station in wanted_stations:
        dt=10
        dt=datetime.timedelta(days=dt)
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        plot_water_levels(station, dates, levels)

if __name__ == '__main__':
    run()