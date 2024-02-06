from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation




def run():
    stations = build_station_list()
    x = inconsistent_typical_range_stations(stations)
#print (x)
    list_inconsistent_stations = []
    for station in x:
        list_inconsistent_stations.append(station.name)
    print (sorted(list_inconsistent_stations))

if __name__ == "__main__":
    run()


