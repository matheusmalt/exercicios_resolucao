# Dado um intervalo numérico inteiro num. inicial e num. tudo bem, obtenha o número de números positivos e negativos que existem no intervalo.

numeroInicial = int(input("Número inicial: "))
numeroFinal = int(input("Número final: "))
positivos = 0
negativos = 0
     
for numero in range(numeroInicial, numeroFinal +1):
  if numero % 2 == 0:
    positivos += 1
  else:
    negativos += 1
     
print("Positivos: {}".format(positivos))
print("Negativos: {}".format(negativos))

