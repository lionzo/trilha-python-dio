menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informar valor de depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: + R${valor_deposito:.2f}\n"
            print(f"""
                +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
                                                        
                Depósito realizado com sucesso!     
                Seu saldo agora é de R${saldo:.2f}   
                                                        
                =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=""")
        else: 
            print(f"""
                  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                  Valor inválido para depósito. Tente novamente!
                  
                  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""")

    elif opcao == "s":
        valor_saque = float(input("Informar valor de saque: "))
        if LIMITE_SAQUES > numero_saques:
            if valor_saque < saldo:
                saldo -= valor_saque
                extrato += f"Saque:    - R${valor_saque:.2f}\n"
                numero_saques += 1
                print(f"""
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                                        
                Saque realizado com sucesso!     
                Seu saldo agora é de R${saldo:.2f}   
                                                        
                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            elif valor_saque > saldo:
                print(f"""
                ===============================
                                                        
                Seu saldo é insuficiente para
                realizar o saque.      
                Seu saldo atual é de R${saldo:.2f}   
                                                        
                ===============================""")
            else:
                (f"""
                  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                    Valor inválido para saque. Tente novamente!
                  
                  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""")
        else:
            print(f"""
                ===============================
                                                        
                O limite de saques foi atingido.
                Você deve tentar novamente em 24h.   
                                                        
                ===============================""")

    elif opcao == "e":

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
