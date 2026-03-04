p1, p2, p3 = float(input("Ingrese el valor del primer producto: ")), float(input("Ingrese el valor del segundo producto: ")), float(input("Ingrese el valor del tercer producto: "))
if p1 <= p2 and p1 <= p3:
    min = p1
elif  p2 <=p2 <= p1 and p3:
    min = p2
else:
    min = p3
D = min / 2
total = p1 + p2 + p3 - D
print(f"El total de la compra es: {total}")