from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

Test_station_1 =MonitoringStation("testid1","testmeasure1","1",(0, 360),(-4, 6),"testriver1","testtown1")
Test_station_2 =MonitoringStation("testid2","testmeasure2","2",(180, 180),(3, 7),"testriver2","testtown2")
Test_station_3 =MonitoringStation("testid3","testmeasure3","3",(-180, 0), None,"testriver3","testtown3")       

Test_station_1.latest_level = 1 #Test_station_1 will have a relative water level of 0.5
Test_station_2.latest_level = 11 #Test_station_2 will have a relative water level of 2
Test_station_3.latest_level = -2

Test_station_list = [Test_station_1, Test_station_2, Test_station_3]


def test_stations_level_over_threshold():
    assert stations_level_over_threshold(Test_station_list, 0.9) == [(Test_station_2), 2]