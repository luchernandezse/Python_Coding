menu_options = {
    1: 'Longitud de desarrollo reducida',
    2: 'Longitud de desarrollo exacta',
    3: 'Empalmes de barras',
    4: 'Ganchos a 90° y 180°',
    5: 'Exit'
}

def CQ():
    CQ = '',
    nMIN='',
    nMAX='',
    bars=[],
    try:
        CQ = float(input('Ingrese la calidad del concreto en MPa:  '))
        nMIN = int(input("Ingrese el numero de barra menor para el que desea la LD : "))
        nMAX = int(input("Ingrese el numero de barra mayor para el que desea la LD : "))
    except:
        print('Revise que este ingresando una calidad de concreto valida ...')
    bars = list(range(nMIN, nMAX+1))
    print("se hara el analisis para las siguientes barras ")
    print(bars)


def print_menu():
    print('Programa para el calculo de longitud de desarrollo. \nEl presente codigo fue desarrollado tomando en cuenta la norma NSR10.')
    print('Primero se debe escoger alguna de las siguientes funciones para arrancar el programa:')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     
     print('Handle option \'Option 1\'')
     CQ()
     print('Hola mundo')

def option2():
     print('Handle option \'Option 2\'')
     CQ()

def option3():
     print('Handle option \'Option 3\'')
     CQ()
def option4():
     print('Handle option \'Option 4\'')
     CQ()

if __name__=='__main__':
    
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
           exit()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')