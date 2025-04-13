import random

opcao = 0
escolha = ["atacar", "curar"]
rodada = 1
cura_max = 20

while opcao != 2:
    opcao = int(input("\n1.Jogar"
                      "\n2.Sair"
                      "\nEscreva o número de uma opção para escolher: "))
    if opcao == 1:
        vida_max = random.randint(200,1000)
        vida_jogador = vida_max
        atq_jogador = random.randint(1,50)
        def_jogador = random.randint(1,50)
        vida_cpu = vida_max
        atq_cpu = random.randint(1,50)
        def_cpu = random.randint(1,50)

        while atq_jogador <= def_cpu:
            atq_jogador = random.randint(1, 50)
        while atq_cpu <= def_jogador:
            atq_cpu = random.randint(1, 50)

        print("===== Duelo de Heróis =====")
        print(f"\n===== Você ======"
              f"\nHP: {vida_jogador}"
              f"\nATQ: {atq_jogador}        DEF: {def_jogador}")
        print(f"\n===== Inimigo ======"
              f"\nHP: {vida_cpu}"
              f"\nATQ: {atq_cpu}        DEF: {def_cpu}")

        while True:
            print(f"\n----- Rodada {rodada} -----")
            print(f"Você HP: {vida_jogador} | Inimigo HP: {vida_cpu}")

            while True:
                escolha_jogador = int(input("\nSua Vez"
                                            "\n[1] Atacar"
                                            "\n[2] Curar"
                                            "\nO que você deseja fazer: "))

                if escolha_jogador == 1:
                    break

                elif escolha_jogador == 2:
                    if vida_jogador == vida_max:
                        print("Você já está com vida máxima.")
                    else:
                        break
                else:
                    print("Opção inválida. Tente novamente.")

            if escolha_jogador == 1:
                vida_perdida = atq_jogador - def_cpu
                vida_cpu = vida_cpu - vida_perdida
                print(f"Você ataca o inimigo! ele perde {vida_perdida} de HP")

            elif escolha_jogador == 2:
                cura = vida_max - vida_jogador

                if cura < cura_max:
                    vida_jogador = vida_jogador + cura
                    print(f"Você se cura em {cura} de HP!")
                else:
                    vida_jogador = vida_jogador + cura_max
                    print(f"Você se cura em 20 de HP!")

            escolha_cpu = random.choice(escolha)

            if escolha_cpu == "curar":
                while vida_cpu == vida_max:
                    escolha_cpu = random.choice(escolha)

            if escolha_cpu == "atacar":
                vida_perdida = atq_cpu - def_jogador
                vida_jogador = vida_jogador - vida_perdida
                print(f"O inimigo te ataca! você perde {vida_perdida} de HP")
            else:
                cura = vida_max - vida_cpu

                if cura < cura_max:
                    vida_cpu = vida_cpu + cura
                    print(f"O inimigo se cura em {cura} de HP!")
                else:
                    vida_cpu = vida_cpu + cura_max
                    print(f"O inimigo se cura em 20 de HP!")

            rodada += 1

            if vida_jogador <= 0:
                print(f"\nO inimigo ganhou, tente novamente")
                break
            elif vida_cpu <= 0:
                print(f"\nParabéns você ganhou")
                break

    elif opcao == 2:
        print("\nSaindo...")
    else:
        print("\nINVALIDO")