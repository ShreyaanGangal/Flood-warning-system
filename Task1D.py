from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station

def run():
    """prints how many rivers have at least one monitoring station and prints the first 10 of these rivers in alphabetical order"""
    stations = build_station_list()
    river_container = rivers_with_station(stations)
    
    print(f"{len(river_container)} stations.")
    print(river_container[0:10])

    """prints """


if __name__ == '__main__':
    run()