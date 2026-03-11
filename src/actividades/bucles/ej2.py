N1, N2 = float(input("ingrese el numero inicial: ")), float(input("ingrese el numero final: "))
if N1 > N2:
    N, n = N1, N2
else: 
    n, N = N1, N2
while n <= N:
    if n % 2 == 0:
        print(n)
    n += 1