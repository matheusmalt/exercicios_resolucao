# Dado um intervalo de inteiros, encontre o número de inteiros que ele contém.

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

contador = 0
i = numero1 + 1

while i < numero2:
        contador += 1
        i += 1

print("Contador: {}".format(contador))
