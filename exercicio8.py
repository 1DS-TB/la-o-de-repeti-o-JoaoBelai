numero = int(input("Digite um número inteiro positivo, para fazermos a soma da série harmônica: "))

i = 1
soma = 0
if numero >= 0:
    while i <= numero:
        soma = soma + (1/i)
        i+=1
    print(f"\nA soma harmônica é: {soma:.2f}")
else:
    print("INVALIDO")
