intentos = 0
while intentos < 3:
    contraseña = input("Introduce una contraseña: ")
    if contraseña == "contraseña123":
        print("La contraseña es correcta, ¡Bienvenido!")
        break
    else:
        intentos += 1
        print("intento nº",intentos,",Contraseña incorrecta")
else:
    print("Te has quedado sin intentos")
        