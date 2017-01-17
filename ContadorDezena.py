valor = int(input("Digite um número para contagem de dezenas "))

dezena = int(valor /10)

dezena = dezena % 10

#Ou poderia ser feito dezena = int(valor%100) e depois dezena = dezena//10

print("A casa da dezena é: ",dezena)
