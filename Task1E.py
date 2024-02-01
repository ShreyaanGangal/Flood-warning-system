from floodsystem.stationdata import build_station_list

stations = build_station_list()
'''''def rivers_by_station_number(stations, N):
    rivers = []
    number_of_stations = [0] * 100
    # create a list of all the rivers and the number of monitoring stations on each
    for station in stations:
        if station.river in rivers:
            number_of_stations[rivers.index(station.river)] = number_of_stations[rivers.index(station.river)] + 1
        else:
           rivers.append(station.river)
           print (number_of_stations)
           #print(rivers.index(station.river))
           number_of_stations[rivers.index(station.river)] = number_of_stations[rivers.index(station.river)] + 1
    tuple_rivers_and_number = ()
    for i in len(number_of_stations):
        tuple_rivers_and_number = tuple_rivers_and_number + ((rivers(i), number_of_stations[i]),)
    
    return tuple_rivers_and_number'''''

rivers_by_station_number(stations,1)


def rivers_by_station_number(stations, N):
    for station in stations:
        