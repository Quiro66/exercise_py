# # exercise 1

# print("--------------------------------------")
# Name = str(input("Ingresa tu nombre:  "))
# print("--------------------------------------")
# Age = int(input("Ingresa tu edad:  "))
# print("--------------------------------------")
# print(f"Hola {Name},  espero que estes bien, Oh estas grande tienes {Age} ")


# # 1.2
# print("--------------------------------------")
# Food = str(input("Ingresa tu comida favorita:  "))
# print("--------------------------------------")
# Color = str(input("Ingresa tu color favorito:  "))
# print("--------------------------------------")
# print(f"Oh, tu comida favorita es {Food}, la mia tambien, sera por que nos gusta el color {Color}  ")

# # 1.3
# Num = int(input("Ingresa un numero:  "))
# print(f"El doble de ese numero es {Num*2} y su triple es {Num*3}")


# # Exercise 2
# entero = int(10)
# flotante = float(3.1415)
# cadena = str("esto esta cabronn")
# booleano = bool(True)

# # 2.2
# numero_str = "10"
# numero_conv = int(numero_str)
# numero_suma = numero_conv + 5

# # 2.3
# entrada_text =  input("igresa un numero flotante  :")
# numero_flotante = float(entrada_text)
# print(numero_flotante*2)

# # 2.4
# def cadena_a_flotante (cadena):
#     try:
#         float(cadena)
#         return (True)
#     except ValueError:
#         return (False)
    
# print(cadena_a_flotante(2.9928282))

# # exercise 3
# base = input("Ingresa la base: ")
# altura = input("Ingresa la Altura: ")
# print(f"El area es {base*altura}")

# # 3.2
# price = int(input("Ingresa el precio del producto: "))
# porcentary = int(input("Ingresa el el descuento del producto: "))
# print(f"El producto del descuento es: ${price-((porcentary * price)/100)}")

# 3.3
# num1 = int(input("ingresa un numero: "))
# num2 = int(input("ingresa un numero: "))
# result = (num1 % num2)
# print (f"El resultado es: {result}")

# 3.4
# num = int(input("ingresa un numero: "))
# print(f"el resultado de una de la pontencia por el mismo numero y sumar y dividir es: {(num**num)+num//num}")

# exercise 4
# num1 = int(input("ingresa un numero: "))
# num2 = int(input("ingresa un numero: "))
# if num1 == num2 :
#     print("Los numeros son iguales")
# else:
#     if num1>num2 :
#         print(f"El numero {num1} es mayor")
#     else:
#         print(f"El numero {num2} es mayor")
        
# 4.2
# age = int(input(f"Ingresa tu edad: "))
# if age >= 18 :
#     print(f"Eres mayor de edad")
# else:
#     print("eres menor de edad")

# 4.3
# tex1 = str(input("ingresa texto 1: "))
# tex2 = str(input("ingresa texto 2: "))
# if tex1 == tex2 :
#     print("las dos cadenas de texto son iguales")
# else:
#     print("La dos cadenas de texto son diferentes")

# exercise 5
# age = int(input("Ingresa tu edad: "))
# license = str(input("¿Tienes licencia de conducir?: "))

# if age>=18 and license=="si":
#     print("Puedes conducir")
# else:
#     print("Lo siento, no puedes conducir")

# 5.2
# title = str(input("¿Tienes titulo profecional?  si/no  :"))
# experience = str(input("¿Tienes experiencia laboral? si/no  :"))

# if title or experience == "si":
#     print("Puedes postularte al puesto de trabajo")
#  else:
#      print("Lo siento, no puedes conducir")


# 5.3
# num = int(input("Ingresa un numero: "))
# if num >10 and num <50:
#     print("Esta en el rango, pasas")
# else:
#     print("No esta en el rango no pasas")



    