import requests

cep = int(input("Digite seu cep: "))
cep = str(cep)
response = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
print(response.text)
print(response.json())
dados_cep = response.json()
print(dados_cep['logradouro'])
