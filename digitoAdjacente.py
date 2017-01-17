numero = int(input("Digite um número para verificação "))

adjacente = False

while not adjacente:
    ultimoNumero = numero%10
    numero = int(numero/10)
    penultimoNumero = numero%10
    if ultimoNumero == penultimoNumero:
        adjacente = True

if adjacente:
    print("Número adjacente",ultimoNumero, ",",penultimoNumero,"encontrados")
else:
    print("Este número não possui valores adjacentes")
