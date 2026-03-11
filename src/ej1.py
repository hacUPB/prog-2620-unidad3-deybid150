NC = float(input("ingrese el nivel de combustible en L: "))
GC = 125
Tm = NC * 0.2
i = 0
while NC > Tm:
    i += 1
    NC = NC - GC
    if NC < GC:
        print("Alerta: consumo anomalo")
print((2*i), "horas de vuelo")