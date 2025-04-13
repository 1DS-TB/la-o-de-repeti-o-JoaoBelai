import random

opcao = 0
escolha = ["atacar", "curar", "item", "poder"]
escolha_item = []
escolha_poder = []
rodada = 1
cura_max = 20

buffer_usado_j1 = False
loop_usado_j1 = False
tela_usado_j1 = False
cache_usado_j1 = False

buffer_usado_j2 = False
loop_usado_j2 = False
tela_usado_j2 = False
cache_usado_j2 = False

buffer_usado_cpu = False
loop_usado_cpu = False
tela_usado_cpu = False
cache_usado_cpu = False

buffer_turnos_j1 = 0
loop_turnos_j1 = 0
tela_turnos_j1 = 0

buffer_turnos_j2 = 0
loop_turnos_j2 = 0
tela_turnos_j2 = 0

buffer_turnos_cpu = 0
loop_turnos_cpu = 0
tela_turnos_cpu = 0

item1 = False
item2 = False
item3 = False
item4 = False

item1_j2 = False
item2_j2 = False
item3_j2 = False
item4_j2 = False

item1_cpu = False
item2_cpu = False
item3_cpu = False
item4_cpu = False

forca_ativa = 0
escudo_ativo = 0
amolar_ativo = 0

forca_ativa_j2 = 0
escudo_ativo_j2 = 0
amolar_ativo_j2 = 0

forca_ativa_cpu = 0
escudo_ativo_cpu = 0
amolar_ativo_cpu = 0

