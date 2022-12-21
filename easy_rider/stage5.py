def convert_times(x):
    # Conver to time formar
    time_format = '%H:%M'

    return datetime.strptime(x, time_format).time()


def compare_times(x, y):
    # Compare if time x is greater than time y
    return convert_times(x) > convert_times(y)


def stop_time_dict(bus_id):
    # Create a bus line dictionary containing stop name and time
    bus_dict = {i['stop_name']: i['a_time'] for i in data if i['bus_id'] == bus_id} 
    time_list = list(bus_dict.values())
    time_list_subset = time_list[1:]

    stop_name_list = list(bus_dict.keys())

    return time_list, time_list_subset, stop_name_list


def line_checker():
    # Creates a dictionary with identified errors 
    bus_ids = list(set([i['bus_id'] for i in data]))
    errors_dict = {}

    for i in bus_ids:
        time, time_subset, stop_name = stop_time_dict(i)

        for j in range(len(time_subset)):
            check = convert_times(time_subset[j]) > convert_times(time[j])
            stop = stop_name[j+1]

            if check == False:
                errors_dict[i] = stop
                break

    return errors_dict
    

# Final
result = line_checker()
if len(result) == 0:
    print(f"Arrival time test: n\OK")

else:
    print("Arrival time test:")
    for i in result.keys():
        print(f"bus_id line {i}: wrong time on station {result[i]}")
