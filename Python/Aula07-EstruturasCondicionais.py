saldo = int(input("Qual o seu saldo? "))
'''
saque = int(input("Qual o valor do saque? "))

if saldo >= saque:
    print("Saque realizado com sucesso")
else:
    print("Saque não realizado")

'''



opcao = int(input("Você deseja sacar (1) ou depositar (2)? "))

if opcao == 1:
    saque = int(input("Qual o valor do saque? "))
    saldo -= saque
    print("Saque realizado com sucesso")
    print(f"Seu novo saldo é {saldo}")
elif opcao == 2:
    deposito = int(input("Qual o valor do deposito? "))
    saldo += deposito
    print("Deposito realizado com sucesso")
    print(f"Seu novo saldo é {saldo}")
