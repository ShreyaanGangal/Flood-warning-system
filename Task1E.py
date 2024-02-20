from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

#rivers_by_station_number(stations,1)

def run():
    stations = build_station_list()
    print(rivers_by_station_number(stations, 7))

if __name__ == '__main__':
    run()



