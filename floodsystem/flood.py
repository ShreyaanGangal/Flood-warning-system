from floodsystem.stationdata import update_water_levels 
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples that hold a station at which the latest relative water level is over 'tol' and the relative water level at the station."""
    list = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                list.append((station, station.relative_water_level()))
    sorted_list_by_rwl = sorted_by_key(list, 1, reverse= True)
    return sorted_list_by_rwl


def stations_highest_rel_level(stations, N):
    """Returns a list of N stations at which the water level, relative to the typical range, is highest."""
    list = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() is not None:
            list.append((station, station.relative_water_level()))
    sorted_list = sorted_by_key(list, 1, reverse= True)
    
    N_sorted_list = []
    for target in sorted_list: 
        N_sorted_list.append(target[0:N])
    return N_sorted_list
