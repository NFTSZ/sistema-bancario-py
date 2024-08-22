from datetime import datetime
from func import *

while True:
    reset_trans()

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
        deposito(valor)
    
    # Saque
    elif opcao_menu == 2:
        valor = float(input("Valor a ser sacado: "))
        saque(valor)

    # Extrato
    elif opcao_menu == 3:
        mostrar_extrato(extrato)

    else:
        print("Opção inválida.")