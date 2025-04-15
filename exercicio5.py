numero = int(input("Digite um número que você gostaria de saber se é primo: "))
divisor = 2
primo = True

if numero == 1:
    print("1 não eh primo")
elif numero > 0:
    while divisor <= numero:
        resto = numero % divisor
        if numero == divisor:
            if primo == True:
                print("Número primo")
                divisor += 1
            else:
                print("Não é primo")
                divisor += 1
        else:
            if resto == 0:
                primo = False
                divisor += 1
            else:
                divisor += 1
else:
    print("INVALIDO")
