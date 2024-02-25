import json
import requests

r = requests.get("https://stats-api.hyperliquid.xyz/hyperliquid/funding_rate?start_date=2023-11-14&end_date=2024-02-25")
data = r.json()["chart_data"]

def list_all_coins(data):
	return [entry['coin'] for entry in data]


def filter_eth_btc(data):
    return [entry for entry in data if entry['coin'] in ['ETH', 'BTC']]

result = {}

for coin in list_all_coins(data):
    data_points = [item['sum_funding'] for item in data if item['coin'] == coin] #coins might have fewer data points than other coins due to being newer
    result[coin] = sum(data_points) / len(data_points)

for item in result:
    if (item == "BTC" or item == "ETH"):
        print(item)
        print(round(result[item], 2))
        print("\n")