while opcao != 3:
    opcao = int(input("\n1.Multi Player"
                      "\n2.Single Player"
                      "\n3.Sair"
                      "\nEscreva o número de uma opção para escolher: "))
    if opcao == 1:
        vida_max = random.randint(200, 1000)
        vida_jogador1 = vida_max
        atq_jogador1 = random.randint(1, 50)
        def_jogador1 = random.randint(1, 50)
        vida_jogador2 = vida_max
        atq_jogador2 = random.randint(1, 50)
        def_jogador2 = random.randint(1, 50)

        while atq_jogador1 <= def_jogador2:
            atq_jogador1 = random.randint(1, 50)
        while atq_jogador2 <= def_jogador1:
            atq_jogador2 = random.randint(1, 50)

        print("===== Duelo de Heróis =====")
        print(f"\n===== Jogador 1 ======"
                f"\nHP: {vida_jogador1}"
                f"\nATQ: {atq_jogador1}        DEF: {def_jogador1}")
        print(f"\n===== Jogador 2 ======"
                f"\nHP: {vida_jogador2}"
                f"\nATQ: {atq_jogador2}        DEF: {def_jogador2}")

        while True:
            print(f"\n----- Rodada {rodada} -----")
            print(f"Jogador 1 HP: {vida_jogador1} | Jogador 2 HP: {vida_jogador2}")

            if loop_turnos_j1 > 0:
                print("O jogador 1 perde sua rodada por estar em um Loop Infinito")
                loop_turnos_j1 = loop_turnos_j1 - 1
            else:
                while True:
                    escolha_jogador1 = int(input("\nSua Vez jogador 1"
                                                "\n[1] Atacar"
                                                "\n[2] Curar"
                                                "\n[3] Usar item"
                                                "\n[4] Poder Especial"
                                                "\nO que você deseja fazer: "))

                    if escolha_jogador1 == 1:
                        break

                    elif escolha_jogador1 == 2:
                        if vida_jogador1 == vida_max:
                            print("Você já está com vida máxima.")
                        else:
                            break

                    elif escolha_jogador1 == 3:
                        if item1 and item2 and item3 and item4:
                            print("Você já usou todos os seus itens!")
                        else:
                            while True:
                                item = int(input("\nItens:"
                                                "\n[1] Poção de Força"
                                                "\n[2] Escudo Reforçado"
                                                "\n[3] Pedra de Amolar"
                                                "\n[4] Bola de fogo"
                                                "\n[5] Voltar"
                                                "\nEscolha um item: "))

                                if item == 1 and not item1:
                                    print("Jogador 1 usou a Poção de Força! Sua força será dobrada nos próximos 2 turnos")
                                    item1 = True
                                    forca_ativa = 2
                                    break
                                elif item == 2 and not item2:
                                    print("Jogador 1 usou o Escudo Reforçado! Sua defesa será dobrada nos próximos 2 turnos")
                                    item2 = True
                                    escudo_ativo = 2
                                    break
                                elif item == 3 and not item3:
                                    print("Jogador 1 usou a Pedra de Amolar! Seu ataque dará o dobro de dano nos próximos 2 turnos")
                                    item3 = True
                                    amolar_ativo = 2
                                    break
                                elif item == 4 and not item4:
                                    dano_explosivo = random.randint(30, 50)
                                    vida_jogador2 = vida_jogador2 - dano_explosivo
                                    print(f"Jogador 1 usou Bola de fogo e causou {dano_explosivo} de dano!")
                                    item4 = True
                                    break
                                elif item == 5:
                                    print("Voltando ao menu principal...")
                                    break
                                else:
                                    print("Item inválido ou já foi usado.")
                            if item != 5:
                                break
                    elif escolha_jogador1 == 4:
                        if buffer_usado_j1 and tela_usado_j1 and loop_usado_j1 and cache_usado_j1:
                            print("Você já utilizou todos os seus poderes!")
                        else:
                            while True:
                                poder = int(input("\nPoderes:"
                                                 "\n[1] Buffer Overflow"
                                                 "\n[2] Loop Infinito"
                                                 "\n[3] Tela Azul"
                                                 "\n[4] Cache Hit"
                                                 "\n[5] Voltar"
                                                 "\nEscolha um poder: "))

                                if poder == 1 and not buffer_usado_j1:
                                    print("Buffer Overflow lançado em jogador 2! Nos próximos 2 turnos ele perderá o equivalente a 5% da sua vida!")
                                    buffer_usado_j1 = True
                                    buffer_turnos_j2 = 2
                                    break
                                elif poder == 2 and not loop_usado_j1:
                                    print("Loop Infinito ativado! O jogador 2 perderá o próximo turno")
                                    loop_usado_j1 = True
                                    loop_turnos_j2 = 1
                                    break
                                elif poder == 3 and not tela_usado_j1:
                                    print("Tela Azul! A defesa do jogador 2 foi reduzida a 0 por 2 turnos")
                                    tela_usado_j1 = True
                                    tela_turnos_j2 = 2
                                    break
                                elif poder == 4 and not cache_usado_j1:
                                    if vida_jogador1 < vida_max * 0.25:
                                        cura = int(vida_max * 0.30)
                                        vida_jogador1 = vida_jogador1 + cura
                                        cache_usado_j1 = True
                                        print(f"Jogador 1 usa Cache Hit e se cura em {cura} de HP.")
                                    else:
                                        print("Cache Hit só pode ser usado com menos de 25% de HP.")

                                elif poder == 5:
                                    print("Voltando ao menu principal...")
                                    break
                                else:
                                    print("Poder inválido ou já foi usado.")
                            if poder != 5:
                                break
                    else:
                        print("Opção inválida. Tente novamente.")

                if buffer_turnos_j1 > 0:
                    dano = int(vida_max * 0.05)
                    vida_jogador1 = vida_jogador1 - dano
                    buffer_turnos_j1 = buffer_turnos_j1 - 1
                    print(f"O jogador 1 perde {dano} de HP pelo Buffer Overflow")

                if escolha_jogador1 == 1:
                    critico = random.randint(1, 10)

                    atq = atq_jogador1
                    defesa = def_jogador2

                    if tela_turnos_j2 > 0:
                        defesa = 0
                        tela_turnos_j2 = tela_turnos_j2 - 1

                    if forca_ativa > 0:
                        atq = atq * 2
                        forca_ativa = forca_ativa - 1

                    if escudo_ativo_j2 > 0:
                        defesa = defesa * 2
                        escudo_ativo_j2 = escudo_ativo_j2 - 1

                    if critico == 10:
                        vida_perdida = max(0, atq - defesa)
                        vida_perdida = vida_perdida * 2
                        if amolar_ativo > 0:
                            vida_perdida = vida_perdida * 2
                            amolar_ativo = amolar_ativo - 1
                        vida_jogador2 = vida_jogador2 - vida_perdida
                        print(f"ATAQUE CRÍTICO! o jogador 2 perde {vida_perdida} de HP")
                    else:
                        vida_perdida = max(0, atq - defesa)
                        if amolar_ativo > 0:
                            vida_perdida = vida_perdida * 2
                            amolar_ativo = amolar_ativo - 1
                        vida_jogador2 = vida_jogador2 - vida_perdida
                        print(f"Você ataca o jogador 2! ele perde {vida_perdida} de HP")

                elif escolha_jogador1 == 2:
                    cura = vida_max - vida_jogador1

                    if cura < cura_max:
                        vida_jogador1 = vida_jogador1 + cura
                        print(f"Jogador 1 se cura em {cura} de HP!")
                    else:
                        vida_jogador1 = vida_jogador1 + cura_max
                        print(f"Jogador 1 se cura em 20 de HP!")


            if loop_turnos_j2 > 0:
                print("O jogador 2 perde sua rodada por estar em um Loop Infinito")
                loop_turnos_j2 = loop_turnos_j2 - 1
            else:
                while True:
                    escolha_jogador2 = int(input("\nSua Vez jogador 2"
                                                 "\n[1] Atacar"
                                                 "\n[2] Curar"
                                                 "\n[3] Usar item"
                                                 "\n[4] Poder Especial"
                                                 "\nO que você deseja fazer: "))

                    if escolha_jogador2 == 1:
                        break

                    elif escolha_jogador2 == 2:
                        if vida_jogador2 == vida_max:
                            print("Você já está com vida máxima.")
                        else:
                            break

                    elif escolha_jogador2 == 3:
                        if item1_j2 and item2_j2 and item3_j2 and item4_j2:
                            print("Você já usou todos os seus itens!")
                        else:
                            while True:
                                item_j2 = int(input("\nItens:"
                                                    "\n[1] Poção de Força"
                                                    "\n[2] Escudo Reforçado"
                                                    "\n[3] Pedra de Amolar"
                                                    "\n[4] Bola de fogo"
                                                    "\n[5] Voltar"
                                                    "\nEscolha um item: "))

                                if item_j2 == 1 and not item1_j2:
                                    print("Jogador 2 usou a Poção de Força! Sua força será dobrada nos próximos 2 turnos")
                                    item1_j2 = True
                                    forca_ativa_j2 = 2
                                    break
                                elif item_j2 == 2 and not item2_j2:
                                    print("Jogador 2 usou o Escudo Reforçado! Sua defesa será dobrada nos próximos 2 turnos")
                                    item2_j2 = True
                                    escudo_ativo_j2 = 2
                                    break
                                elif item_j2 == 3 and not item3_j2:
                                    print("Jogador 2 usou a Pedra de Amolar! Seu ataque dará o dobro de dano nos próximos 2 turnos")
                                    item3_j2 = True
                                    amolar_ativo_j2 = 2
                                    break
                                elif item_j2 == 4 and not item4_j2:
                                    dano_explosivo = random.randint(30, 50)
                                    vida_jogador1 = vida_jogador1 - dano_explosivo
                                    print(f"Jogador 2 usou Bola de fogo e causou {dano_explosivo} de dano!")
                                    item4_j2 = True
                                    break
                                elif item_j2 == 5:
                                    print("Voltando ao menu principal...")
                                    break
                                else:
                                    print("Item inválido ou já foi usado.")
                            if item_j2 != 5:
                                break

                    elif escolha_jogador2 == 4:
                        if buffer_usado_j2 and tela_usado_j2 and loop_usado_j2 and cache_usado_j2:
                            print("Você já utilizou todos os seus poderes!")
                        else:
                            while True:
                                poder = int(input("\nPoderes:"
                                                 "\n[1] Buffer Overflow"
                                                 "\n[2] Loop Infinito"
                                                 "\n[3] Tela Azul"
                                                 "\n[4] Cache Hit"
                                                 "\n[5] Voltar"
                                                 "\nEscolha um poder: "))

                                if poder == 1 and not buffer_usado_j2:
                                    print("Buffer Overflow lançado em jogador 1! Nos próximos 2 turnos ele perderá o equivalente a 5% da sua vida!")
                                    buffer_usado_j2 = True
                                    buffer_turnos_j1 = 2
                                    break
                                elif poder == 2 and not loop_usado_j2:
                                    print("Loop Infinito ativado! O jogador 1 perderá o próximo turno")
                                    loop_usado_j2 = True
                                    loop_turnos_j1 = 1
                                    break
                                elif poder == 3 and not tela_usado_j2:
                                    print("Tela Azul! A defesa do jogador 1 foi reduzida a 0 por 2 turnos")
                                    tela_usado_j2 = True
                                    tela_turnos_j1 = 2
                                    break
                                elif poder == 4 and not cache_usado_j2:
                                    if vida_jogador2 < vida_max * 0.25:
                                        cura = int(vida_max * 0.30)
                                        vida_jogador2 = vida_jogador2 + cura
                                        cache_usado_j2 = True
                                        print(f"Jogador 2 usa Cache Hit e se cura em {cura} de HP.")
                                    else:
                                        print("Cache Hit só pode ser usado com menos de 25% de HP.")

                                elif poder == 5:
                                    print("Voltando ao menu principal...")
                                    break
                                else:
                                    print("Poder inválido ou já foi usado.")
                            if poder != 5:
                                break
                    else:
                        print("Opção inválida. Tente novamente.")

                if buffer_turnos_j2 > 0:
                    dano = int(vida_max * 0.05)
                    vida_jogador2 = vida_jogador2 - dano
                    buffer_turnos_j2 = buffer_turnos_j2 - 1
                    print(f"O jogador 2 perde {dano} de HP pelo Buffer Overflow")

                if escolha_jogador2 == 1:
                    critico = random.randint(1, 10)

                    atq = atq_jogador2
                    defesa = def_jogador1

                    if tela_turnos_j1 > 0:
                        defesa = 0
                        tela_turnos_j1 = tela_turnos_j1 - 1

                    if forca_ativa_j2 > 0:
                        atq= atq * 2
                        forca_ativa_j2 = forca_ativa_j2 - 1

                    if escudo_ativo > 0:
                        defesa = defesa * 2
                        escudo_ativo = escudo_ativo - 1

                    if critico == 10:
                        vida_perdida = max(0, atq - defesa)
                        vida_perdida = vida_perdida * 2
                        if amolar_ativo_j2 > 0:
                            vida_perdida = vida_perdida * 2
                            amolar_ativo_j2 = amolar_ativo_j2 - 1
                        vida_jogador1 = vida_jogador1 - vida_perdida
                        print(f"ATAQUE CRÍTICO! o jogador 1 perde {vida_perdida} de HP")
                    else:
                        vida_perdida = max(0, atq - defesa)
                        if amolar_ativo_j2 > 0:
                            vida_perdida = vida_perdida * 2
                            amolar_ativo_j2 = amolar_ativo_j2 - 1
                        vida_jogador1 = vida_jogador1 - vida_perdida
                        print(f"Você ataca o jogador 1! ele perde {vida_perdida} de HP")

                elif escolha_jogador2 == 2:
                    cura = vida_max - vida_jogador2

                    if cura < cura_max:
                        vida_jogador2 = vida_jogador2 + cura
                        print(f"Jogador 2 se cura em {cura} de HP!")
                    else:
                        vida_jogador2 = vida_jogador2 + cura_max
                        print(f"Jogador 2 se cura em 20 de HP!")

            rodada += 1

            if vida_jogador1 <= 0:
                print(f"\nO jogador 2 ganhou, parabéns")
                break
            elif vida_jogador2 <= 0:
                print(f"\nO jogador 1 ganhou, parabéns")
                break

    if opcao == 2:
        vida_max = random.randint(200, 1000)
        vida_jogador = vida_max
        atq_jogador = random.randint(1, 50)
        def_jogador = random.randint(1, 50)
        vida_cpu = vida_max
        atq_cpu = random.randint(1, 50)
        def_cpu = random.randint(1, 50)

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

            if loop_turnos_j1 > 0:
                print("Você perde sua rodada por estar em um Loop Infinito")
                loop_turnos_j1 = loop_turnos_j1 - 1
            else:
                while True:
                    escolha_jogador = int(input("\nSua Vez"
                                                "\n[1] Atacar"
                                                "\n[2] Curar"
                                                "\n[3] Usar item"
                                                "\n[4] Poder especial"
                                                "\nO que você deseja fazer: "))

                    if escolha_jogador == 1:
                        break

                    elif escolha_jogador == 2:
                        if vida_jogador == vida_max:
                            print("Você já está com vida máxima.")
                        else:
                            break

                    elif escolha_jogador == 3:
                        if item1 and item2 and item3 and item4:
                            print("Você já usou todos os seus itens!")
                        else:
                            while True:
                                item = int(input("\nItens:"
                                                 "\n[1] Poção de Força" 
                                                 "\n[2] Escudo Reforçado" 
                                                 "\n[3] Pedra de Amolar" 
                                                 "\n[4] Bola de fogo"
                                                 "\n[5] Voltar"
                                                 "\nEscolha um item: "))

                                if item == 1 and not item1:
                                    print("Você usou a Poção de Força! Sua força será dobrada nos próximos 2 turnos")
                                    item1 = True
                                    forca_ativa = 2
                                    break
                                elif item == 2 and not item2:
                                    print("Você usou o Escudo Reforçado! Sua defesa será dobrada nos próximos 2 turnos")
                                    item2 = True
                                    escudo_ativo = 2
                                    break
                                elif item == 3 and not item3:
                                    print("Você usou a Pedra de Amolar! Seu ataque dará o dobro de dano nos próximos 2 turnos")
                                    item3 = True
                                    amolar_ativo = 2
                                    break
                                elif item == 4 and not item4:
                                    dano_explosivo = random.randint(30,50)
                                    vida_cpu = vida_cpu - dano_explosivo
                                    print(f"Você usou Bola de fogo e causou {dano_explosivo} de dano!")
                                    item4 = True
                                    break
                                elif item == 5:
                                    print("Voltando ao menu principal...")
                                    break
                                else:
                                    print("Item inválido ou já foi usado.")
                            if item != 5:
                                break

                    elif escolha_jogador == 4:
                        if buffer_usado_j1 and tela_usado_j1 and loop_usado_j1 and cache_usado_j1:
                            print("Você já utilizou todos os seus poderes!")
                        else:
                            while True:
                                poder = int(input("\nPoderes:"
                                                  "\n[1] Buffer Overflow"
                                                  "\n[2] Loop Infinito"
                                                  "\n[3] Tela Azul"
                                                  "\n[4] Cache Hit"
                                                  "\n[5] Voltar"
                                                  "\nEscolha um poder: "))

                                if poder == 1 and not buffer_usado_j1:
                                    print("Buffer Overflow lançado no inimigo! Nos próximos 2 turnos ele perderá o equivalente a 5% da sua vida!")
                                    buffer_usado_j1 = True
                                    buffer_turnos_cpu = 2
                                    break
                                elif poder == 2 and not loop_usado_j1:
                                    print("Loop Infinito ativado! O inimigo perderá o próximo turno")
                                    loop_usado_j1 = True
                                    loop_turnos_cpu = 1
                                    break
                                elif poder == 3 and not tela_usado_j1:
                                    print("Tela Azul! A defesa do inimigo foi reduzida a 0 por 2 turnos")
                                    tela_usado_j1 = True
                                    tela_turnos_cpu = 2
                                    break
                                elif poder == 4 and not cache_usado_j1:
                                    if vida_jogador < vida_max * 0.25:
                                        cura = int(vida_max * 0.30)
                                        vida_jogador = vida_jogador + cura
                                        cache_usado_j1 = True
                                        print(f"Você usa Cache Hit e se cura em {cura} de HP.")
                                    else:
                                        print("Cache Hit só pode ser usado com menos de 25% de HP.")

                                elif poder == 5:
                                    print("Voltando ao menu principal...")
                                    break

                                else:
                                    print("Poder inválido ou já foi usado.")

                            if poder != 5:
                                break
                    else:
                        print("Opção inválida. Tente novamente.")

                if buffer_turnos_j1 > 0:
                    dano = int(vida_max * 0.05)
                    vida_jogador = vida_jogador - dano
                    buffer_turnos_j1 = buffer_turnos_j1 - 1
                    print(f"Você perde {dano} de HP pelo Buffer Overflow")

                if escolha_jogador == 1:
                    critico = random.randint(1,10)

                    atq = atq_jogador
                    defesa = def_cpu

                    if tela_turnos_cpu > 0:
                        defesa = 0
                        tela_turnos_cpu = tela_turnos_cpu - 1

                    if forca_ativa > 0:
                        atq = atq * 2
                        forca_ativa = forca_ativa - 1

                    if escudo_ativo_cpu > 0:
                        defesa = defesa * 2
                        escudo_ativo_cpu = escudo_ativo_cpu -1

                    if critico == 10:
                        vida_perdida = max(0, atq - defesa)
                        vida_perdida = vida_perdida * 2
                        if amolar_ativo > 0:
                            vida_perdida = vida_perdida * 2
                            amolar_ativo = amolar_ativo - 1
                        vida_cpu = vida_cpu - vida_perdida
                        print(f"ATAQUE CRÍTICO! o inimigo perde {vida_perdida} de HP")
                    else:
                        vida_perdida = max(0, atq - defesa)
                        if amolar_ativo > 0:
                            vida_perdida = vida_perdida * 2
                            amolar_ativo = amolar_ativo - 1
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

            if loop_turnos_cpu > 0:
                print("O inimigo perde sua rodada por estar em um Loop Infinito")
                loop_turnos_cpu = loop_turnos_cpu - 1
            else:
                escolha_cpu = random.choice(escolha)

                if buffer_turnos_cpu > 0:
                    dano = int(vida_max * 0.05)
                    vida_cpu = vida_cpu - dano
                    buffer_turnos_cpu = buffer_turnos_cpu - 1
                    print(f"O inimigo perde {dano} de HP pelo Buffer Overflow")

                if escolha_cpu == "curar":
                    while vida_cpu == vida_max:
                        escolha_cpu = random.choice(escolha)

                if escolha_cpu == "poder":
                    if buffer_usado_cpu and loop_usado_cpu and tela_usado_cpu and cache_usado_cpu:
                        while escolha_cpu == "poder":
                            escolha_cpu =random.choice(escolha)

                if escolha_cpu == "item":
                    if item1_cpu and item2_cpu and item3_cpu and item4_cpu:
                        while escolha_cpu == "item":
                            escolha_cpu = random.choice(escolha)

                if escolha_cpu == "poder":
                    poder_cpu = random.randint(1, 4)
                    while poder_cpu in escolha_poder:
                        poder_cpu = random.randint(1, 4)

                    escolha_poder.append(poder_cpu)

                    if poder_cpu == 4 and not cache_usado_cpu:
                        if vida_cpu < vida_max * 0.25:
                            cura = int(vida_max * 0.30)
                            vida_cpu = vida_cpu + cura
                            cache_usado_cpu = True
                            print(f"O inimigo usa Cache Hit e se cura em {cura} de HP.")
                        else:
                            escolha_poder.remove(poder_cpu)
                            poder_cpu = random.randint(1, 3)
                            while poder_cpu in escolha_poder:
                                poder_cpu = random.randint(1, 3)

                            escolha_poder.append(poder_cpu)

                    elif poder_cpu == 1 and not buffer_usado_cpu:
                        print("Buffer Overflow lançado no em Você! Nos próximos 2 turnos você perderá o equivalente a 5% da sua vida!")
                        buffer_usado_cpu = True
                        buffer_turnos_j1 = 2

                    elif poder_cpu == 2 and not loop_usado_cpu:
                        print("Loop Infinito ativado! Você perderá o próximo turno")
                        loop_usado_cpu = True
                        loop_turnos_j1 = 1

                    elif poder_cpu == 3 and not tela_usado_cpu:
                        print("Tela Azul! A sua defesa foi reduzida a 0 por 2 turnos")
                        tela_usado_cpu = True
                        tela_turnos_j1 = 2

                elif escolha_cpu == "item":
                    item_cpu = random.randint(1, 4)
                    while item_cpu in escolha_item:
                        item_cpu = random.randint(1, 4)

                    escolha_item.append(item_cpu)

                    if item_cpu == 1 and not item1_cpu:
                        print("O inimigo usou a Poção de Força! O ataque dele será dobrado nos próximos 2 turnos")
                        item1_cpu = True
                        forca_ativa_cpu = 2

                    elif item_cpu == 2 and not item2_cpu:
                        print("O inimigo usou o Escudo Reforçado! A defesa dele será dobrada nos próximos 2 turnos")
                        item2_cpu = True
                        escudo_ativo_cpu = 2

                    elif item_cpu == 3 and not item3_cpu:
                        print("O inimigo usou a Pedra de Amolar! O ataque dele dará o dobro de dano nos próximos 2 turnos")
                        item3_cpu = True
                        amolar_ativo_cpu = 2

                    elif item_cpu == 4 and not item4_cpu:
                        dano_explosivo = random.randint(30, 50)
                        vida_jogador = vida_jogador - dano_explosivo
                        print(f"O inimigo usou Bola de Fogo e causou {dano_explosivo} de dano!")
                        item4_cpu = True

                elif escolha_cpu == "atacar":
                    critico = random.randint(1, 10)

                    atq = atq_cpu
                    defesa = def_jogador

                    if tela_turnos_j1 > 0:
                        defesa = 0
                        tela_turnos_j1 = tela_turnos_j1 - 1

                    if escudo_ativo > 0:
                        defesa = defesa * 2
                        escudo_ativo = escudo_ativo -1

                    if forca_ativa_cpu > 0:
                        atq = atq * 2
                        forca_ativa_cpu = forca_ativa_cpu - 1

                    if critico == 10:
                        vida_perdida = max(0, atq - defesa)
                        vida_perdida = vida_perdida * 2
                        if amolar_ativo_cpu > 0:
                            vida_perdida = vida_perdida * 2
                            amolar_ativo_cpu = amolar_ativo_cpu - 1
                        vida_jogador = vida_jogador - vida_perdida
                        print(f"ATAQUE CRÍTICO! Você perde {vida_perdida} de HP")
                    else:
                        vida_perdida = max(0, atq - defesa)
                        if amolar_ativo_cpu > 0:
                            vida_perdida = vida_perdida * 2
                            amolar_ativo_cpu = amolar_ativo_cpu - 1
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

    elif opcao == 3:
        print("\nSaindo...")

    else:
        print("\nINVALIDO")