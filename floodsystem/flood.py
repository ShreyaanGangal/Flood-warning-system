from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples that hold a station at which the latest relative water level is over 'tol' and the relative water level at the station."""
    list_1 = []
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                list_1.append((station, station.relative_water_level()))
    sorted_list_by_rwl = sorted_by_key(list_1, 1, reverse= True)
    return sorted_list_by_rwl


def stations_highest_rel_level(stations, N):
    """Returns a list of N stations at which the water level, relative to the typical range, is highest."""
    list_1 = []
    for station in stations:
        if station.relative_water_level() is not None:
            list_1.append((station, station.relative_water_level()))
    return sorted_by_key(list_1, 1, reverse= True)[0:N]