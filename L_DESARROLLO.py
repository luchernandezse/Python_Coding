# Maximo
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b

# Ld es la funcion de longitud de desarrollo que depende de la calidad del concreto CQ
def Ld(CQ):
    CQ=CQ

# GE define la longitud del gancho estandard
def GE(db):
    GE180=maximum(db*4,65)
    GE90=db*12

# LDR es la funcion de longitud de desarrollo reducida
#def LDR(CQ):

menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def run():
    while(True):
        print_menu()
        option = int(input('Enter your choice: '))
        if option == 1:
            print('Handle option \'Option 1\'')
        elif option == 2:
            print('Handle option \'Option 2\'')
        elif option == 3:
            print('Handle option \'Option 3\'')
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

    CQ = float(input("Ingrese la calidad del concreto en MPa: "))
    nMIN = int(input("Ingrese el numero de barra menor para el que desea la LD : "))
    nMAX = int(input("Ingrese el numero de barra mayor para el que desea la LD : "))
    mtd = int(input("Ingrese el metodo para calcular la longitud de desarrollo : "))
    print("se hara el analisis para las siguientes barras ")

# Entry point: una vez python encuentra esto, corre lo que esta debajo
if __name__=='__main__':
    run()