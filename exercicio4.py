numero = int(input("Digite um número para calcularmos o fatorial: "))
indice = 1
multiplicacao = 1

if numero >=0:
    while indice <= numero:
        multiplicacao = multiplicacao * indice
        indice += 1
    print(f"O fatorial de {numero} é: {multiplicacao}")
else:
    print("INVALIDO")