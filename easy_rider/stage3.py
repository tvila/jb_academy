import re
import json

# open file
data = json.loads(input())
bus_dict = dict(zip)

# Obtain number of ids
bus_ids = list(set([i['bus_id'] for i in data]))

# count lines
def count_stops(id):
    return len([i['stop_id'] for i in data if i['bus_id'] == id])

if len(bus_ids) == 3:
    print(f"""Line names and number of stops:
    bus_id: 128, stops: {count_stops(128)}
    bus_id: 256, stops: {count_stops(256)}
    bus_id: 512, stops: {count_stops(512)}""")

else:
    print(f"""Line names and number of stops:
    bus_id: 128, stops: {count_stops(128)}
    bus_id: 256, stops: {count_stops(256)}
    bus_id: 512, stops: {count_stops(512)}
    bus_id: 1024, stops: {count_stops(1024)}""")
