from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """prints a list of tuples for the 10 clsoest and 10 furthest stations from the Cambridge city centre"""
    
    stations_list = []
    cambridge_city_centre_coords = (52.2053, 0.1218)
    stations_distance_list = stations_by_distance(build_station_list(),cambridge_city_centre_coords)
    for (station,distance) in stations_distance_list:
        stations_list.append((station.name,station.town,distance))

    print (stations_list[:10])
    print (stations_list[-10:])

if __name__ == '__main__':
    run()