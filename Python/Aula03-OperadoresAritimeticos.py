Nome = input("Digite o nome do cliente: ")
peso = float(input("Digite o peso do cliente: "))
Altura = float(input("Digite a altura do cliente: "))
Imc = peso / (Altura * Altura)
print(f"O IMC do {Nome} é {Imc:.2f}")