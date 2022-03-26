NOME_ARQUIVO = "contas.txt"
contas = []


def ler_contas(contas):
    with open(NOME_ARQUIVO, "r") as arq:
        linha = arq.readline()
        while (linha != ""):
            linha = linha.strip("\n")
            linha = linha.split(";")
            #print(linha)
            linha[0], linha[3] = int(linha[0]), float(linha[3])
            #print(linha)
            contas.append(linha)
            linha = arq.readline()
    return contas


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: Por Favor, Digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário Preferiu não Digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return "-" * tam


def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    titulo("Menu do Sistema") 
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt("Sua Opção: ")
    return opc    


def valida_int():
    dado_ok = False
    while not dado_ok:
        try:
            num_conta = int(input('Entre com o número da conta: '))
            dado_ok = True
        except(ValueError):
            print("ERROR, digite um número válido!")
    return num_conta


def valida_escolha():
    dado_ok = False
    while not dado_ok:
        try:
            escolha = int(input("Escolha uma opção: "))
            dado_ok = True
        except(ValueError):
            print("ERROR, digite um número válido!")
    return escolha


def valida_float():
    dado_ok = False
    while not dado_ok:
        try:
            saldo = float(input('Entre com seu Saldo: '))
            dado_ok = True
        except(ValueError):
            print("ERROR, digite um número inválido!")
    return saldo


def valida_nome():
    dado_ok = False
    while not dado_ok:
        try:
            nome = str(input)
            dado_ok = True
        except(ValueError):
            print("Número inválido!")
    return nome


def pesquisar(contas, num_conta):
    existe = False
    for conta in contas:
        if(conta[0] == num_conta):
            existe = True
            break
    return existe


def cadastrar(contas):
    num_conta = valida_int()
    if pesquisar(contas, num_conta) == False:
        pnome = str(input("Entre com seu nome: "))
        while len(pnome) < 4:
            print("O Primeiro nome deve ter pelo menos 4 caracteres")
            pnome = str(input("Entre com seu nome: "))
            break
        snome = str(input("Entre com seu Sobrenome: "))
        while len(snome) < 4:
            print("O seu Sobrenome deve ter pelo menos 4 caracteres")
            snome = str(input("Entre com seu Sobrenome: "))
            break
        saldo = valida_float()
        conta_nova = [num_conta, pnome, snome, saldo]
        contas.append(conta_nova)
        print(contas)
    elif pesquisar(contas, num_conta) == True:
        print("Conta já existente")


def alterar_saldo(contas):
    num_conta_alterar = valida_int()  
    for conta in contas:  
        if pesquisar(contas, num_conta_alterar) == True:
            if(conta[0] == num_conta_alterar):
                print("[1] para depositar\n[2] para sacar")
                escolha = valida_escolha()
                if(escolha == 1):
                    depositar = float(input("Digite o valor que você quer depositar da sua conta: "))
                    if(depositar > 0):
                        novo_saldo = conta[3] + depositar
                        print(conta)
                        print(novo_saldo)
                        conta[3] = novo_saldo
                        print(contas)
                    else:
                        print("Digite um número maior que zero!")
                elif(escolha == 2):
                    sacar = float(input("Digite o valor que você quer sacar da sua conta: "))
                    if(sacar > 0):
                        novo_saldo = conta[3] - sacar
                        print(conta)
                        print(novo_saldo)
                        conta[3] = novo_saldo
                        print(contas)
                    else:
                        print("Digite um número maior que zero!")
        elif pesquisar(contas, num_conta_alterar) == False:
            print("ERROR, O numero da sua conta não foi encontrado!")   


def consultar(contas):
    num_conta = valida_int()
    for conta in contas:
        if(conta[0] == num_conta):
            print("Número da conta = {} | Titular da conta = {} {} | Saldo da conta = {}".format(conta[0], conta[1], conta[2], conta[3]))


def excluir_conta(contas):
    num_conta_excluir = valida_int()  
    for conta in contas:
        if(conta[0] == num_conta_excluir):
            if(conta[3] == 0):
                contas.remove(conta)
                print(contas)
            else:
                print("O saldo da conta deve estar zerado para concluir a exclusão!")
                break
        else:
            print("sua conta não foi encontrada!")
            
            



def gravar_contas(contas):
    with open(NOME_ARQUIVO, "w") as arq:
        for conta in contas:
            arq.write((str(conta[0]) + ";" + (conta[1]) + ";" + (conta[2]) + ";" + str(conta[3])) + "\n")
    print() 


def relatorio():
    print("[1] para mostrar contas negativas\n[2] para mostrar contas a partir de determinado valor\n[3] Para mostrar sua conta ")
    escolha = valida_escolha()
    if(escolha == 1):
        for conta in contas:
            if(conta[3] < 0):
                print(conta)
    elif(escolha == 2):
        filtar = int(input("Escolha o valor que você deseja filtar: "))
        for conta in contas:
            if(conta[3] >= filtar):
                print(conta)        
    elif(escolha == 3):
        consultar(contas)
    else:
        print("Ocorreu um ERRO, digite um número valido!")
        

ler_contas(contas)
print(contas)
while True:      
    resposta = menu(["Cadastro", "Alterar saldo","excluir conta", "Relatorios","Sair do sistema"])
    if(resposta == 1):
        titulo("Cadastrar")
        cadastrar(contas) 
    elif(resposta == 2):
        titulo("Alterar Saldo")
        alterar_saldo(contas)
    elif(resposta == 3):
        titulo("Exclusão de conta")
        excluir_conta(contas)
    elif(resposta == 4):
        titulo("relatórios")
        relatorio()
    elif(resposta == 5):
        titulo("Você saiu do sistema")
        break
    else:
        print("Ocorreu um ERRO, digite uma opção válida")
gravar_contas(contas)