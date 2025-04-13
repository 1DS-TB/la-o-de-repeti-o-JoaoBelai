numero = int(input("Digite um número inteiro positivo: "))

if numero > 0:
    i = 1
    elemento = "*"
    elementos = ""
    while i <= numero:
        print(elemento + elementos)
        elementos += elemento
        i += 1
else:
    print("INVALIDO")