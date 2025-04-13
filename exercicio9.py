numero = 1
i = 1
lista_divisores = []
lista_perfeitos = []

for numero in range(1, 10001):
    lista_divisores = []
    soma = 0
    for i in range(1, numero):
        resto = numero % i

        if resto == 0:
            lista_divisores.append(i)

        i += 1

    soma = sum(lista_divisores)
    if numero == soma:
        lista_perfeitos.append(numero)

    numero += 1

print(lista_perfeitos)