num = int(input("Ingrese el número de acl "))
if num >= 1 and num <=99:
    print("El número ingresado corresponde a una ACL IPv4 estándar")
elif num >=100 and num<=199:
    print("El número ingresado corresponde a una ACL IPv4 extendida")
else:
    print("El número ingresado no corresponde a ninguna ACL")