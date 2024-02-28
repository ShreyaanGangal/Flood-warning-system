from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level     

test_station_1 = MonitoringStation("Station ID 1", "Measure ID 1", "Station 1", (3,4), (5,6),"River 1", "Town 1") 
test_station_2 = MonitoringStation("Station ID 2", "Measure ID 2", "Station 2", (-6,8), None,"River 2", "Town 2") 
test_station_3 = MonitoringStation("Station ID 3", "Measure ID 3", "Station 3", (0,-15), (3,4),"River 3", "Town 3") 

test_station_1.latest_level = 5.5 #test_station_1 will have a relative water level of 0.5
test_station_2.latest_level = 11 
test_station_3.latest_level = 5 #test_station_3 will have a relative water level of 2

test_station_list = [test_station_1, test_station_2, test_station_3]

def test_stations_level_over_threshold():
    assert stations_level_over_threshold(test_station_list, 0.1) == [(test_station_3, 2), (test_station_1, 0.5)]

def test_stations_highest_rel_level():
    assert stations_highest_rel_level(test_station_list, 2) == [(test_station_3, 2), (test_station_1, 0.5)]