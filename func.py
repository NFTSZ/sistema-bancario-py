from datetime import datetime
    
def reset_trans(ultima_data, data_hora_atual, transacao):
    # Capturando data e reiniciando limite de transacoes diarias
    data_hora_atual = datetime.today().replace(microsecond=0)
    if data_hora_atual.date() != ultima_data:
        transacao = 0
        ultima_data = data_hora_atual.date()

# cadastrar usuario e criar conta vinculando com o usuario
def criar_usuario():
    pass
def criar_conta():
    pass

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
    return valor_em_conta
    
# funcao de saque
def saque(valor, excedeu_transacao, valor_em_conta, extrato, transacao, data_hora_atual):
    excedeu_limite = valor > limite
    excedeu_valor = valor > valor_em_conta
    excedeu_transacao = transacao >= LIMITE_TRANS_DIARIA
    
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
    return valor_em_conta
    
# funcao de mostrar extrato
def mostrar_extrato(extrato):
    print("Nao foram feitas transacoes" if not extrato else extrato)
