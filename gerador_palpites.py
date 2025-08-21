# --- Gerador de Palpites para Sorteio ---

import random

print("--- Gerador de Palpites da Sorte ---")

numeros_sorteados = []
quantidade = 6 # Altere aqui para quantos números você quer

while len(numeros_sorteados) < quantidade:
    numero = random.randint(1, 60)
    if numero not in numeros_sorteados:
        numeros_sorteados.append(numero)

numeros_sorteados.sort() # Deixa os números em ordem

print("\nSeus números da sorte são:")
print(numeros_sorteados)
