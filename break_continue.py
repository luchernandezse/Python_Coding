def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)
def run2():
    for i in range(10000):
        print (i)
        if i==5678:
            break
def run3():
    texto=input('Escribe texto: ')
    for letra in texto:
        if letra=='o':
            break
        print(letra)

if __name__=='__main__':
    #run()
    #run2()
    run3()