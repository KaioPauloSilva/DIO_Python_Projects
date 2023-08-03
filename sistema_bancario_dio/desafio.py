import textwrap


def menu():
    menu = '''\n
    -----MENU-----
    [d] Depositar
    [s] Sacar
    [nu] Novo Usuario
    [nc] Nova Conta
    [lc] Listar Contas
    [e] Extrato
    [q] Sair
    ->'''
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n### Depósito realizado com sucesso! ###")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, valor, saldo, limite, extrato, limite_saques, numero_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print('\n ### Saque realizado com sucesso! ###')

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return None


def novo_usuario(usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n###Já existe usuário com este CPF! ###')
        return

    nome = input('Informe o nome completo:')
    data_nascimento = input('Informe sua data de nacscimento (dd-mm-aaaa) :')
    endereço = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado) :')

    usuarios.append({'nome': nome,
                     'data_nascimento': data_nascimento,
                     'endereço': endereço
                     })
    print(' ### Usuário criado com sucesso! ### ')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f'''\n
            Agência:\t{conta['agencia']}
            Conta-Corrente:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}        
'''
    print('#' * 20)
    print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        if opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato, numero_saques = sacar(valor=valor,
                                   saldo=saldo,
                                   limite=limite,
                                   extrato=extrato,
                                   limite_saques=LIMITE_SAQUES,
                                   numero_saques=numero_saques
                                   )
        elif opcao == 'e':
            extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            novo_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break
main()
