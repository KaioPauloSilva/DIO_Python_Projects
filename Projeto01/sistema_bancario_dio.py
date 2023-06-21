menu = """ 

        ---MENU---
    [1] Depositar
    [2] Sacas
    [3] Extrato
    [4] Sair

    Digite uma das opções:
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:

    opcao = int(input(menu))

    if opcao == 1:
        print('\nDeposito Selecionado!\n\n')
        deposito = float(input('Digite o valor que deseja depositar:'))
        if deposito <= 0 :
            print('Não é possivel depositar este valor negativo!')
        else:
            saldo = deposito
            extrato += f'Depósito no valor de R$ {deposito:.2f}\n'
            print(f'Depósito no valor de R$ {deposito:.2f}. Realizado  com sucesso!')  
    
    elif opcao == 2:
        print('Saque Selecionado!')
        saque = float(input('Digite o valor que deseja sacar:'))
        if saque > saldo:
            print('Você não possui saldo suficiente para sacar!')
        elif numero_saques >= LIMITE_SAQUES:
            print('Você atingiu o limite de saque diário')
        elif saque > limite:
            print(f'Seu limite por saque é de {limite}, digite um valor igual ou menor')
        else:
            saldo -= saque
            extrato += f'Saque no valor de R$ {saque:.2f}\n'
            print(f'Saque no valor de R$ {saque:.2f}. Realizado  com sucesso!')
    elif opcao == 3:
        print('========== EXTRATO ==========')
        if extrato == "":
            print("Nenhuma operação realizada.\n")
        else:
            print(extrato)
            print(f'Saldo atual: R$ {saldo:.2f}')
            numero_saques += 1    
            print(f'Limite disponível: R$ {limite:.2f}')
            print(29 * "=")
    elif opcao == 4:
        print("Obrigado por utilizar o sistema!")
        break
    else:
        print('\nDigite o valor da opção desejada! ')    