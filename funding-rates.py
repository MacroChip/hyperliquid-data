import json
import requests
from datetime import datetime

start_date_str = "2024-04-25"
end_date_str = "2029-04-16"
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

print("from " + start_date_str)
print("to " + end_date_str)
print("")

r = requests.get(f"https://d2v1fiwobg9w6.cloudfront.net/funding_rate")
data = r.json()["chart_data"]

def all_coins(data):
    return [entry['coin'] for entry in data]

def filter_desired_entries(data, coin_filter):
    result = []
    for entry in data:
        date_to_check = datetime.strptime(entry['time'], "%Y-%m-%dT%H:%M:%S")
        if entry['coin'] in coin_filter and start_date <= date_to_check <= end_date:
            result.append(entry)
    return result

def all_coins(data):
    return [entry['coin'] for entry in data]

result = {}
coin_filter = all_coins(data)
coins = filter_desired_entries(data, coin_filter)
# print(coins)
print(str(len(coins)) + " data points")
print("")

for coin in coin_filter:
    data_points = [item['sum_funding'] for item in coins if item['coin'] == coin]
    result[coin] = sum(data_points) / len(data_points)  #coins might have fewer data points than other coins due to being newer so divide by len(data_points)

sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=False)

for item, value in sorted_result:
    print(item)
    print(round(value, 4))
    print("\n")
