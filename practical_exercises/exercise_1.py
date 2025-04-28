## Ejercicios Prácticos de Python 1

# Solicita el nombre y edad del usuario, luego imprime un saludo personalizado que incluya ambos datos

print("--------------------------------------")
Name = str(input("Ingresa tu nombre:  "))
print("--------------------------------------")
Age = int(input("Ingresa tu edad:  "))
print("--------------------------------------")
print(f"Hola {Name},  espero que estes bien, Oh estas grande tienes {Age} ")


# # 1.2
# Pide al usuario que ingrese su comida favorita y su color favorito, luego imprime una frase con ambos.
print("--------------------------------------")
Food = str(input("Ingresa tu comida favorita:  "))
print("--------------------------------------")
Color = str(input("Ingresa tu color favorito:  "))
print("--------------------------------------")
print(f"Oh, tu comida favorita es {Food}, la mia tambien, sera por que nos gusta el color {Color}  ")

# # 1.3
# Solicita un número y muestra su doble y su triple.
Num = int(input("Ingresa un numero:  "))
print(f"El doble de ese numero es {Num*2} y su triple es {Num*3}")
