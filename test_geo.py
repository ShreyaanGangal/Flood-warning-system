from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number

test_station_1 = MonitoringStation("Station ID 1", "Measure ID 1", "Label 1", (1,2), (3,4),"River 1", "Town 1") 
test_station_2 = MonitoringStation("Station ID 2", "Measure ID 2", "Label 2", (-5,2), None,"River 2", "Town 2") 
test_station_3 = MonitoringStation("Station ID 3", "Measure ID 3", "Label 3", (5,-6), (3,4),"River 1", "Town 1") 

test_stations_list = [test_station_1, test_station_2, test_station_3]

def test_stations_by_distance():
    stations_by_distance(test_stations_list,)
