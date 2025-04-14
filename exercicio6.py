numero = int(input("Escreva quantos números da sequência de Fibonacci você quer: "))

fibo_agora = 1
fibo_anterior = 0
lista = []
i = 0
if numero < 0:
    print("INVALIDO")
else:
    while i < numero:
        fibo_agora, fibo_anterior = fibo_anterior, fibo_agora + fibo_anterior
        lista.append(fibo_agora)
        i += 1
    print(lista)
