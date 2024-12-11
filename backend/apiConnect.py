import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

api_key = "bfeeb7cd-24e7-4b14-882c-a2604e8af2c3"

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": api_key,
}

parameters = {
    "start": "1",
    "limit": "50",
    "convert": "USD",
}

def responApiJson():
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur {response.status_code}: {response.text}")