import requests

exchange_rates_cache = {}


def get_exchange_rate(currency):
    if currency in exchange_rates_cache:
        return exchange_rates_cache[currency]
    url = f"http://www.floatrates.com/daily/{currency}.json"
    response = requests.get(url)
    data = response.json()
    exchange_rates_cache[currency] = data
    return data


def convert_currency(amount, source_currency, target_currency):
    source_data = get_exchange_rate(source_currency)
    source_rate = source_data[target_currency]['rate']
    converted_amount = amount * source_rate
    return converted_amount


source_currency = input("Введіть код валюти, яку ви маєте: ")
target_currency = input("Введіть код валюти, в яку ви хочете обміняти: ")
amount = float(input("Введіть суму грошей, яку ви маєте: "))

while source_currency:
    if source_currency == target_currency.upper():
        print("Валюти однакові. Розрахунок не потрібен.")
    else:
        converted_amount = convert_currency(amount, source_currency, target_currency)
        print(f"{amount} {source_currency.upper()} = {converted_amount} {target_currency.upper()}")

    source_currency = input("Введіть код валюти, яку ви маєте (або натисніть Enter для завершення): ")
    if source_currency:
        target_currency = input("Введіть код валюти, в яку ви хочете обміняти: ")
        amount = float(input("Введіть суму грошей, яку ви маєте: "))
