numero = int(input("Digite um número que deseja ver a tabuada: "))

if numero <= 0:
    print("INVALIDO")
else:
    for conta in range(0,11):
        resultado = numero * conta
        print(f"{numero} * {conta} = {resultado}")
