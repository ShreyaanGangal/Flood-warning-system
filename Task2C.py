from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    """Prints the name of the 10 stations at which the current relative level is highest, with the relative level beside each station name."""
    stations = build_station_list()
    update_water_levels(stations)
    high_risk_stations = stations_highest_rel_level(stations, 10)
    for station, relative_level in high_risk_stations:
        print(station.name, relative_level)

if __name__ == '__main__':
    run()