import random

num_ale = random.randint(1, 10)
i = 3 

while i > 0:    
    num=int(input("Ingrese número: "))
    if num == num_ale:
        print("El número es correcto!!!")
        break
    elif num < num_ale :
        print("El numero es mayor")
    elif num > num_ale :
        print ("El numero es menor ")
        i = i-1
    
    if i==0 :
        print(f"intentos fallidos, el numero es {num_ale}") 
        
