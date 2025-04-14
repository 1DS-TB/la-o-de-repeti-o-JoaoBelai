numero = int(input("Digite um número que deseja ver a tabuada: "))

if numero < 0:
    print("INVALIDO")
else:
    for conta in range(1,11):
        resultado = numero * conta
        print(f"{numero} x {conta} = {resultado}")
