## Ejercicios Prácticos de Python 3

# 3.1
# Calcula el área de un rectángulo a partir de base y altura ingresadas por el usuario.
base = input("Ingresa la base: ")
altura = input("Ingresa la Altura: ")
print(f"El area es {base*altura}")

# 3.2
# Dado un precio y un porcentaje de descuento, muestra el valor final a pagar.
price = int(input("Ingresa el precio del producto: "))
porcentary = int(input("Ingresa el el descuento del producto: "))
print(f"El producto del descuento es: ${price-((porcentary * price)/100)}")

# 3.3
# Calcula el residuo de dividir dos números dados por el usuario.
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))
result = (num1 % num2)
print (f"El resultado es: {result}")

# 3.4
# Escribe una fórmula que use al menos tres operadores diferentes y muestre el resultado.
num = int(input("ingresa un numero: "))
print(f"el resultado de una de la pontencia por el mismo numero y sumar y dividir es: {(num**num)+num//num}")