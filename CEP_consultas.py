import requests

res = requests.get('https://cep.awesomeapi.com.br/json/30140100')

res.json()
