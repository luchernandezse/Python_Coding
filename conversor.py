def conversor(tipo_pesos,valor_dolar):
    pesos = float(input("Cuantos pesos" +tipo_pesos+ "deseas convertir?:"))
    dolares =str(round(pesos/valor_dolar,2))
    print("Tienes $"+dolares+" dolares")


menu="""
Bienvenido al conversor de monedas🖥

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
elige una opcion:
"""
opcion=input(menu)

if opcion=='1':
    conversor("Colombianos",3875)
elif opcion=='2':
    conversor("Argentinos",65)
elif opcion=='3':
    conversor("Mexicanos",24)
else:
    print("Ingresa una opcion correcta")

#if opcion=='1':
#    pesos = float(input("Cuantos pesos colombianos deseas convertir?:"))
#    valor_dolar = 3875
#    dolares =str(round(pesos/valor_dolar,2))
#    print("Tienes $"+dolares+" dolares")
#elif opcion=='2':
#    pesos = float(input("Cuantos pesos argentino deseas convertir?:"))
#    valor_dolar = 65
#    dolares =str(round(pesos/valor_dolar,2))
#   print("Tienes $"+dolares+" dolares")
#elif opcion=='3':
#    pesos = float(input("Cuantos pesos mexicanos deseas convertir?:"))
#    valor_dolar = 24
#    dolares =str(round(pesos/valor_dolar,2))
#    print("Tienes $"+dolares+" dolares")
#else:
#    print("Ingresa una opcion correcta")