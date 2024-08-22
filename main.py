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
    ultima_data, transacao = reset_trans(ultima_data, data_hora_atual, transacao)

    mostrar_total(valor_em_conta)
    print("[0] Sair [1] Deposito  [2] Saque  [3] Extrato")
    opcao_menu = int(input("Escolha uma opcao: "))

    # Sair do programa
    if opcao_menu == 0:
        print("Volte sempre.")
        break

    # Deposito
    elif opcao_menu == 1:
        valor = float(input("Valor a ser depositado: "))
        valor_em_conta, extrato, transacao = deposito(valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual)
    
    # Saque
    elif opcao_menu == 2:
        valor = float(input("Valor a ser sacado: "))
        valor_em_conta, extrato, transacao = saque(valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual)

    # Extrato
    elif opcao_menu == 3:
        mostrar_extrato(extrato)

    else:
        print("Opção inválida.")
