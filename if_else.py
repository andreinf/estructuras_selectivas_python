'''

Sintaxis:
if condicional:
    Instrucción1
    Instrucción2
else:
    Instrucción3
    Instrucción4
'''

#Ejemplo:
#Elabore un rpograma en python que determine
#si una persona es mayor o menor de edad
#y por tanto, habilitada para votar

edad = int(input("Ingrese su edad"))
documento = input ("Tiene documento si/no")
if edad >= 18 and documento== "si":
    print("Usted es mayor de edad")
    print("Puede votar")
else:
    print("Usted es menor de edad")
    print("o")
    print("No puede votar")
print("Fin del programa")
