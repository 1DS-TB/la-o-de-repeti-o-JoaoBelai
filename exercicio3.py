numero = int(input("Digite um número que deseja ver a tabuada: "))


for conta in range(1,11):
    resultado = numero * conta
    print(f"{numero} x {conta} = {resultado}")
