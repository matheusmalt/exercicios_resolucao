# Digite 6 números em uma lista e obtenha o maior e o menor número inserido.

lista = list()
print("Digite 6 números")
for i in range(1, 7):
    numero = int(input("Digite um número: "))
    print(f"Números digitados [{i}]")
    lista.append(numero)
    
lista = sorted(lista)
    
print("Maior número: {}".format(lista[5]))
print("Menor número: {}".format(lista[0]))
