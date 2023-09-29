#Algoritmo que calcula o fatorial de n

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
print(fatorial(6))
