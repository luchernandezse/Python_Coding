# Es bueno tener definida una función que tenga referencia como a un arranque de la función.
def palindromo (palabra):
    palabra=palabra.replace(' ','')
    palabra=palabra.lower()
    palabra_inv= palabra[::-1]
    print (palabra_inv)
    if palabra== palabra_inv:
        return True
    else:
        return False


def run():
    palabra= input('Ingrese la palabra:')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print ('Es palindromo')
    else:
        print('No es palindromo')

# Entry point: una vez python encuentra esto, corre lo que esta debajo
if __name__=='__main__':
    run()