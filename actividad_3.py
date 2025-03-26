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
==>Para el caso de prestacion de servicios
    Se debe solicitar:
    - el valor del contrato
    - el numero de meses del contrato
    - la antiguedad del empleado(años)
    El salario neto, en este caso se calcula
    1- dividir el valor de contrato 
        por el numero de meses
    2- restar el 0.15% del valor anterior
        por concepto de EPS
    3- restar el 10% de valor del salario mensual,
        por concepto de Pension
    4- si el empleado tiene una antiguedad igual o superior a 10 años
        tendra una bonificacion del 0.5% sobre el valor mensual

==> para el caso de contrato a termino indenido
    se debe solicitar:
    - antiguedad(años)
    - grado o escalafon (1 - 5)
    - el salario minimo 
    El salario mensual se calcula de acuerdo
    a la siguiente tabla:
    - grado 1: 1.5 SM
    - grado 2: 1.7 SM 
    - grado 3: 2.0 SM
    - grado 4: 2.5 SM
    - grado 5: 3.0 SM
    La bonificacion estara acorde a 
    los siguentes rangos segun la antiguedad
    - entre 1 y 5 años: 1% del salario mensual
    - entre 6 y 10 años: 2% del salario mensual
    - superior a 10 años: 3% del salario mensual
    para este caso, los descuentos de ley son:
    - 25% por concepto de EPS 
    - 22% por concepto de pension
    - 0.1% por concepto del ARL
    
'''

contrato = input("Ingrese el tipo de contrato")
#Inicializar variables
# dar valor inicial a una variable
# asi no se utilice en el momento
salario_neto = 0

if contrato == "a":
    print("Contrato a termino indefinido")
    antiguedad = int(input("Ingrese antiguedad del empleado"))
    grado = int(input("Ingrese grado"))
    salario_minimo = int(input("Ingrese valor del salario"))
    salario_mensual = 0
    if grado == 1 :
        salario_mensual = salario_minimo * 1.5
    if grado == 2 :
        salario_mensual = salario_minimo * 1.7
    if grado == 3 :
        salario_mensual = salario_minimo * 2.0
    if grado == 4 :
        salario_mensual = salario_minimo * 2.5
    if grado == 5 :
        salario_mensual = salario_minimo * 3.0
    ###calcular bonificacion
    bonificacion = 0 
    if antiguedad >= 1 and antiguedad <=5:
        bonificacion = salario_mensual * 0.01
    if antiguedad >= 5 and antiguedad <=10:
        bonificacion = salario_mensual * 0.02
    if antiguedad >= 10:
        bonificacion = salario_mensual * 0.03
    ##descuentos de ley
    eps = salario_mensual * 0.25
    pension = salario_mensual * 0.22
    arl = salario_mensual * 0.001
    salario_neto = salario_mensual - eps - pension - arl + bonificacion
  
         

elif contrato == "b":
    print("Contrato por prestacion de servicios")
    valor_contrato = int(input("Ingresa valor de contrato"))
    numero_meses = int(input("Ingrese numero de meses"))
    antiguedad = int(input("Ingrese antiguedad del empleado(años)"))
    salario_mensual = valor_contrato / numero_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.5
    salario_neto = salario_mensual - eps - pension
    if antiguedad >= 10:
        salario_neto = salario_neto + bonificacion

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
    valor_hora = int(input("Ingr ese valor por hora a pagar"))
    salario_neto = numero_horas * valor_hora

else:
    print ("Tipo de contrato nno existente")
print ("El salario neto es:" , salario_neto)
print("Fin del programa")

