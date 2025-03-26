'''
if anidados:
if dentros de otros if 

Syntax:
if condicion:
    if condicion:
        print("mensaje")
    else:
        print("mensaje")
No confundir con elif 
'''

#Ejemplo:1
#MOdifique ele ejercicio de la edad 
#para las siguientes comdiciones
#1. Si es mayor de 18 años
#   pero no tiene documento, no puede votar
#   de lo contrario si puede votar
#2. Si es menor de 18 años
#   no puede votar
#   utilice estructura de if anidados

edad = int(input("Ingrese su edad"))
if edad >= 18:
    documento = input ("Tiene documento? (si/no)")
    if documento == "si":
        print("Puede votar, todo en regla")
    else:
        print("No puede votar, no tiene documento")
else:
    print("No puede votar, es menor de edad")
