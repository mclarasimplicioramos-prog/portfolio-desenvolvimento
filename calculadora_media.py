# --- Calculadora de Média de Notas ---

print("Vamos calcular a sua média. Digite 'fim' quando terminar de adicionar as notas.")

notas = []
entrada_usuario = ""

while entrada_usuario.lower() != "fim":
    entrada_usuario = input("Digite uma nota (ou 'fim' para calcular): ")
    if entrada_usuario.lower() != "fim":
        try:
            notas.append(float(entrada_usuario))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("\n--- Resultado ---")
    print(f"As notas digitadas foram: {notas}")
    print(f"A média final é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida para calcular a média.")
