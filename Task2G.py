from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
import numpy as np
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.dates
from floodsystem.stationdata import update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    monitoring_stations_ranked_by_water_level = stations_highest_rel_level(stations, 8)
    dict_town_and_scaled_risk = {}
    for station in monitoring_stations_ranked_by_water_level:
        #if station[0] is None:
            #pass
        stat = station[0]
        dt = 1
        dates, levels = fetch_measure_levels(
                stat.measure_id, dt=datetime.timedelta(days=dt))
        p = 12
        poly, d0 = polyfit(dates, levels, p)
        #print(poly)
        if not poly:
            #print(station[0].name)
            continue
        derivative = poly.deriv()
        #print(derivative)
        a = matplotlib.dates.date2num(dates)
        #print(stat.relative_water_level())
        #print(derivative(a[-1]- d0))
        if stat.town in dict_town_and_scaled_risk:
           dict_town_and_scaled_risk[stat.town] += ((stat.relative_water_level())+(stat.relative_water_level())*derivative(a[-1]-d0))
        else:
            dict_town_and_scaled_risk[stat.town] = ((stat.relative_water_level())+(stat.relative_water_level())*derivative(a[-1]-d0))
    
    #print(dict_town_and_scaled_risk)
    sorted_dict_town_and_scaled_risk = sorted(dict_town_and_scaled_risk.items(), key=lambda x: x[1], reverse = True)
    print(sorted_dict_town_and_scaled_risk)
    
    length = len(sorted_dict_town_and_scaled_risk)
    station_name = 'Old Windsor'
    high_level = sorted_dict_town_and_scaled_risk[int((length/5))][1] # finds the cutoff risk level for the medium levels
    print (high_level)
    medium_level = sorted_dict_town_and_scaled_risk[int((length/3))][1] # finds the cutoff risk level for the medium levels
    low_level = sorted_dict_town_and_scaled_risk[int((length/1.5))][1] # finds the cutoff risk level for the lowest levels

    #keys = list(sorted_dict_town_and_scaled_risk.keys())
    town_names = [item[0] for item in sorted_dict_town_and_scaled_risk]
    print (town_names)
    if station_name in town_names:
        index = town_names.index(station_name)
        if sorted_dict_town_and_scaled_risk[index][1] > high_level:
            print(station_name + ' ' + 'has a high risk of flooding')
        elif sorted_dict_town_and_scaled_risk[index][1] > medium_level:
            print(station_name + ' ' + 'has a medium risk of flooding')
        elif sorted_dict_town_and_scaled_risk[index][1] > low_level:
            print(station_name + ' ' + 'has a low risk of flooding')

    else:
        print (station_name + ' ' + 'is not a valid station name')


    #resultList = list(sorted_dict_town_and_scaled_risk.items())
 #   empty_dictionary = {}
  #  for n in sorted_dict_town_and_scaled_risk:
         
         





if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()





