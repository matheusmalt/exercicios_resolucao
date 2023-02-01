'''
    Crear un sistema que detecte si un numero es primo o no

    Para solucionar este problema se requiere que el usuario ingres un numero por teclado y el sistema detecte si es primo o no.

    Un numero primo es aquel que se puede dividir solo dos veces por 1 y por sí misma.
'''

import sys

def primo(numero):
    mult = 0
    for cont in range(2, numero):
        if numero % cont == 0:
            mult += 1
    
    if mult == 0:
        print("Primo")
    else:
        print("Não é primo")

menu = """
 _______            __                         
/       \          /  |                        
$$$$$$$  | ______  $$/  _____  ____    ______  
$$ |__$$ |/      \ /  |/     \/    \  /      \ 
$$    $$//$$$$$$  |$$ |$$$$$$ $$$$  |/$$$$$$  |
$$$$$$$/ $$ |  $$/ $$ |$$ | $$ | $$ |$$ |  $$ |
$$ |     $$ |      $$ |$$ | $$ | $$ |$$ \__$$ |
$$ |     $$ |      $$ |$$ | $$ | $$ |$$    $$/ 
$$/      $$/       $$/ $$/  $$/  $$/  $$$$$$/  
                                               
"""

def main():
    try:
        print(menu)
        numero = int(input("Digite o número: "))
        primo(numero)
    except:
        print("Erro")
        sys.exit(0)


main()
