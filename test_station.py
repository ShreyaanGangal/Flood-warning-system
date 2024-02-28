# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

Test_station_1 =MonitoringStation("testid1","testmeasure1","1",(0, 360),(-5, 6),"testriver1","testtown1")
Test_station_2 =MonitoringStation("testid2","testmeasure2","2",(180, 180),(7, 3),"testriver2","testtown2")
Test_station_3 =MonitoringStation("testid3","testmeasure3","3",(-180, 0), None,"testriver3","testtown3")       
Test_station_list = [Test_station_1, Test_station_2, Test_station_3]


def test_typical_range_consistent():
    assert Test_station_1.typical_range_consistent() #assert that test station 1 returns true
    assert not Test_station_2.typical_range_consistent() #assert that test station 2 returns false
    assert not Test_station_3.typical_range_consistent() #assert that test station 3 returns false

def test_inconsistent_typical_range_stations():
    a = inconsistent_typical_range_stations(Test_station_list) 
    assert Test_station_2 in a
    assert Test_station_3 in a
    assert len(a) ==  2

def test_relative_water_level():
    Test_station_1.latest_level = 105
    assert Test_station_1.relative_water_level() == 10

    Test_station_1.latest_level = 0.5
    assert Test_station_1.relative_water_level() == 0.5









        
