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
    monitoring_stations_ranked_by_water_level = stations_highest_rel_level(stations, len(stations))
    dict_town_and_scaled_risk = {}
    for station in monitoring_stations_ranked_by_water_level:
        #if station[0] is None:
            #pass
            stat = station[0]
            dt = 5
            dates, levels = fetch_measure_levels(
                    stat.measure_id, dt=datetime.timedelta(days=dt))
            p = 4
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
    
    print(dict_town_and_scaled_risk)
    sorted_dict_town_and_scaled_risk = sorted(dict_town_and_scaled_risk.items(), key=lambda x: x[1], reverse = True)
    print(sorted_dict_town_and_scaled_risk)
    #resultList = list(sorted_dict_town_and_scaled_risk.items())
 #   empty_dictionary = {}
  #  for n in sorted_dict_town_and_scaled_risk:
         
         





if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()





