from datetime import datetime
from time import sleep

LIMITE_TRANS_DIARIA = 10
AGENCIA = "0001"

extrato = ''
valor_em_conta = 0
transacao = 0
limite = 500
usuarios = []
contas = []

excedeu_transacao = transacao >= LIMITE_TRANS_DIARIA
data_hora_atual = datetime.today().replace(microsecond=0)
ultima_data = data_hora_atual.date()


def reset_trans(ultima_data, data_hora_atual, transacao):
    # Capturando data e reiniciando limite de transacoes diarias
    data_hora_atual = datetime.today().replace(microsecond=0)
    if data_hora_atual.date() != ultima_data:
        transacao = 0
        ultima_data = data_hora_atual.date()
    return ultima_data, transacao

# funcao de deposito
def deposito(valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual):
    excedeu_transacao = transacao >= LIMITE_TRANS_DIARIA
    if excedeu_transacao:
        print("Nao foi possivel completar essa operacao: Limite de transacoes diarias excedido. (Max. 10)")
    elif valor > 0:
        valor_em_conta += valor
        extrato += f'Deposito: R$ {valor:.2f} | {data_hora_atual}\n'
        transacao += 1
    else:
        print("Valor inválido.")
    return valor_em_conta, extrato, transacao

# funcao de saque
def saque(valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual):
    excedeu_limite = valor > limite
    excedeu_valor = valor > valor_em_conta
    excedeu_transacao = transacao >= LIMITE_TRANS_DIARIA

    if excedeu_limite:
        print(
            "Nao foi possivel completar essa operacao: Limite de valor excedido. (Max. 500)")
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
    return valor_em_conta, extrato, transacao

# mostra o saldo total em conta
def mostrar_total(valor_em_conta):
    print(f'\nTotal: {valor_em_conta:.2f}')

# funcao de mostrar extrato
def mostrar_extrato(extrato):
    print("Nao foram feitas transacoes" if not extrato else extrato)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# cadastrar usuarios
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Ja existe um usuarioc com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereco (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco': endereco})

    print("Usuario cadastrado com sucesso!")

# criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print("Usuario nao encontrado. Crie um usuario primeiro!")

while True:
    ultima_data, transacao = reset_trans(ultima_data, data_hora_atual, transacao)
    mostrar_total(valor_em_conta)
    print("[0] Sair [1] Deposito  [2] Saque  [3] Extrato [4] Cadastrar usuario  [5] Criar conta")
    opcao_menu = int(input("Escolha uma opcao: "))

    # Sair do programa
    if opcao_menu == 0:
        print("Volte sempre.")
        break

    # Deposito
    elif opcao_menu == 1:
        valor = float(input("Valor a ser depositado: "))
        valor_em_conta, extrato, transacao = deposito(
            valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual)

    # Saque
    elif opcao_menu == 2:
        valor = float(input("Valor a ser sacado: "))
        valor_em_conta, extrato, transacao = saque(
            valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual)

    # Extrato
    elif opcao_menu == 3:
        print("\n===============================")
        mostrar_extrato(extrato)
        print("\n===============================")

    elif opcao_menu == 4:
        criar_usuario(usuarios)

    elif opcao_menu == 5:
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        if conta:
            contas.append(conta)

    else:
       print("Opção inválida.")
