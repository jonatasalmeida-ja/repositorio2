import random

numeros = []

for i in range(1, 11):
    num_aleatorio = random.randint(1, 100)
    numeros.append(num_aleatorio)

print(numeros)
print(sum(numeros))