 My code
def check_start_stops(data, flag=['S', 'F']):
    return list(set([i['stop_name'] for i in data if i['stop_type'] == flag]))

def check_tranfers(data):
    transfer_stations = {key: 0 for key in list(set([i['stop_name'] for i in data]))}
    
    for i in data:
        transfer_stations[i['stop_name']] += 1

    result = {key:value for (key, value) in transfer_stations.items() if value > 1}
    return list(result.keys())


def check_lines(data):
    bus_ids = list(set([i['bus_id'] for i in data]))
    dict_start_stop_c = {key: [] for key in bus_ids}

    pattern =  r"^[SF]{1}$"

    for i in data:
        bus_id = i['bus_id']
        stop_type = i['stop_type']
        if re.search(pattern, stop_type):
            dict_start_stop_c[bus_id].append(stop_type)

    result = [len(dict_start_stop_c[i]) for i in dict_start_stop_c.keys()]
    
    try:
        non_valid = list({key:value for (key, value) in dict_start_stop_c.items() if len(value) != 2}.keys())[0]
    except:
        pass
    
    return True if len(set(result)) == 1 else non_valid


def main():

    validator = check_lines(data)
    
    if validator == True:
        start = check_start_stops(data, "S")
        stop = check_start_stops(data, "F")
        transfer = check_tranfers(data)

        return f"Start stops: {len(start)} {sorted(start)}\nTransfer stops: {len(transfer)} {sorted(transfer)}\nFinish stops: {len(stop)} {sorted(stop)}"""
    else:
        return f"There is no start or end stop for the line: {validator}."

print(main())
