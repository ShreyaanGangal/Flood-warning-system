# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from .utils import sorted_by_key  # noqa


from floodsystem.stationdata import build_station_list

def rivers_by_station_number(stations, N):
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
    tuple_rivers_number = ()
    for i in len(number_of_stations):
        tuple_rivers_number.append(rivers(i), number_of_stations[i])
    
    return tuple_rivers_number



