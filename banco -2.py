menu = """   
Nosso Banco.
Escolha a operação desejada:

[d] Depositar
[s] Sacar   
[e] Extrato   
[q] Sair  

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

extrato_depositos = []
extrato_saques = []

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor_depositado = input("Informe o valor a ser depositado: ")
        valor_depositado_float = float(valor_depositado)

        if valor_depositado_float <=0:
            print("Depósito não realizado. Os valores depósitados devem ser maiores que 0")
        

        elif valor_depositado_float > 0:
            print (f"Você realizou um depósito no valor de R${valor_depositado_float}")
            saldo += valor_depositado_float
            extrato_depositos.append(valor_depositado_float)

            
        else:
            print ("Algo deu errado. Por favor repita a operação. \nObservação: só são aceitos valores maiores que 0 para depósitos")
            

    elif opcao == "s":

        if numero_saques < LIMITES_SAQUES:
            saque = float(input("Informe o valor sacado: "))
            

            if saque > saldo: 
                print("Seu saldo não é suficiente para realizar esse saque")

            elif saque > 500:
                print("O valor sacado deve ser inferior a R$500,00")

            elif saque <= 0:
                print("O valor informado não pode ser sacado")

            elif saque <= saldo:
                print(f"Voccê realizou um saque de no valor de R${saque}. \nAguarde a contagem das notas")
                extrato_saques.append(saque)
                saldo -= saque
                numero_saques += 1

        

        else:
            print ("Você já alcançou seu limite de três saques diários")


    
    elif opcao == "e":
        print("Extrato de Conta Bancária")
        print(f"Seu saldo é R${saldo}")

        for index, depo in enumerate(extrato_depositos):
            print("Deposito", index +1, ":", depo)

        for index, saqu in enumerate(extrato_saques):
            print("Saque", index +1, ":", saqu)
    
    elif opcao == "q":
        print("Nosso Banco. \nObrigado por utilizar nosso sistema.")
        break
        

    else:
        print ("Operação Inválida, por favor selecione novamente a operação desejada. ")
