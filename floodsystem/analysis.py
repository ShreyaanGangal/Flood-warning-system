from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import matplotlib as plt
import datetime
import numpy as np
import matplotlib.dates

def polyfit(dates, levels, p):
    b = matplotlib.dates.date2num(dates)

    if not (len(b) and len(levels)):
       return 0, 0

    if not all(isinstance(n, (datetime.datetime)) for n in dates):
        return 0, 0
    
    if not all(isinstance(n, (int, float)) for n in b):
        return 0, 0
    
    if not all(isinstance(n, (int, float)) for n in levels):
        return 0, 0

    if len(b) != len(levels):
        return 0, 0
    
    p_coeff = np.polyfit(b - b[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly, b[0])





def run():

    # Build list of stations
    stations = build_station_list()

    # Station name to find
    station_name = "Cam"

    # Find station
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    # Check that station could be found. Return if not found.
    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return

    # Alternative find station 'Cam' using the Python 'next' function
    # (https://docs.python.org/3/library/functions.html#next). Raises
    # an exception if station is not found.
    # try:
    #     station_cam = next(s for s in stations if s.name == station_name)
    # except StopIteration:
    #     print("Station {} could not be found".format(station_name))
    #     return

    # Fetch data over past 2 days
    dt = 2
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))

    # Print level history
    for date, level in zip(dates, levels):
        print(date, level)


if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()