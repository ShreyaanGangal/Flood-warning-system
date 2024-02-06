from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number

test_station_1 = MonitoringStation("Station ID 1", "Measure ID 1", "Station 1", (3,4), (5,6),"River 1", "Town 1") 
test_station_2 = MonitoringStation("Station ID 2", "Measure ID 2", "Station 2", (-6,8), None,"River 2", "Town 2") 
test_station_3 = MonitoringStation("Station ID 3", "Measure ID 3", "Station 3", (0,-15), (3,4),"River 3", "Town 3") 

test_stations_list = [test_station_1, test_station_2, test_station_3]

def test_stations_by_distance():
    test_output = stations_by_distance(test_stations_list,(0,0))
    assert test_output[0][0]==test_station_1
    assert test_output[1][0]==test_station_2
    assert test_output[2][0]==test_station_3

def test_stations_within_radius():
    test_output = stations_within_radius(test_stations_list, (0,0), 1000000)
    assert test_output == [test_station_1.name, test_station_2.name, test_station_3.name]

def test_rivers_with_stations():
    test_output = rivers_with_station(test_stations_list)
    assert test_output == [test_station_1.river, test_station_2.river, test_station_3.river]

def test_stations_by_river():
    test_output = stations_by_river(test_stations_list)
    assert test_output[test_station_1.river] == [test_station_1.name]
    assert test_output[test_station_2.river] == [test_station_2.name]
    assert test_output[test_station_3.river] == [test_station_3.name]


test_station_1 = MonitoringStation("Station ID 1", "Measure ID 1", "Station 1", (3,4), (5,6),"River 1", "Town 1") 
test_station_2 = MonitoringStation("Station ID 2", "Measure ID 2", "Station 2", (-6,8), None,"River 2", "Town 2") 
test_station_3 = MonitoringStation("Station ID 3", "Measure ID 3", "Station 3", (0,-15), (3,4),"River 3", "Town 3") 
test_station_4 = MonitoringStation("Station ID 4", "Measure ID 4", "Station 4", (0,-15), (3,4),"River 1", "Town 4") 
test_station_5 = MonitoringStation("Station ID 5", "Measure ID 5", "Station 5", (0,-15), (3,4),"River 3", "Town 5")
test_station_6 = MonitoringStation("Station ID 5", "Measure ID 5", "Station 5", (0,-15), (3,4),"River 3", "Town 6")  
test_stations_list_2 = [test_station_1, test_station_2, test_station_3, test_station_4, test_station_5, test_station_6]

def test_rivers_by_station_number():
    test_output_1 = rivers_by_station_number(test_stations_list_2, 2)
    assert test_output_1 == [("River 3", 3), ("River 1", 2)]
    test_output_2 = rivers_by_station_number(test_stations_list_2, 3)
    assert test_output_2 == [("River 3", 3), ("River 1", 2), ("River 2", 1)]
