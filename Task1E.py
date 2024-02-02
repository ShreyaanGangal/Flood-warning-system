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

#rivers_by_station_number(stations,1)


def rivers_by_station_number(stations, N):
    rivers_station_number_dict = {}
    for station in stations:
        if station.river in rivers_station_number_dict:
            rivers_station_number_dict[station.river] += 1
        else:
            rivers_station_number_dict[station.river] = 1

    
    sorted_rivers_station_number_list = sorted(rivers_station_number_dict.items(), key=lambda x: x[1], reverse = True) #creates a sorted list of all dictionary items in descending order by value
    #print(sorted_rivers_station_number_dict)
    #print(len(sorted_rivers_station_number_dict))
    list_largest_rivers = sorted_rivers_station_number_list[:N] #creates a list of the rivers with the N largest amount of monitoring stations
    for i in range(N, len(sorted_rivers_station_number_list)):
        if sorted_rivers_station_number_list[i][1] == list_largest_rivers[-1][1]:
            list_largest_rivers.append(sorted_rivers_station_number_list[i])
        else:
            break
    
    print(list_largest_rivers)

rivers_by_station_number(stations, 9)



