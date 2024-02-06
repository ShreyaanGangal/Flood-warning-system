from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    "builds a list of stations within 10km of the Cambridge city centre."
    cambridge_city_centre_coords = (52.2053, 0.1218)
    stations_in_radius = stations_within_radius(build_station_list(),cambridge_city_centre_coords,10)
    print (stations_in_radius)
    
if __name__ == '__main__':
    run()