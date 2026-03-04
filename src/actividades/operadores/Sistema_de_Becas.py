P, NS = float(input("ingrese su promedio: ")), (input("Ingrese su estatus socioenconomico (1/2): "))
E = ((P >= 8.0) and (NS == "1")) or P >= 9.0
print(f"acceso a la beca: {E}")