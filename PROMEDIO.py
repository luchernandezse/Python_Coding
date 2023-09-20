cedulas=[1192758002,1003704661,1004730465,1000512898,1193071413,1062913050,1000589907,1004638038,1000133852,1098608572,1002528645,1002605032,1000611406,1000184284,1003520192,1005236177,1016111439,1052417072,1005832005,1014198336,1071168476,1000325182,1007146673,1053617179,1004134970,1000049791]
print(cedulas)
#num=str(input("ingrese el numero de documento"))

mi_lista=[],
print(type(mi_lista))
mi_lista=list(mi_lista)
print(type(mi_lista))

for i in cedulas:
    num=str(i)
    print(num)
    sum=0
    count=0
    for contador in num:
        print(contador)
        sum=sum+int(contador)
        count=count+1
        
    print(sum/count)
    mi_lista.append(sum/count)

print(mi_lista)
