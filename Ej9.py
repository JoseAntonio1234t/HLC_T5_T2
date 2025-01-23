import random

numerosrandom = random.randint(1, 50)  # Número aleatorio entre 1 y 50 (ambos incluidos)
numusuario = int(input("Introduce un número: "))

while numusuario != numerosrandom:
    if numusuario < numerosrandom:
        print("El número es mayor. Intenta nuevamente.")
    else:
        print("El número es menor. Intenta nuevamente.")
    
    numusuario = int(input("Introduce un número: "))

print(f"Has acertado el número. Tu número ha sido el: {numusuario}, y el número aleatorio ha sido el: {numerosrandom}.")
