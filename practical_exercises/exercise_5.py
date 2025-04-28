## Ejercicios Prácticos de Python 5

# 5.1
# Pide al usuario su edad y si tiene licencia de conducción. Solo si ambas condiciones se cumplen, imprime que puede conducir.
age = int(input("Ingresa tu edad: "))
license = str(input("¿Tienes licencia de conducir?: "))

if age>=18 and license=="si":
    print("Puedes conducir")
else:
    print("Lo siento, no puedes conducir")

# 5.2
# Solicita si una persona tiene experiencia laboral y título universitario. Usa operadores lógicos para decidir si puede aplicar a una oferta de trabajo.
title = str(input("¿Tienes titulo profecional?  si/no  :"))
experience = str(input("¿Tienes experiencia laboral? si/no  :"))

if title or experience == "si":
    print("Puedes postularte al puesto de trabajo")
else:
     print("Lo siento, no puedes conducir")


# 5.3
# Dado un número, determina si está en el rango de 10 a 50 (inclusive).
num = int(input("Ingresa un numero: "))
if num >10 and num <50:
    print("Esta en el rango, pasas")
else:
    print("No esta en el rango no pasas")