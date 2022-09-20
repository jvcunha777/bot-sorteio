import math
import random

numero = input('escreva o numero de sorteados:')
lista = []


i = 1
while i <= int(numero):
    nome = input('escreva o nome#'+str(i)+ ':')
    lista.append(nome)
    i += 1
print('pessoas a ser sorteadas',len(lista))

sorteio = random.choice(lista)

print('primeiro a apresentar',sorteio)