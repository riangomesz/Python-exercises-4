def dec2bin(numero):
  """
  Converte um número decimal para binário.

  Args:
    numero: O número decimal a ser convertido.

  Returns:
    O número binário convertido como um `str`.
  """

  pilha = []
  while numero > 0:
    res = numero % 2
    pilha.append(res)
    numero //= 2

  binario = ""
  for item in pilha:
    binario += str(item)

  return binario

def main():
  numero_decimal = int(input("Digite um número decimal: "))
  numero_binario = dec2bin(numero_decimal)
  print("O " + str(numero_decimal) + " foi convertido em binário: "+numero_binario)

if __name__ == "__main__":
  main()
