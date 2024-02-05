from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation


stations = build_station_list()

x = inconsistent_typical_range_stations(stations)

''''list_inconsistent_stations = []
print (x)
for i in x:
    if 'Station name' in i:
         list_inconsistent_stations.append(i['Station name'])
print (list_inconsistent_stations)'''


''''for e in data["items"]:
        # Extract town string (not always available)
        town = None
        if 'town' in e:
            town = e['town']'''''

#print (x)
list_inconsistent_stations = []
for station in x:
    list_inconsistent_stations.append(station.name)
print (sorted(list_inconsistent_stations))