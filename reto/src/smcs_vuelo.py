def Cons_C(D,V, H):
     CP, VC, DC = 5400, 900, 0.785
     VT = VC + V
     if VT <= 185:
      return(print(f"entrando en stall,\n abortando ruta en hora: {H},\n buscar aeropuerto mas cercano..."))
     T = D / VT
     Cons_T = CP * T * DC
     return(print(f" el consumo de Jet A-1 fue de: {Cons_T:0.2f} kg"))

CI, H = float(input("ingrese cantidad de combustible en kilogramos")), int(input("ingrese la cantidad de horas de vuelo presupuestas para el vuelo: "))
i = 1
while i <= H:
    D = float(input("ingrese la distancia en km: "))
    V = float(input("Ingrese la velocidad del viento, si el viento es a favor es postivo y si es en contra negativo: "))
    Cons_C(D,V, H)