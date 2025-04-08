usuario = int(input("Digite um número: "))
soma = 0
numero = 0

if usuario > 0:
    while numero <= usuario:
        soma = soma + numero
        numero += 1
    print(f"A soma de todos os números de 1 até {usuario} é: {soma}")
else:
    print("INVALIDO")