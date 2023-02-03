'''
    Crear un sistema que convierta de moneda nacional a dólares por ejemplo de soles peruanos a dólares, pesos mexicanos a dólares, pesos colombianos a dólares.

    Para solucionar este problema se requiere que el usuario ingrese la cantidad de monedas nacionales y luego realizar la conversión.

    Para este sistema debe hacer un menú de navegación para seleccionar a que tipo de moneda se ara la conversión y también para cerrar el programa, el sistema no se debe cerrarse si no lo deseas.
'''
import sys

menu = """
    [1] - Soles Peruanos a Dolares
    [2] - Pesos Mexicanos a Dolares
    [3] - Pesos Colombianos a Dolares
    [4] - Real para Dolares
    [qualquer tecla] - Sair
    Digite uma opção:
"""
def conversor(dolar, pais):
    quantidade_moeda = float(input(f"Quantidade de {pais}: "))
    dolares = quantidade_moeda / dolar
    dolares = round(dolares, 2)
    print(f"Você tem {dolares}")

def main():
    while True:
        try:
            opcao = int(input(menu))
            if opcao == 1:
                conversor(3.89, "soles peruanos")
            elif opcao == 2:
                conversor(18.66, "pesos mexicanos")
            elif opcao == 3:
                conversor(4693.24, "pesos colombianos")
            elif opcao == 4:
                conversor(5.05, "real")
            else:
                print("Saindo")
                break
        except:
            print("Saindo")
            sys.exit()

main()
