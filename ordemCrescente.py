m n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if(n1 <= n2 and n2 <= n3):
    print("Os valores",n1,n2,n3, "estão em ordem Crescente")
else:
    print("Os valores não estão em ordem crescente")
