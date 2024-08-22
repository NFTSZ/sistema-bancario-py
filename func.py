from datetime import datetime

# cadastrar usuario e criar conta vinculando com o usuario
# saque, deposito e extrato
extrato = ''
valor_em_conta = 0
transacao = 0
# LIMITE_SAQUES = 3
LIMITE_TRANS_DIARIA = 10
limite = 500
excedeu_transacao = transacao >= LIMITE_TRANS_DIARIA
data_hora_atual = datetime.today().replace(microsecond=0)
ultima_data = data_hora_atual.date()
    
def reset_trans():
    global ultima_data
    data_hora_atual = datetime.today().replace(microsecond=0)
    # Capturando data e reiniciando limite de transacoes diarias
    data_hora_atual = datetime.today().replace(microsecond=0)
    if data_hora_atual.date() != ultima_data:
        transacao = 0
        ultima_data = data_hora_atual.date()

def criar_usuario():
    pass
def criar_conta():
    pass

# funcao de deposito
def deposito(valor):
    global excedeu_transacao
    global valor_em_conta
    global extrato
    global transacao
    global data_hora_atual

    if excedeu_transacao:
        print("Nao foi possivel completar essa operacao: Limite de transacoes diarias excedido. (Max. 10)")
    elif valor > 0:
        valor_em_conta += valor
        extrato += f'Deposito: R$ {valor:.2f} | {data_hora_atual}\n'
        transacao += 1
    else:
        print("Valor inválido.")
    return valor
    
# funcao de saque
def saque(valor):
    global excedeu_transacao
    global valor_em_conta
    global extrato
    global transacao
    global data_hora_atual

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

# funcao de mostrar extrato
def mostrar_extrato(extrato):
    print("Nao foram feitas transacoes" if not extrato else extrato)