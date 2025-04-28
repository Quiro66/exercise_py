nota = int(input("ingrese la nota: "))
if nota >= 0 and nota <= 100:
    if nota >= 60:
        print("Aprobado")
    else:
        print("Desaprobado")