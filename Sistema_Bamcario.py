def mostrar_menu():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    return input(menu)

def mostrar_extrato(saldo, extrato, nome, cpf):
    print("\n================ EXTRATO ================")
    print(f"Titular: {nome} | CPF: {cpf}")
    print("------------------------------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def realizar_deposito(saldo, extrato, nome):
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
        return saldo, extrato

    if valor > 0:
        saldo += valor
        extrato += f"{nome} - Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Insira um valor positivo para depositar.")

    return saldo, extrato

def realizar_saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES, nome):
    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
        return saldo, extrato, numero_saques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"{nome} - Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        print(f"Saques restantes hoje: {LIMITE_SAQUES - numero_saques}")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def criar_conta(usuarios):
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF (somente números): ")
    
    if cpf in usuarios:
        print("CPF já cadastrado!")
        return
    
    usuarios[cpf] = {
        "nome": nome,
        "saldo": 0.0,
        "extrato": "",
        "saques": 0
    }
    print("Conta criada com sucesso!")

def acessar_conta(usuarios):
    cpf = input("Digite seu CPF para acessar a conta: ")
    if cpf not in usuarios:
        print("CPF não encontrado. Cadastre-se primeiro.")
        return
    
    conta = usuarios[cpf]
    nome = conta["nome"]
    saldo = conta["saldo"]
    extrato = conta["extrato"]
    numero_saques = conta["saques"]
    LIMITE = 500
    LIMITE_SAQUES = 3

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato, nome)

        elif opcao == "s":
            saldo, extrato, numero_saques = realizar_saque(
                saldo, extrato, LIMITE, numero_saques, LIMITE_SAQUES, nome
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato, nome, cpf)

        elif opcao == "q":
            print("Saindo da conta...\n")
            break

        else:
            print("Operação inválida! Por favor, selecione novamente.")
    
    # Atualiza a conta do usuário com os novos dados
    usuarios[cpf]["saldo"] = saldo
    usuarios[cpf]["extrato"] = extrato
    usuarios[cpf]["saques"] = numero_saques

# ======== Início do Programa Principal ========
usuarios = {}

while True:
    print("\n=== BANCO DIGITAL PYTHON ===")
    print("[1] Criar conta")
    print("[2] Acessar conta")
    print("[0] Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        criar_conta(usuarios)
    elif escolha == "2":
        acessar_conta(usuarios)
    elif escolha == "0":
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
