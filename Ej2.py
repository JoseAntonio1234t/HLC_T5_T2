# En primer lugar, pedimos a los usuarios que introduzcan tres números.
# int se usa para indicar en el input que estamos pidiendo un número entero y no texto.


num1 = int(input("Introduce el primer número:"))
num2 = int(input("Introduce el segundo número:"))
num3 = int(input("Introduce el tercer número:"))

def comparaciondatos(num1, num2, num3):
# Utilizando los condicionales if, elif y else pediremos las siguientes condiciones.
    if num1 > num2 and num1 > num3:
        print("El",num1,"es el mayor")
    elif num2 > num1 and num2 > num3:
        print("El",num2,"es el mayor")
    else:
        print("El",num3,"es el mayor")
        
comparaciondatos(num1, num2, num3)

def valoresiguales(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        print("El",num1,"es igual que el",num2,"y el",num3)
    elif num1 == num2:
        print("El",num1,"es igual que el",num2)
    elif num1 == num3:
        print("El",num1,"es igual que el",num3)
valoresiguales(num1, num2, num3)