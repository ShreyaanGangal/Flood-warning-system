from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    """Prints the name of each station at which the current relative level is over 0.8, with the relative level alongside the name."""
    stations = build_station_list
    update_water_levels(stations)
    for station , water_level in stations_level_over_threshold(stations, 0.8):
        print (station.__name__, water_level)

if __name__ == '__main__':
    run()