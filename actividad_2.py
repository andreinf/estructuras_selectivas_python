estrato = int(input("Digita tu estrato"))
edad = int(input("Digita tu edad"))

if edad > 18 and estrato == 1:
    print("Si es mayor de edad")
    print("Tiene el 20% de descuento en su matricula")
elif edad <= 18 and estrato == 1:
    print("NO es mayor de edad")
    print("Tiene el 15% de descuento en su matricula")
elif edad >18 and estrato == 2:
    print("Si es mayor de edad")
    print("Tiene el 10% de descuento en su matricula")
elif edad <=18 and estrato == 2:
    print("NO es mayor de edad")
    print("Tiene el 5% de descuento en su matricula")
else: 
    print ("No se puede")