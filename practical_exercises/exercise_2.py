## Ejercicios Prácticos de Python 2

# 2.1
# Declara una variable de cada tipo básico: entero, flotante, cadena y booleano.
entero = int(10)
flotante = float(3.1415)
cadena = str("esto esta cabronn")
booleano = bool(True)

# 2.2
# Convierte una cadena con valor numérico a entero y realiza una suma con otro número.
numero_str = "10"
numero_conv = int(numero_str)
numero_suma = numero_conv + 5
print(f"El resultado de la suma es: {numero_suma}")

# 2.3
# Convierte una entrada de texto a número flotante, multiplícala por 2 y muestra el resultado.
entrada_text =  input("igresa un numero flotante  :")
numero_flotante = float(entrada_text)
print(numero_flotante*2)

# 2.4
# Escribe una función que reciba un string y devuelva True si puede convertirse a número y False si no.

num = input("ingresa un algo:  ")

def es_numero(num):
    try:
        int(num)
        print("Puede convertirse a número")
        return True
    except ValueError:
        print("No se puede convertirse a número")
        return False

resultado = es_numero(num)
print(f"Resultado: {resultado}")