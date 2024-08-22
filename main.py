from datetime import datetime

extrato = ''
valor_em_conta = 0
transacao = 0
# LIMITE_SAQUES = 3
LIMITE_TRANS_DIARIA = 10
limite = 500

excedeu_transacao = transacao >= LIMITE_TRANS_DIARIA
data_hora_atual = datetime.today().replace(microsecond=0)
ultima_data = data_hora_atual.date()

while True:
    reset_trans(ultima_data, data_hora_atual, transacao)

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
        deposito(valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual)
    
    # Saque
    elif opcao_menu == 2:
        valor = float(input("Valor a ser sacado: "))
        saque(valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual)

    # Extrato
    elif opcao_menu == 3:
        mostrar_extrato(extrato)

    else:
        print("Opção inválida.")