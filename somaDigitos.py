unidade = int(input("Digite o numero que será somados os digitos "))
somaTotal = 0
while unidade != 0:
    soma = unidade%10
    somaTotal = somaTotal + soma
    unidade = unidade/10
    unidade = int(unidade)

print("O valor da soma é:", somaTotal)
