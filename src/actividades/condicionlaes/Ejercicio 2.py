E, C = 9000, float(input("por favor ingrese el costo de la compra: "))
if C < 100000:
    T = C + E
    print(f"el valor de su compra mas el envio es de {T}")
else: print(f"el envio es gratis por lo tanto su total es {C}")