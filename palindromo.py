'''
Crear un sistema que detecte si una palabra es palíndroma o no

Para solucionar este problema el usuario tiene que ingresar por pantalla una palabra y el sistema verificas si es palíndromo o no.

Una palabra palíndroma se lee de igual formo como de la derecha y de la izquierda.
'''
import sys

def palindromo(palavra):
    reverso = palavra[::-1]
    if palavra == reverso:
        print("São palindromos")
    else:
        print("Não são palindromos")

menu = """


                     __  __                  __                                             
                    /  |/  |                /  |                                            
  ______    ______  $$ |$$/  _______    ____$$ |  ______    ______   _____  ____    ______  
 /      \  /      \ $$ |/  |/       \  /    $$ | /      \  /      \ /     \/    \  /      \ 
/$$$$$$  | $$$$$$  |$$ |$$ |$$$$$$$  |/$$$$$$$ |/$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |
$$ |  $$ | /    $$ |$$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |$$ | $$ | $$ |$$ |  $$ |
$$ |__$$ |/$$$$$$$ |$$ |$$ |$$ |  $$ |$$ \__$$ |$$ |      $$ \__$$ |$$ | $$ | $$ |$$ \__$$ |
$$    $$/ $$    $$ |$$ |$$ |$$ |  $$ |$$    $$ |$$ |      $$    $$/ $$ | $$ | $$ |$$    $$/ 
$$$$$$$/   $$$$$$$/ $$/ $$/ $$/   $$/  $$$$$$$/ $$/        $$$$$$/  $$/  $$/  $$/  $$$$$$/  
$$ |                                                                                        
$$ |                                                                                        
$$/                                                                                         

"""
# ASCII art
# https://patorjk.com/software/taag/#p=display&f=Big Money-sw&t=Palindromo
def main():
    try:
        print(menu)
        palavra = input("\nDigite a palavra: ")
        palindromo(palavra)
    except:
        print("Erro")
        sys.exit()

main()
