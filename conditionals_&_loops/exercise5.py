#importamos la libreria ramdom
import random

#generamos un numero aleatorio con la libreria.funcion randint
num_ale = random.randint(1, 10)
#definimos i que sea 3 a los numero de intentos posiblies
i = 3 
#creamos un bucle while para determinar si el número es correcto o incorrecto
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
        
