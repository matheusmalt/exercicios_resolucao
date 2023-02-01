# Dados 4 números, retorne os números em ordem crescente.
lista = []
print("Tudo em ordem")
for i in range(1,5):
    numero = int(input(f"DIgite o {i} número: "))
    lista.append(numero)

lista = sorted(lista)
print("Números em ordem: {}".format(lista))
