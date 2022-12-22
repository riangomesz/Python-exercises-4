# Antes de iniciar o desenvolvimento do código, fui no powershell e instalei o pacote 'requests'.
# Após isso desenvolvi o programa que faz com que o usuário informe seu cep.
# Depois ele imprime na tela os dados de sua casa. A partir de uma API web que busca "ceps" online.

import requests

cep = int(input("Digite seu cep: "))
cep = str(cep)
response = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
print(response.text)
dados_cep = response.json()
print('Sua rua '+dados_cep['logradouro'])
print('Seu ddd '+dados_cep['ddd'])
print('Seu bairro '+dados_cep['bairro'])
print('Sua cidade '+dados_cep['localidade'])
print('Seu estado '+dados_cep['uf'])

