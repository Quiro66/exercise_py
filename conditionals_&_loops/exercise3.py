#Le decimos al usuario que ingrese un número 
num = int(input("Ingrese el número para multiplicar: "))
#Creamos un bucle for con iteracion de rango de 1 a 11 para que imprima las tablas del 1 al 10
for i in range(1,11): 
    print(f"{num} x {i} = {num*i}")
    i = i+1
