# Antes de iniciar o desenvolvimento do código, fui no powershell e instalei o pacote 'requests'.
# Após isso desenvolvi o programa que faz com que o usuário informe seu cep.
# Depois ele imprime na tela os dados de sua casa. A partir de uma API web que busca "ceps" online.

import requests

cep = int(input("Digite seu cep: "))
cep = str(cep)
response = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
print(response.text)
print(response.json())
dados_cep = response.json()
print(dados_cep['logradouro'])
