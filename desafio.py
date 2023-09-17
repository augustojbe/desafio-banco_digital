menu = """
 Bom vindo ao Banco, escolha um dos nossos serviços
===================================================
                [d] = Depositar
                [s] = Sacar
                [e] = extrato
                [q] = Sair 
===================================================
"""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual o valor que voce que depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao =="s":
        valor = float(input("Qual o valor que voce que sacar: "))

        excedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        exedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif exedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        elif exedeu_saque:
            print("Operação falhou! Número maximo de saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n "
            numero_saque += 1
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n=======================Extrato============================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {valor:.2f}\n ")
        print("\n==========================================================")

    elif opcao == "q":
        print("Obrigado por usar nossos serviços")
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada. ")




