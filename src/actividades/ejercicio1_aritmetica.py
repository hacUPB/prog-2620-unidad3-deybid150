C,P, VPr = float(input("ingrese el valor de la cuenta: ")), int(input("ingrese el numero de personas asociadas a dicha cuenta: ")), int(input("ingrese la propina en porcentaje: "))
Pr = C * (VPr/100)
T = C + Pr
D = T/P
print (f"El precio total es: {T:.2f}$, a cada uno le corresponde: {D:.2f}$")
