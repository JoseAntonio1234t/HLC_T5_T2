cadena = input("Introduce una cadena: ")
special_chars = ["@","#","$","%"]
for char in special_chars:
    if char in cadena:
        print("La cadena",cadena,"contiene @, %, # o $")