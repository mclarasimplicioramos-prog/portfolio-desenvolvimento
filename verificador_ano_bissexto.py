# --- Verificador de Ano Bissexto ---

ano = int(input("Digite um ano para verificar se é bissexto: "))

# Regras para ser bissexto:
# 1. Divisível por 4, mas não por 100.
# 2. A menos que seja divisível por 400.

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano de {ano} é um ano bissexto!")
else:
    print(f"O ano de {ano} não é um ano bissexto.")
