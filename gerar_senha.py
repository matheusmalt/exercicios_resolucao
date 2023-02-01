'''
    Crear un sistema que genere una contraseña aleatoria

    Para solucionar este problema se requiere listas,
    listas mayúsculas, lista de minúsculas, lista de números y lista de símbolos
    y luego armar una contraseña aleatoria sacando caracteres de estas listas.
'''

import random, string, sys

menu = """
 _______                               __       __        __ 
/       \                             /  |  _  /  |      /  |
$$$$$$$  | ______    _______  _______ $$ | / \ $$ |  ____$$ |
$$ |__$$ |/      \  /       |/       |$$ |/$  \$$ | /    $$ |
$$    $$/ $$$$$$  |/$$$$$$$//$$$$$$$/ $$ /$$$  $$ |/$$$$$$$ |
$$$$$$$/  /    $$ |$$      \$$      \ $$ $$/$$ $$ |$$ |  $$ |
$$ |     /$$$$$$$ | $$$$$$  |$$$$$$  |$$$$/  $$$$ |$$ \__$$ |
$$ |     $$    $$ |/     $$//     $$/ $$$/    $$$ |$$    $$ |
$$/       $$$$$$$/ $$$$$$$/ $$$$$$$/  $$/      $$/  $$$$$$$/ 
                                                             
"""

def gerar(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = list()
    for i in range(tamanho):
        caracter_random = random.choice(caracteres)
        senha.append(caracter_random)
    
    senha = "".join(senha)
    return senha

def main():
    try:
        print(menu)
        tamanho = int(input("Digite o tamanho da senha: "))
        quantidade = int(input("Digite a quantidade de senhas: "))
        contador = 0
        while contador < quantidade:
            senha = gerar(tamanho)
            print(f"Senha gerada: {senha}")
            contador += 1
    except:
        print("Erro")
        sys.exit()

main()
