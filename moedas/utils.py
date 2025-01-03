import requests

CURRENCY_NAMES = {
  "USD": "Dólares dos Estados Unidos da América",
  "BRL": "Real",
  "EUR": "Euro"
}

EXCHANGE_RATES = {
  "USD": {
      "BRL": 5.80,
      "EUR": 0.85
  },
  "BRL":{
      "USD": 1 / 5.8,
      "EUR": 1 / 6.15
  }
}

def get_exchange_rate(from_code, to_code, kind='ask'):
  # return EXCHANGE_RATES[from_code][to_code]
  url = 'https://economia.awesomeapi.com.br/last/{}-{}'
  r = requests.get(url.format(from_code, to_code))
  rate = r.json()[f'{from_code}{to_code}'][kind]
  return float(rate)