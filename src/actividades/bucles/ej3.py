e = True
C = input("cree una nueva contraseña: ")
while e == True:
    P = input("Ingrese la contraseña: ")
    if C == P:
        print("Contraseña correcta, entrando... ")
        e = False
    else: print("contraseña incorrecta")