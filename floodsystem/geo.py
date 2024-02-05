# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """returns a list of the stations and its distance from the coordinate p"""
    distances = []
    for station in stations: 
        distance = haversine(station.coord,p)
        distances.append((station, distance))
    sorted_by_distance = sorted_by_key(distances,1)
    return sorted_by_distance

from floodsystem.stationdata import build_station_list

''''def rivers_by_station_number(stations, N):
    stations = build_station_list()
    rivers = ()
    number_of_stations = []
    # create a list of all the rivers and the number of monitoring stations on each
    for station in stations:
        if station.river in rivers:
            number_of_stations[rivers.index(station.river)] = number_of_stations[rivers.index(station.river)] + 1
        else:
           rivers.append(station.river)
           number_of_stations[rivers.index(station.river)] = number_of_stations[rivers.index(station.river)] + 1
    tuple_rivers_and_number = ()
    for i in len(number_of_stations):
        tuple_rivers_and_number.append(rivers(i), number_of_stations[i])
    
    return tuple_rivers_and_number'''

def rivers_by_station_number(self, N):
    rivers_station_number_dict = {}
    for station in self:
        if station.river in rivers_station_number_dict:
            rivers_station_number_dict[station.river] += 1
        else:
            rivers_station_number_dict[station.river] = 1

    
    sorted_rivers_station_number_list = sorted(rivers_station_number_dict.items(), key=lambda x: x[1], reverse = True) #creates a sorted list of all dictionary items in descending order by value
    #print(sorted_rivers_station_number_dict)
    #print(len(sorted_rivers_station_number_dict))
    list_largest_rivers = sorted_rivers_station_number_list[:N] #creates a list of the rivers with the N largest amount of monitoring stations
    for i in range(N, len(sorted_rivers_station_number_list)):
        if sorted_rivers_station_number_list[i][1] == list_largest_rivers[-1][1]:
            list_largest_rivers.append(sorted_rivers_station_number_list[i])
        else:
            break
    
    return list_largest_rivers



