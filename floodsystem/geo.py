# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


from floodsystem.stationdata import build_station_list

def rivers_greatest_no_monitoring_stations():
    stations = build_station_list()
    

