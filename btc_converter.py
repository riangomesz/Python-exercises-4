import requests

# URL da API do Mercado Bitcoin
url = 'https://www.mercadobitcoin.net/api/BTC/ticker/'

# Solicita a cotação atual do Bitcoin em reais
response = requests.get(url)
data = response.json()
btc_rate = float(data['ticker']['last'])

# Solicita o valor em reais a ser convertido em Bitcoin
brl_amount = float(input('Digite o valor em reais a ser convertido em Bitcoin: '))

# Converte o valor em reais em Bitcoin
btc_amount = brl_amount / btc_rate

# Imprime o resultado
print(f'{brl_amount:.2f} reais = {btc_amount:.8f} Bitcoin')
