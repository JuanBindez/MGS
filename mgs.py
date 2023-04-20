import random

while len(numeros_sorteados) < 6:
    numero = random.randint(1, 60)
    if numero not in numeros_sorteados:
        numeros_sorteados.append(numero)

        if len(numeros_sorteados) == 1:
            card_1 = numero
        elif len(numeros_sorteados) == 2:
            card_2 = numero
        elif len(numeros_sorteados) == 3:
            card_3 = numero
        elif len(numeros_sorteados) == 4:
            card_4 = numero
        elif len(numeros_sorteados) == 5:
            card_5 = numero
        else:
            card_6 = numero


print(card_1)
print(card_2)
print(card_3)
print(card_4)
print(card_5)
print(card_6)
