def fibonacci():
    a=0
    b=1
    for i in range(20):
        print(a)
        c=a+b
        a=b
        b=c
    
fibonacci()