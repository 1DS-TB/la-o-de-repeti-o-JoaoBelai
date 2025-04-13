import math

comeco = int(input("Digite um número para começar a verificação: "))
final = int(input("Digite um número para finalizar a verificação: "))

str_esquerda = ""
str_direita = ""
int_esquerda = 0
int_direita = 0
kaprekar = []
quadrado = 0

if comeco < 0 or final < 0:
    print("INVALIDO")
elif comeco > final:
    print("INVALIDO")
else:
    for numero in range(comeco, final + 1):
        str_esquerda = ""
        str_direita = ""
        quadrado = int(quadrado)
        quadrado = 0

        quadrado = numero ** 2
        quadrado = str(quadrado)

        meio = len(quadrado) / 2
        meio = math.floor(meio)

        str_esquerda = quadrado[0: meio]
        str_direita = quadrado[meio: len(quadrado)]

        if str_esquerda != '':
            int_esquerda = int(str_esquerda)
        if str_direita != '':
            int_direita = int(str_direita)

        soma = int_direita + int_esquerda

        if soma == numero:
            kaprekar.append(numero)

    if 0 in kaprekar:
        kaprekar.remove(0)
    print(kaprekar)
