# Write your awesome code here
import json

# open file
data = json.loads(input())

stop_name = list(set([i['stop_name'] for i in data]))

# count lines
def count_stops(id):
    return [i['stop_type'] for i in data if i['stop_name'] == id]

wrong_stops = []

for i in stop_name:
    stop_types = count_stops(i)

    if len(stop_types) > 1 and 'O' in stop_types:
        wrong_stops.append(i)

print(f"On demand stops test:")
if len(wrong_stops) == 0:
    print("OK")
else:
    print(f"Wrong stop type: {sorted(wrong_stops)}")
