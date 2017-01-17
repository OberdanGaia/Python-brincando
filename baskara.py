import math

valorA = int(input("Digite o valor da Variavel A "))
valorB = int(input("Digite o valor da Variavel B "))
valorC = int(input("Digite o valor da Variavel C "))

delta = valorB**2 - 4*valorA*valorC

if delta<0:
    print("Não existem raizes reais")
elif delta==0:
    x = -valorB/(2*valorA)
    print("Existe apenas a raiz real: ",x)
else:
    x1 = (-valorB + math.sqrt(delta))/(2*valorA)
    x2 = (-valorB - math.sqrt(delta))/(2*valorA)
    print("Existem duas raizes reais que são:",x1, " e:",x2)
