Palavra_verificada = input("Digite uma palavra: ")
VOGAL = ["A", "E", "I", "O", "U"] 

for Letra in Palavra_verificada:
    if Letra.upper() in VOGAL:
        print(Letra," ")


for Tabuada2 in range(0, 21, 2):
    print(Tabuada2, " ")

opcao = -1
saldo = int(input("Qual o seu saldo? "))
while opcao != 0:
    opcao = int(input("Você deseja sacar (1) ou depositar (2) ou (0)Sair? "))

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