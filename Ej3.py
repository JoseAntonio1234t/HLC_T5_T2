nota=int(input("Escribe una calificación entre 0 y 100: "))

if(nota<0 or nota>100):
    
    print("Por favor, escriba una calificación comprendido entre 0 y 100")
    
elif nota >=50:
    
    print("Aprobado.")
    
else:
    
    print("Reprobado.")