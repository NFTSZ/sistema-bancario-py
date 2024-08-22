# saque, deposito e extrato
extrato = ''
valor_em_conta = 0
saques = 0
LIMITE_SAQUES = 3
limite = 500

while True:
    print(f'\nTotal: {valor_em_conta:.2f}')
    print("[0] Sair [1] Deposito  [2] Saque  [3] Extrato")
    opcao_menu = int(input("Escolha uma opcao: "))

    # Sair do programa
    if opcao_menu == 0:
        print("Volte sempre.")
        break

    # Deposito
    elif opcao_menu == 1:
        valor = float(input("Valor a ser depositado: "))

        if valor > 0:
            valor_em_conta += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            
        else:
            print("Valor inválido.")
    
    # Saque
    elif opcao_menu == 2:
        valor = float(input("Valor a ser sacado: "))

        excedeu_limite = valor > limite
        excedeu_saque = saques >= LIMITE_SAQUES
        excedeu_valor = valor > valor_em_conta

        if excedeu_limite:
            print("Nao foi possivel completar essa operacoa: Limite de valor excedido. (Max. 500)")

        elif excedeu_saque: 
            print("Nao foi possivel completar essa operacoa: Limite de saques excedido. (Max. 3)")

        elif excedeu_valor: 
            print("Nao foi possivel completar essa operacoa: Saldo insuficiente")

        elif valor > 0:
            valor_em_conta -= valor
            saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        
        else:
            print("valor inválido.")

    # Extrato
    elif opcao_menu == 3:
        print("Nao foram feitas transacoes" if not extrato else extrato)

    else:
        print("Opção inválida.")