import time
import random
import json


falaRadioLista = ["Radio: Atenção sobreviventes, foi identificado que os infectados estão passando por mutações nos últimos dias, alguns deles *falha*...", "Radio: Atenção sobreviventes, as áreas de risco são: Delegacia, Corpo de Bombeiros e Igreja.", "*Radio falhando"]
falasEncontrosZumbi = ["Ele te agarrou com força, te arranhando um pouco.", "Ele te deu uma pancada em uma tentativa de agarrão!", "Ele te deu uma mordida, por sorte, a mordida não espalha a infecção." ]
inventario = []
ficha = []
armasFracas = ["Cano de Metal Desgastado", "Faca de Cozinha", "Garrafa de vidro Quebrado"]
armasMedias = ["Cano de Metal", "Facão", "Machadinha", "Chave Inglesa", "Martelo Pequeno", "Pá", "Cassetete"]
armasFortes = ["Machado de Lenhador", "Pistola Municiada", "Machete de Guerra", "Machado de Bombeiro"]
itensBombeiros = [armasFortes[3], "Capacete de Bombeiro", "Lancheira", armasMedias[4]]
itensDelegacia = [armasMedias[5], armasFortes[2], "Munição de Pistola", "Colete Policial"]
itensHospital = ["Seringa", "Bisturi", "Xarope", "Bandagens", "Jaleco rasgado"]
itensBairro = ["Garrafa", "Garrafa de Vidro", "Pilhas", "Caixa de Comida", armasMedias[4]]
itensPosto = ["Galão Vazio", "Álcool", "Cigarros", "Isqueiro", "Gasolina", armasMedias[3]]
comidas = ["Comida Enlatada", "Frutas", "Congelados", "Barra de Chocolate"]
bebidas = ["Água", "Cerveja", "Refrigerante", "Vinho"]

def animacao():
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")

def introducao():
    print("Primeiro, irei te ensinar o básico do sistema do jogo")
    time.sleep(0.5)
    print("Seus atributos variam de 0 a 10, e toda ação que você fizer, um D10 será rolado")
    time.sleep(0.5)
    print("Caso o valor do dado seja menor ou igual ao valor do seu atributo, você passou no teste")
    print("Exemplo: Dado = 4, Combate = 6. Sucesso!")
    print("Exemplo: Dado = 6, Combate = 6. Sucesso!")
    print("Exemplo: Dado = 8, Combate = 6. Fracasso!")
    time.sleep(1)
    print("Agora, é hora de te apresentar as perícias!")
    print("Você tem 5 perícias principais")
    time.sleep(1)
    print("----EXPLORAÇÃO----")
    print("Determina suas habilidades de encontrar itens enquanto explora.")
    time.sleep(3)
    print("----COMBATE----")
    print("Determina suas capacidades dentro do campo de batalha!")
    time.sleep(3)
    print("----MEDICINA----")
    print("Determina sua habilidade de curar ferimentos com o que tiver disponível.")
    time.sleep(3)
    print("----ARTESANATO----")
    print("Determina suas habilidades em criar itens úteis e bases.")
    time.sleep(3)
    print("----FISICO----")
    print("Determina o quão resistente você é a ferimentos, doenças, etc.")
    time.sleep(3)
    print("Agora, te falarei sobre as mecânicas básicas do jogo")
    print("Durante o dia, você poderá realizar 4 ações variadas, algumas delas gastam uma ação, outras não")
    print("Exemplo: Comer/Beber não gastam ações, mas Explorar gasta.")
    time.sleep(3)
    print("Ao final das suas ações, a noite irá cair. Ao amanhecer, você irá perder fome e sede")
    print("Explore os lugares para tentar encontrar comida, bebidas, armas ou outros itens úteis")
    time.sleep(3)
    print("A cada 10 dias, os zumbis se fortificam, esteja ciente disso")
    print("Sobreviva 50 dias para vencer, boa sorte!")

