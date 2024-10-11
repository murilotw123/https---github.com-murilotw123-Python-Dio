def calcular_tabuada(numero_tabuada, numero_inicio, numero_fim):
    for i in range(numero_inicio, numero_fim, numero_tabuada):
        print(f"A tabuada do {numero_tabuada} é: {i}")

calcular_tabuada(5, 0, 51)        

def calcula_numeros(num):
    return sum(num)

print(calcula_numeros([1,2]))