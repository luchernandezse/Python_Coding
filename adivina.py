import random

menu="""
Bienvenido al juego adivina un numero*****
Tienes un total de 8 vidas

comencemos!
Ingresa un número entre el 1 y el 100: 
"""

def run():
    num_ale=random.randint(1,100)
    num_eleg=int(input(menu))
    vida=8
    while num_ale!=num_eleg:
        if num_eleg<num_ale:
            print('Escoge un numero mayor')
        else:
            print('Escribe un numero menor')
        num_eleg=int(input('intenta otro numero: '))
        vida-=1
        if vida==0:
            print('Has perdido todas tus vidas :( ')
            print('El numero era: ' + str(num_ale))
            break
    if num_ale==num_eleg:
        print('Has ganado!!')

if __name__=='__main__':
    run()numero2=[6,7,8,9]