def criarFichas():
    nome = str(input("Digite o nome do Sobrevivente: "))
    while True:
        pontosRestantes = 30
        atributoMax = 8
        print(f"Você tem {pontosRestantes} pontos restantes")
        print(f"O máximo que cada atributo pode possuir é {atributoMax}")

        exploracao = int(input("Digite seu valor de Exploracao: "))
        pontosRestantes -= exploracao
        print(f"Você tem {pontosRestantes} pontos restantes")

        combate = int(input("Digite seu valor de Combate: "))
        pontosRestantes -= combate
        print(f"Você tem {pontosRestantes} pontos restantes")

        medicina = int(input("Digite seu valor de Medicina: "))
        pontosRestantes -= medicina
        print(f"Você tem {pontosRestantes} pontos restantes")

        artesanato = int(input("Digite seu valor de Artesanato: "))
        pontosRestantes -= artesanato
        print(f"Você tem {pontosRestantes} pontos restantes")

        fisico = int(input("Digite seu valor de Físico: "))
        pontosRestantes -= fisico
        print(f"Você tem {pontosRestantes} pontos restantes")

        if exploracao > atributoMax or combate > atributoMax or medicina > atributoMax or artesanato > atributoMax or fisico > atributoMax:
            print("Um de seus atributos ultrapassou os limites máximos de 8 pontos")
            continue



        if pontosRestantes < 0:
            print("Sua ficha ultrapassou os limites de pontos, por favor, recrie sua ficha")
        elif pontosRestantes > 0:
            print("Você não usou todos seus pontos, isso pode te prejudicar...")
        else:
            print("Ficha Criada com Sucesso! ")
            vida = 12 + fisico
            ficha.append({
                "Nome": nome,
                "Exploração": exploracao,
                "Combate": combate,
                "Medicina": medicina,
                "Artesanato": artesanato,
                "Físico": fisico,
                "Vida": vida
                })
            return
                
def mostrarFicha():
    print("Sua ficha está assim!")
    print("-----FICHA-----")
    for item in ficha:
            print(f"Nome: {item['Nome']}")
            print(f"Vida: {item['Vida']}")
            print(f"Exploração: {item['Exploração']}")
            print(f"Combate: {item['Combate']}")
            print(f"Medicina: {item['Medicina']}")
            print(f"Artesanato: {item['Artesanato']}")
            print(f"Físico: {item['Físico']}")

