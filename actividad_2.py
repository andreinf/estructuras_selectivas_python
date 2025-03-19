estrato = int(input("Digita tu estrato"))
edad = int(input("Digita tu edad"))
precio = int(input("Digita el valor de la matricula"))


if edad > 18 and estrato == 1:
    print("Si es mayor de edad")
    print("Tiene el 20% de descuento en su matricula")
    descuento= precio * 0.2
elif edad <= 18 and estrato == 1:
    print("NO es mayor de edad")
    print("Tiene el 15% de descuento en su matricula")
    descuento= precio * 0.15
elif edad >18 and estrato == 2:
    print("Si es mayor de edad")
    print("Tiene el 10% de descuento en su matricula")
    descuento= precio * 0.1
elif edad <=18 and estrato == 2:
    print("NO es mayor de edad")
    print("Tiene el 5% de descuento en su matricula")
    descuento= precio * 0.05


total_pagar = precio - descuento
print ("Valor total de matricula", total_pagar)