import json
import requests

start_date = "2023-11-01"
end_date = "2024-03-12"

print("from " + start_date)
print("to " + end_date)
print("\n")

r = requests.get(f"https://stats-api.hyperliquid.xyz/hyperliquid/funding_rate?start_date={start_date}&end_date={end_date}")
data = r.json()["chart_data"]

def filter_desired_coins(data, coin_filter = ['ETH', 'BTC']):
    return [entry['coin'] for entry in data if entry['coin'] in coin_filter]

result = {}

for coin in filter_desired_coins(data):
    data_points = [item['sum_funding'] for item in data if item['coin'] == coin]
    result[coin] = sum(data_points) / len(data_points)  #coins might have fewer data points than other coins due to being newer so divide by len(data_points)

for item in result:
    print(item)
    print(round(result[item], 2))
    print("\n")
