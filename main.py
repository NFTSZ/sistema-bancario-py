# aqui importamos as bibliotecas a serem trabalhadas no codigo
from datetime import datetime

'''
Definição de constantes
    LIMITE_TRANS_DIARIA: número máximo de transações diárias;
    AGENCIA: número da agência bancária;
'''
LIMITE_TRANS_DIARIA = 10
AGENCIA = "0001"

'''
Inicialização de variáveis:
    extrato: Armazena o histórico de transações em formato de string;
    valor_em_conta: O saldo atual da conta;
    transacao: Contador de quantas transações foram feitas no dia;
    limite: Limite de saque (neste caso, R$500);
    usuarios: Lista para armazenar os dados dos usuários cadastrados;
    contas: Lista para armazenar as contas criadas;
    '''
extrato = ''
valor_em_conta = 0
transacao = 0
limite = 500
usuarios = []
contas = []

'''
Definicao das variaveis que irao tratar do reset diario, `ultima_data` armazena
apenas a parte da data (sem a hora) para facilitar o controle de reset das 
transações diárias. 
'''
excedeu_transacao = transacao >= LIMITE_TRANS_DIARIA
data_hora_atual = datetime.today().replace(microsecond=0)
ultima_data = data_hora_atual.date()

'''
Função para resetar transações diárias: Verifica se houve mudança de dia e reseta
o contador de transações diárias se necessário. Se a data atual for diferente da
última data registrada (ultima_data), as transações são resetadas para 0 e a última
data é atualizada.
'''
def reset_trans(ultima_data, data_hora_atual, transacao):
    # Capturando data e reiniciando limite de transacoes diarias
    data_hora_atual = datetime.today().replace(microsecond=0)
    if data_hora_atual.date() != ultima_data:
        transacao = 0
        ultima_data = data_hora_atual.date()
    return ultima_data, transacao

'''
Função para depósito: Realiza um depósito na conta e atualiza o saldo, extrato 
e contador de transações. Verifica se o limite de transações diárias foi excedido
antes de permitir o depósito. Caso não, verifica se o valor é positivo. Se sim, 
ele é adicionado ao saldo da conta, registrado no extrato, e o contador de transações
é incrementado.
'''
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

'''
Função para saque: Realiza um saque da conta, com verificação de saldo, limite de 
saque e limite de transações. Confere se o valor do saque excede o limite diário,
o saldo em conta ou o número de transações diárias permitidas. Se todas as condições
forem atendidas (sem exceder limite e com saldo suficiente), o valor é debitado da
conta e o extrato e contador de transações são atualizados.
'''
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
        extrato += f"Saque: R$ {valor:.2f} | {data_hora_atual}\n"
        transacao += 1
    else:
        print("valor inválido.")
    return valor_em_conta, extrato, transacao

'''
Mostrar saldo total: Função simples que exibe o saldo da conta formatado com duas casas decimais.
'''
def mostrar_total(valor_em_conta):
    print(f'\nTotal: {valor_em_conta:.2f}')

'''
Exibe as transações feitas, ou uma mensagem indicando que não houve transações.
'''
def mostrar_extrato(extrato):
    print("Nao foram feitas transacoes" if not extrato else extrato)

'''
Filtrar usuário por CPF: Busca um usuário na lista de usuários com base no CPF.
Retorna o primeiro encontrado, ou None se não houver correspondência.
'''
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

'''
Criar novo usuário: Pede as informações do usuário e o adiciona à lista de usuários.
Verifica, filtrando o CPF, se já existe na lista. Se sim, retorna uma mensagem informando
que o usuário já está cadastrado. Caso contrário, solicita as demais informações e
adiciona o usuário à lista.
'''
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Ja existe um usuario com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco': endereco})

    print("Usuario cadastrado com sucesso!")

'''
Criar nova conta: Associa uma conta a um usuário existente, buscando-o por CPF. Caso
o cpf nao esteja vinculado a nenhum usuario, mostra um aviso.
'''
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print("Usuario nao encontrado. Crie um usuario primeiro!")

'''
Listar contas: Exibe todas as contas criadas, mostrando o nome do titular,
a agência e o número da conta.
'''
def listar_contas(contas):
    for conta in contas:
        print(f"""
        Titular: {conta['usuario']['nome']}  
        Agencia: {conta['agencia']}  
        C/C: {conta['numero_conta']}""")
        print("""
        ="""* 100)


'''
Loop principal do programa: Exibe o saldo e um menu de opções. A execução do loop
só termina se o usuário selecionar a opção 0 para sair.
'''
while True:
    ultima_data, transacao = reset_trans(ultima_data, data_hora_atual, transacao)
    mostrar_total(valor_em_conta)
    print("[0] Sair  [1] Deposito  [2] Saque  [3] Extrato  [4] Cadastrar usuario  [5] Criar conta  [6] Listar contas")
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

    # Novo usuario
    elif opcao_menu == 4:
        criar_usuario(usuarios)

    # Nova conta
    elif opcao_menu == 5:
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        # Se a função retornar uma conta (não for None), este bloco será executado.
        if conta:
            contas.append(conta)

    # Listar contas existentes
    elif opcao_menu == 6:
        listar_contas(contas)

    else:
       print("Opção inválida.")
