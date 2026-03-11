N = int(input("ingresar numero entero para verificar si es par o impar: "))
R = N % 2
if R == 0:
    print(f"{N} es un numero par")
else: print(f"{N} es un numero impar")