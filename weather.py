# Código que #

import requests

apiKey = 'b5647a2a3eaf4416830181957230105'
city = 'Belo Horizonte'

response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}')
data = response.json()

temperature = data['current']['temp_c']
description = data['current']['condition']['text']

print(f'Em {city}, a temperatura atual é de {temperature} graus Celsius e o tempo está {description}.')
