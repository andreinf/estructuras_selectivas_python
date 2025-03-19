'''
if en cascada:
estructura  selectiva compuesta
por multiples condicionales, seguidos
unos de otros

Sintaxis:
if condicional1:
    instruccion1
    instruccion2

elif condicional2:
    instruccion3
    instruccion4

elif condicional3:
    instruccion5
    instruccion6
NOTA: cada condicional
es MUTUAMENTE EXCLUYENTE
'''
#Ejemplo:
#Vamos a hacer un pequeño traductor
#El programa debe permitir leer
#una fruta en español y debe
#mostrar esa fruta en ingles

fruta_es = input("Ingrese Fruta:")
if fruta_es == "Manzana" or fruta_es == "manzana":
    print("Apple")
elif fruta_es == "Naranja" or fruta_es == "naranja":
    print ("Orange")
elif fruta_es == "Uva" or fruta_es == "uva":
    print ("Grape")
elif fruta_es == "Piña" or fruta_es == "piña":
    print ("Pinneaple")
#Caso por defecto
#Default
    print ("No se encontro traduccion")