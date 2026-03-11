E = int(input("ingrese su edad: "))
if E > 0:    
    if E < 6:
        R = "Infacia"
    elif E < 12:
        R = "NIÑEZ"
    elif E < 20:
        R = "Adolescencia"
    elif E < 25:
        R = "juventud"
    elif E < 60:
        R = "Adultez"
    else: R = "Ancianidad / Vejez"
    print(f"el rango de tu edad es: {R}")
else: print("Valor no valido, ingrese un valor positivo")