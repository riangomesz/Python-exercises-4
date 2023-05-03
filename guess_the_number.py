import random

def main():
    print("Bem-vindo ao jogo 'Adivinhe o número'!")
    print("Estou pensando em um número entre 1 e 10.")
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    while True:
        tentativas += 1
        palpite = int(input("Digite seu palpite: "))

        if palpite < numero_secreto:
            print("Seu palpite é muito baixo. Tente novamente.")
        elif palpite > numero_secreto:
            print("Seu palpite é muito alto. Tente novamente.")
        else:
            print("Parabéns! Você acertou em", tentativas, "tentativas.")
            break

if __name__ == '__main__':
    main()
