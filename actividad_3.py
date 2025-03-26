'''
Actividad 3:
Elabore un programa que 
permita calcular el salario
neto de un empleado,

despues de descontar los descuentos
por concepto de:
Salud, Pension, ARL
1. eL programada debe solicitar
    el tipo de empleado
    a - Contrato a termino indefinido
    b - Contrato por prestacion de servicios
    c - Contrato de aprendizaje
    d - contrato por Jornal(Freelance)
==>
    Se debe solicitar
    - numero de horas trabajadas
    - el valor a pagar por hora
    - el total del salario se calcula de multiplicar
      el numero de horas por el valor a pagar por hora
'''

contrato = input("Ingrese el tipo de contrato")
#Inicializar variables
# dar valor inicial a una variable
# asi no se utilice en el momento
salario_neto = 0

if contrato == "a":
    print("Contrato a termino indefinido")
elif contrato == "b":
    print("Contrato por prestacion de servicios")
elif contrato == "c":
    print("Contrato de aprendizaje")
    salario_minimo = int(input("Ingrese valor del salario minimo:"))
    salario_neto =  salario_minimo - (salario_minimo * 0.25)
elif contrato == "d":
    print("Contrato por Jornal")
    #varaible local:
    #variable que solo se utilizar
    #en un bloque de codigo
    numero_horas = int(input("Ingrese numero horas"))
    valor_hora = int(input("Ingrese valor por hora a pagar"))
    salario_neto = numero_horas * valor_hora

else:
    print ("Tipo de contrato nno existente")
print ("El salario neto es:" , salario_neto)
print("Fin del programa")

