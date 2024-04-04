import json
import requests

start_date = "2024-03-27"
end_date = "2069-03-18"

print("from " + start_date)
print("to " + end_date)
print("")

r = requests.get(f"https://stats-api.hyperliquid.xyz/hyperliquid/funding_rate?start_date={start_date}&end_date={end_date}")
data = r.json()["chart_data"]

def filter_desired_coins(data, coin_filter = ['ETH', 'BTC', 'SOL']):
    return [entry['coin'] for entry in data if entry['coin'] in coin_filter]

def all_coins(data):
    return [entry['coin'] for entry in data]

result = {}
coins = filter_desired_coins(data)
print(str(len(coins)) + " data points")
print("")

for coin in coins:
    data_points = [item['sum_funding'] for item in data if item['coin'] == coin]
    result[coin] = sum(data_points) / len(data_points)  #coins might have fewer data points than other coins due to being newer so divide by len(data_points)

for item in result:
    print(item)
    print(round(result[item], 2))
    print("\n")
