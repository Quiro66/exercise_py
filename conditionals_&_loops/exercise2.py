#Le decimos al usuario que ingrese la nota
nota = int(input("Ingrese la nota: "))
#creamos un condicional para determinar si es el numero esta aprobado o desaprobado
if nota >= 0 and nota <= 100:
    if nota >= 60:
        print("Aprobado")
    else:
        print("Desaprobado")