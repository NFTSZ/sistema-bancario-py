from datetime import datetime

# saque, deposito e extrato
extrato = ''
valor_em_conta = 0
transacao = 0
# LIMITE_SAQUES = 3
LIMITE_TRANS_DIARIA = 10
limite = 500

data_hora_atual = datetime.today().replace(microsecond=0)
ultima_data = data_hora_atual.date()

while True:
    # Capturando data e reiniciando limite de transacoes diarias
    data_hora_atual = datetime.today().replace(microsecond=0)
    if data_hora_atual.date() != ultima_data:
        transacao = 0
        ultima_data = data_hora_atual.date()

    print(f'\nTotal: {valor_em_conta:.2f}')
    print("[0] Sair [1] Deposito  [2] Saque  [3] Extrato")
    opcao_menu = int(input("Escolha uma opcao: "))

    excedeu_transacao = transacao >= LIMITE_TRANS_DIARIA
    # Sair do programa
    if opcao_menu == 0:
        print("Volte sempre.")
        break

    # Deposito
    elif opcao_menu == 1:
        valor = float(input("Valor a ser depositado: "))

        if excedeu_transacao:
            print("Nao foi possivel completar essa operacao: Limite de transacoes diarias excedido. (Max. 10)")

        elif valor > 0:
            valor_em_conta += valor
            extrato += f'Deposito: R$ {valor:.2f} | {data_hora_atual}\n'
            transacao += 1
            
        else:
            print("Valor inválido.")
    
    # Saque
    elif opcao_menu == 2:
        valor = float(input("Valor a ser sacado: "))

        excedeu_limite = valor > limite
        excedeu_valor = valor > valor_em_conta

        if excedeu_limite:
            print("Nao foi possivel completar essa operacao: Limite de valor excedido. (Max. 500)")

        elif excedeu_valor: 
            print("Nao foi possivel completar essa operacao: Saldo insuficiente")
        
        elif excedeu_transacao:
            print("Nao foi possivel completar essa operacao: Limite de transacoes diarias excedido. (Max. 10)")

        elif valor > 0:
            valor_em_conta -= valor
            transacao += 1
            extrato += f"Saque: R$ {valor:.2f} | {data_hora_atual}\n"
        
        else:
            print("valor inválido.")

    # Extrato
    elif opcao_menu == 3:
        print("Nao foram feitas transacoes" if not extrato else extrato)

    else:
        print("Opção inválida.")