def jogo(dia=0,
    fome=10,
    sede=10,
    tempo=4,
    lugar=None,
    base=0,
    vidaBase=0,
    vidaBaseMax=10,
    itemEquipado=None,
    dificuldade=0,
    diasDificuldade=10):
    if lugar is None:
        lugar = random.randint(1,5)
    while True:
        if dia >= 50:
            print("Você Ganhou, parabéns.")
            break
        if dificuldade >= 5:
            dificuldade = 5
        if dia > diasDificuldade:
            dificuldade += 1
            diasDificuldade += 10
            print("Os zumbis mudaram, a dificuldade aumentou")
            print(f"Dificuldade: {dificuldade}")
        if base != 0 and vidaBase <= 0:
            print("Sua base foi danificada, reconstrua ela para ter uma base")
            base = 0
        if base != 0:
            print(f"Sua base está com {vidaBase}/{vidaBaseMax} de vida")
        vidaMax = 12 + ficha[0]["Físico"]
        if ficha[0]['Vida'] <= 0:
            print("Você Morreu, fim de Jogo!")
            break
        if lugar == 1:
            print("Você está no Hospital!")
        elif lugar == 2:
            print("Você está nas casas do bairro")
        elif lugar == 3:
            print("Você está no posto")
        elif lugar == 4:
            print("Você está nos bombeiro, tome cuidado")
            print(f"Nível de Risco: {nivelDeRisco}")
        elif lugar == 5:
            print("Você está na Delegacia, tome cuidado")
            print(f"Nível de Risco: {nivelDeRisco}")
        modificador = 0
        if itemEquipado in armasFracas:
            modificador = 1

        elif itemEquipado in armasMedias:
            modificador = 2

        elif itemEquipado in armasFortes:
            modificador = 4
        else:
            modificador = 0
        print("#=================")
        print(f"#======Dia:{dia}======")
        print("#=================")
        if ficha[0]["Vida"] >= vidaMax:
            ficha[0]["Vida"] = vidaMax
        if fome < 0:
            ficha[0]["Vida"] -= 2
        if sede < 0:
            ficha[0]["Vida"] -= 2
        print(f"Você ainda tem {tempo} ações antes do anoitecer")
        time.sleep(1)
        print(f"Você ainda tem {fome} de fome")
        print(f"Você ainda tem {sede} de sede")
        print(f"Você está com {ficha[0]['Vida']}/{vidaMax} de vida")
        time.sleep(2)
        print("1 = Explorar o Lugar")
        print("2 = Sair do Lugar")
        print("3 = Descansar")
        print("4 = Ver inventário")
        print("5 = Tratar-se")
        print("6 = Verificar Ficha")
        print("7 = Comer/Beber")
        print("8 = Equipar Item")
        print("9 = Treinar atributo")
        print("10 = Aprimorar/Consertar Arma")
        print("11 = Usar Item")
        print("12 = Criar Base")
        print("13 = Reparar Base")
        print("14 = Salvar Jogo")
        escolha = int(input("Digite sua escolha: "))
        if escolha == 1:
            dado = random.randint(1, 10)
            if lugar == 1:
                print(f"Teste: {dado}")
                if dado <= ficha[0]["Exploração"]:
                    itemEncontrado = random.choice(itensHospital + comidas + bebidas + armasFracas)

                    inventario.append({
                    "Item": itemEncontrado
                    
                    })


                    print("Dentro do hospital você achou...")
                    print(itemEncontrado)
                
                else:
                    print("Você explorou, mas não encontrou nada")
                eventoRNG = random.randint(1, 4)
                print("Durante sua expedição")
                time.sleep(3)
                if eventoRNG == 1:
                    print("Nada aconteceu")
                elif eventoRNG == 2:
                    print("Um infectado te atacou!")
                    dado= random.randint(1,10)
                    if (dado + dificuldade) - modificador <= ficha[0]["Combate"]:
                        print("Mas você saiu ileso!")
                    else:
                        falaZumbi = random.choice(falasEncontrosZumbi)
                        print(falaZumbi)
                        dano = random.randint(1, 6 ) + random.randint(1, 4)
                        ficha[0]["Vida"] -= dano
                        time.sleep(3)
                        print(f"Você recebeu {dano} de dano.")
                        time.sleep(1)
                        print(f"Você está com {ficha[0]['Vida']} de vida")
                elif eventoRNG == 3:
                    print("Você encontrou um item!")
                    itemEncontrado = random.choice(itensHospital + comidas + bebidas + armasFracas)

                    inventario.append({
                    "Item": itemEncontrado
                    
                    })
                    print(itemEncontrado)
                    

                elif eventoRNG == 4:
                    falaRadio = random.choice(falaRadioLista)
                    print(falaRadio)
                tempo -= 1


            elif lugar == 2:
                print(f"Teste: {dado}")
                if dado <= ficha[0]["Exploração"]:
                    itemEncontrado = random.choice(itensBairro + comidas + bebidas + armasFracas)

                    inventario.append({
                    "Item": itemEncontrado
                    })

                    print("Dentro das casas do bairro você achou...")
                    print(itemEncontrado)
                    
                else:
                    print("Você explorou, mas não encontrou nada")
                eventoRNG = random.randint(1, 4)
                print("Durante sua expedição")
                time.sleep(3)
                if eventoRNG == 1:
                    print("Nada aconteceu")
                elif eventoRNG == 2:
                    print("Um infectado te atacou!")
                    dado = random.randint(1,10)
                    if (dado + dificuldade) - modificador <= ficha[0]["Combate"]:
                        print("Mas você saiu ileso!")
                    else:
                        falaZumbi = random.choice(falasEncontrosZumbi)
                        print(falaZumbi)
                        dano = random.randint(1, 6 ) + random.randint(1, 4)
                        ficha[0]["Vida"] -= dano
                        time.sleep(3)
                        print(f"Você recebeu {dano} de dano.")
                        time.sleep(1)
                        print(f"Você está com {ficha[0]['Vida']} de vida")
                elif eventoRNG == 3:
                    print("Você encontrou um item!")
                    itemEncontrado = random.choice(itensBairro + comidas + bebidas + armasFracas)

                    inventario.append({
                    "Item": itemEncontrado
                    
                    })
                    print(itemEncontrado)

                elif eventoRNG == 4:
                    falaRadio = random.choice(falaRadioLista)
                    print(falaRadio)
                tempo -= 1


            elif lugar == 3:
                print(f"Teste: {dado}")
                if dado <= ficha[0]["Exploração"]:
                    itemEncontrado = random.choice(itensPosto + comidas + bebidas + armasFracas)

                    inventario.append({
                    "Item": itemEncontrado
                    })

                    print("Dentro do posto você achou...")
                    print(itemEncontrado)
                else:
                    print("Você explorou, mas não encontrou nada")

                eventoRNG = random.randint(1, 4)
                print("Durante sua expedição")
                time.sleep(3)
                if eventoRNG == 1:
                    print("Nada aconteceu")
                elif eventoRNG == 2:
                    print("Um infectado te atacou!")
                    dado = random.randint(1,10)
                    if (dado + dificuldade) - modificador <= ficha[0]["Combate"]:
                        print("Mas você saiu ileso!")
                    else:
                        falaZumbi = random.choice(falasEncontrosZumbi)
                        print(falaZumbi)
                        dano = random.randint(1, 6) + random.randint(1, 4)
                        ficha[0]["Vida"] -= dano
                        time.sleep(3)
                        print(f"Você recebeu {dano} de dano.")
                        time.sleep(1)
                        print(f"Você está com {ficha[0]['Vida']} de vida")
                elif eventoRNG == 3:
                    print("Você encontrou um item!")
                    itemEncontrado = random.choice(itensPosto + comidas + bebidas + armasFracas)

                    inventario.append({
                    "Item": itemEncontrado
                    
                    })
                    print(itemEncontrado)

                elif eventoRNG == 4:
                    falaRadio = random.choice(falaRadioLista)
                    print(falaRadio)
                tempo -= 1


            elif lugar == 4:
                print(f"Teste: {dado}")
                if dado <= ficha[0]["Exploração"]:
                    itemEncontrado = random.choice(itensBombeiros + comidas + bebidas + armasFracas)

                    inventario.append({
                    "Item": itemEncontrado
                    })

                    print("Dentro dos bombeiros você achou...")
                    print(itemEncontrado)
                else:
                    print("Você explorou, mas não encontrou nada")

                eventoRNG = random.randint(1, 4)
                print("Durante sua expedição")
                time.sleep(3)
                if eventoRNG == 1:
                    dado = random.randint(1, 10)
                    if dado <= ficha[0]["Físico"]:
                        print("Você teve que sair correndo do lugar e se abrigar em um local mais seguro")
                        lugar = random.randint(1, 3)
                    else:
                        print("Os zumbis te atacaram, mas você não conseguiu sair dela a tempo")
                        dano = random.randint(1, 6 ) * 2 + (nivelDeRisco * 2)
                        ficha[0]["Vida"] -= dano
                        print(f"Você está com {ficha[0]['Vida']} de vida")
                elif eventoRNG == 2:
                    print("Um infectado te atacou!")
                    dado = random.randint(1,10)
                    if (dado + nivelDeRisco + dificuldade) - modificador <= ficha[0]["Combate"]:
                        print("Mas você saiu ileso!")
                    else:
                        falaZumbi = random.choice(falasEncontrosZumbi)
                        print(falaZumbi)
                        dano = random.randint(1, 6 ) * 2 + nivelDeRisco
                        ficha[0]["Vida"] -= dano
                        time.sleep(3)
                        print(f"Você recebeu {dano} de dano.")
                        time.sleep(1)
                        print(f"Você está com {ficha[0]['Vida']} de vida")
                elif eventoRNG == 3:
                    print("Você encontrou um item!")
                    itemEncontrado = random.choice(itensBombeiros + comidas + bebidas + armasFracas)

                    inventario.append({
                    "Item": itemEncontrado
                    
                    })
                    print(itemEncontrado)

                elif eventoRNG == 4:
                    falaRadio = random.choice(falaRadioLista)
                    print(falaRadio)
                tempo -= 1


            elif lugar == 5:
                    print(f"Teste: {dado}")
                    if dado <= ficha[0]["Exploração"]:
                        itemEncontrado = random.choice(itensDelegacia + comidas + bebidas + armasFracas)

                        inventario.append({
                        "Item": itemEncontrado
                        })

                        print("Dentro da delegacia você achou...")
                        print(itemEncontrado)
                    else:
                        print("Você explorou, mas não encontrou nada")

                    eventoRNG = random.randint(1, 4)
                    print("Durante sua expedição")
                    time.sleep(3)
                    if eventoRNG == 1:
                        print("Você teve que sair correndo do lugar e se abrigar em um local mais seguro")
                        lugar = random.randint(1, 3)
                    elif eventoRNG == 2:
                        print("Um infectado te atacou!")
                        dado = random.randint(1,10)
                        if (dado + nivelDeRisco + dificuldade) - modificador <= ficha[0]["Combate"]:
                            print("Mas você saiu ileso!")
                        else:
                            falaZumbi = random.choice(falasEncontrosZumbi)
                            print(falaZumbi)
                            dano = random.randint(1, 6 ) * 2 + nivelDeRisco
                            ficha[0]["Vida"] -= dano
                            time.sleep(3)
                            print(f"Você recebeu {dano} de dano.")
                            time.sleep(1)
                            print(f"Você está com {ficha[0]['Vida']} de vida")
                    elif eventoRNG == 3:
                        print("Você encontrou um item!")
                        itemEncontrado = random.choice(itensDelegacia + comidas + bebidas + armasFracas)

                        inventario.append({
                        "Item": itemEncontrado
                        
                        })
                        print(itemEncontrado)

                    elif eventoRNG == 4:
                        falaRadio = random.choice(falaRadioLista)
                        print(falaRadio)
                    tempo -= 1


        elif escolha == 2:
            lugarPassado = lugar
            lugar = random.randint(1, 5)
            if lugar != lugarPassado:
                if lugar == 1:
                    tempo -= 1
                elif lugar == 2:
                    tempo -= 1
                elif lugar == 3:
                    tempo -= 1
            else:
                print("Você tentou sair, mas os infectados o impediram")


        elif escolha == 3:
            print("Você descansou...")
            animacao()
            descansoRNG = random.randint(1, 3)
            if descansoRNG == 1:
                vidaCurada = random.randint(1,4)
                if base == lugar:
                    vidaCurada += 2
                ficha[0]["Vida"] += vidaCurada
                print(f"Bem! Recuperou {vidaCurada} de vida")
            elif descansoRNG == 2:
                vidaCurada = random.randint(1, 2)
                if base == lugar:
                    vidaCurada += 2
                ficha[0]["Vida"] += vidaCurada
                print(f"Bem, mas com um pouco de incômodo. Recuperou {vidaCurada} de vida")
            elif descansoRNG == 3:
                if base == lugar:
                    vidaCurada = 2
                    ficha[0]["Vida"] += vidaCurada
                    print(f"Mal, mas suficiente para se recuperar. Recuperou {vidaCurada} de vida")
                else:
                    print("Mal! Não recupera nada")
            tempo -= 1


        elif escolha == 4:
            print("----Inventário----")
            for item in inventario:
                print(f'--{item["Item"]}')


        elif escolha == 5:
            temMedicina = False
            for item in inventario:

                if item["Item"] in itensHospital:
                    temMedicina = True
                    print("Você possui um item hospitalar, deseja se tratar?")
                    print("1 = Sim")
                    print("2 = Não")
                    selfcare = int(input("Se tratar? "))
                    if selfcare == 1:
                        tempo -= 1
                        inventario.remove(item)
                        dado = random.randint(1,10)
                        print(dado)
                        animacao()
                        if dado <= ficha[0]["Medicina"]:
                            vidaCurada = random.randint(1,6)
                            ficha[0]["Vida"] += vidaCurada
                            print(f"Você se tratou. Recuperou {vidaCurada} de vida")
                            
                        else:
                            print("Você não conseguiu se tratar")
                        break
                    else:
                        print("Você decidiu não se tratar")
                    
            if temMedicina == False:
                print("Você não possui itens para se tratar.")

        elif escolha == 6:
            mostrarFicha()
            print(f"Modificador Combate: {modificador}")

        elif escolha == 7:
            temComida = False
            for item in inventario:
                if item["Item"] in comidas:
                    temComida = True
                    print("Você possui comida, deseja consumi-la?")
                    print("1 = Sim")
                    print("2 = Não")
                    comer = int(input("Se alimentar? "))
                    if comer == 1:
                        inventario.remove(item)
                        animacao()
                        fomeCurada = random.randint(1,6)
                        fome += fomeCurada
                        if fome > fomeMax:
                            fome = fomeMax
                        print(f"Você comeu. Recuperou {fomeCurada} de fome")
                        break
                    else:
                        print("Você decidiu não comer")
                        break
                    
            if temComida == False:
                print("Você não possui comida para se alimentar.")

            temBebida = False
            for item in inventario:
                if item["Item"] in bebidas:
                    temBebida = True
                    print("Você possui bebida, deseja consumi-la?")
                    print("1 = Sim")
                    print("2 = Não")
                    beber = int(input("Beber? "))
                    if beber == 1:
                        inventario.remove(item)
                        animacao()
                        sedeCurada = random.randint(1,6)
                        sede += sedeCurada
                        if sede > sedeMax:
                            sede = sedeMax
                        print(f"Você bebeu. Recuperou {sedeCurada} de sede")
                        break
                    else:
                        print("Você decidiu não beber")
                        break
                    
            if temBebida == False:
                print("Você não possui bebidas para se tomar.")

        elif escolha == 8:

            armasInventario = []

            numeroArma = 1

            for item in inventario:

                if item["Item"] in armasFracas or item["Item"] in armasMedias or item["Item"] in armasFortes:

                    armasInventario.append(item["Item"])

                    print(f"{numeroArma} = {item['Item']}")

                    numeroArma += 1


            if len(armasInventario) > 0:

                escolhaArma = int(input("Escolha uma arma para equipar: "))

                itemEquipado = armasInventario[escolhaArma - 1]

                print(f"Você equipou {itemEquipado}")

            else:

                print("Você não possui armas.")

        elif escolha == 9:
            print("1 = Exploração")
            print("2 = Combate")
            print("3 = Medicina")
            print("4 = Artesanato")
            print("5 = Físico")
            treino = int(input("Digite sua escolha: "))
            if treino == 1 and ficha[0]["Exploração"] < 10:
                dado = random.randint(1,10)
                if dado <= 3:
                    print("Treino bem sucedido")
                    ficha[0]["Exploração"] += 1
                else:
                    print("Você tenta treinar, mas não vê resultado")


            elif treino == 2 and ficha[0]["Combate"] < 10:
                dado = random.randint(1,10)
                if dado <= 3:
                    print("Treino bem sucedido")
                    ficha[0]["Combate"] += 1
                else:
                    print("Você tenta treinar, mas não vê resultado")


            elif treino == 3 and ficha[0]["Medicina"] < 10:
                dado = random.randint(1,10)
                if dado <= 3:
                    print("Treino bem sucedido")
                    ficha[0]["Medicina"] += 1
                else:
                    print("Você tenta treinar, mas não vê resultado")
            

            elif treino == 4 and ficha[0]["Artesanato"] < 10:
                dado = random.randint(1,10)
                if dado <= 3:
                    print("Treino bem sucedido")
                    ficha[0]["Artesanato"] += 1
                else:
                    print("Você tenta treinar, mas não vê resultado")

            
            elif treino == 5 and ficha[0]["Físico"] < 10:
                dado = random.randint(1,10)
                if dado <= 3:
                    print("Treino bem sucedido")
                    ficha[0]["Físico"] += 1
                else:
                    print("Você tenta treinar, mas não vê resultado")
            tempo -= 1
            fome -= 1
            sede -= 1

        elif escolha == 10:
            lixoInventario = []

            numeroItem = 1

            for item in inventario:

                if item["Item"] in itensPosto or item["Item"] in itensBairro or item["Item"] in itensHospital :

                    lixoInventario.append(item["Item"])

                    print(f"{numeroItem} = {item['Item']}")

                    numeroItem += 1


            if len(lixoInventario) > 0:

                escolhaLixo = int(input("Escolha uma arma para equipar: "))

                lixoEscolhido = lixoInventario[escolhaLixo - 1]

                print(f"Você escolheu {lixoEscolhido}")

                dado = random.randint(1,10)
                if dado <= ficha[0]["Artesanato"]:
                    print(f"Você aprimorou {lixoEscolhido}")

                    if lixoEscolhido == itensBairro[1]:
                        print(f"Virou {armasFracas[2]}")

                        for item in inventario:
                            if item["Item"] == lixoEscolhido:
                                inventario.remove(item)
                                break

                        inventario.append({
                            "Item": armasFracas[2]
                        })
                else:
                    print("Você tentou melhorar seu item, mas acabou danificando ele")
                    for item in inventario:
                            if item["Item"] == lixoEscolhido:
                                inventario.remove(item)
                                break


            else:

                print("Você não possui armas.")

        elif escolha == 11:
            ItensInventario = []

            numeroItem = 1

            for item in inventario:

                if item["Item"] in itensPosto or item["Item"] in itensBairro or item["Item"] in itensHospital :

                    ItensInventario.append(item["Item"])

                    print(f"{numeroItem} = {item['Item']}")

                    numeroItem += 1


            if len(ItensInventario) > 0:

                escolhaItem = int(input("Escolha um item para usar: "))

                ItemEscolhido = ItensInventario[escolhaItem - 1]

                print(f"Você escolheu {ItemEscolhido}")

                if ItemEscolhido == itensBairro[0]:
                    print(f"Virou {bebidas[0]}")
                    for item in inventario:

                        if item["Item"] == ItemEscolhido:

                            inventario.remove(item)

                            break
                    inventario.append({
                    "Item": bebidas[0]
                    
                    })
                
                
                if ItemEscolhido == itensBairro[3]:
                    quantidade = random.randint(1, 6)
                    comidaEncontrada = random.choice(comidas)
                    print(f"Dentro da caixa tinha {quantidade} {comidaEncontrada}")
                    for item in inventario:

                        if item["Item"] == ItemEscolhido:

                            inventario.remove(item)

                            break
                    for i in range(quantidade):
                        inventario.append({
                        "Item": comidaEncontrada
                    
                        })
                
                if ItemEscolhido == itensBombeiros[2]:
                    quantidade = random.randint(1, 3)
                    print(f"Dentro dela tinha {quantidade} {comidas[3]}")
                    for item in inventario:

                        if item["Item"] == ItemEscolhido:

                            inventario.remove(item)

                            break
                    for i in range(quantidade):
                        inventario.append({
                        "Item": comidas[3]
                    
                        })


                else:

                    print("Você não itens que possam ser utilizados.")
            
        elif escolha == 12:
            if base != lugar:
                tempo -= 1
                print("Você parou para construir uma base")
                dado = random.randint(1, 10)
                if dado <= ficha[0]["Artesanato"]:
                    base = lugar
                    print("Base Definida")
                    vidaBase = 10
                elif dado == 10:
                    print("Você tenta criar a sua base, mas acaba se machucando no processo!")
                    ficha[0]["Vida"] -= 1
                else:
                    print("Você tentou contruir a sua base, mas não conseguiu")
            else:
                print("Você já possui uma base aqui")

        elif escolha == 13:
            if base != 0:
                print("Você tenta reparar sua base")
                animacao()
                dado = random.randint(1, 10)
                if dado <= ficha[0]["Artesanato"]:
                    curaBase = random.randint(1, 3)
                    vidaBase += curaBase
                    print(f"E conseguiu, recuperou {curaBase} da base")
                    print(f"Vida da Base: {vidaBase}")

                    if VidaBase > vidaBaseMax:
                        VidaBase = vidaBaseMax
                else:
                    print("Você tenta consertar a base, mas não conseguiu")
                tempo -= 1
            else:
                print("Você não tem uma base")
            
        elif escolha == 14:
            dados = {
            "ficha": ficha,
            "inventario": inventario,
            "dia": dia,
            "fome": fome,
            "sede": sede,
            "armaEquipada": itemEquipado,
            "lugar": lugar,
            "dificuldade": dificuldade,
            "diasDificuldade": diasDificuldade,
            "tempo": tempo,
            "base": base,
            "vidaBase": vidaBase
            }
            with open("save.json", "w") as arquivo:
                json.dump(dados, arquivo)
            print("Jogo Salvo com Sucesso")
        if tempo <= 0:
            print("A noite chegou...")
            animacao()
            animacao()
            anoitecer = random.randint(1, 3)
            if anoitecer == 1:
                print("A noite hoje foi tranquila")
            if anoitecer == 2:
                if base != 0:
                    print("Um infectado atacou sua base essa noite")
                    vidaBase -= random.randint(1, 3) + dificuldade
                else:
                    print("Um infectado te atacou pela noite!")
                    dado = random.randint(1, 10) + 2
                    if dado <= ficha[0]["Combate"]:
                            print("Mas você saiu ileso!")
                    else:
                        falaZumbi = random.choice(falasEncontrosZumbi)
                        print(falaZumbi)
                        dano = random.randint(1, 6 ) + random.randint(1, 4)
                        ficha[0]["Vida"] -= dano
                        time.sleep(3)
                        print(f"Você recebeu {dano} de dano.")
                        time.sleep(1)
                        print(f"Você está com {ficha[0]['Vida']} de vida")
            if anoitecer == 3:
                print("Você escuta os gritos de um sobrevivente")
            tempo = 4
            fome -= random.randint(1, 3)
            sede -= random.randint(1, 3)
            dia += 1
            if base != 0:
                vidaBase -= 1
                

print("1 = Novo Jogo")
print("2 = Novo Jogo s/ introdução")
print("3 = Carregar Jogo")
iniciar = int(input("Digite sua escolha: "))
if iniciar == 1:
    introducao()
    time.sleep(5)
    criarFichas()
    time.sleep(3)
    mostrarFicha()
    time.sleep(3)
    jogo()
elif iniciar == 2:
    criarFichas()
    time.sleep(3)
    mostrarFicha()
    time.sleep(3)
    jogo()
elif iniciar == 3:
    with open("save.json", "r") as arquivo:
        dados = json.load(arquivo)

    ficha = dados["ficha"]
    inventario = dados["inventario"]

    jogo(
        dia=dados["dia"],
        fome=dados["fome"],
        sede=dados["sede"],
        tempo=dados["tempo"],
        lugar=dados["lugar"],
        base=dados["base"],
        vidaBase=dados["vidaBase"],
        itemEquipado=dados["armaEquipada"],
        dificuldade=dados["dificuldade"],
        diasDificuldade=dados["diasDificuldade"]
    )