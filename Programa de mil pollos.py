Nombre:input("Ingrese su Nombre: ")
edad=int(input("Ingrese su edad: "))
cdp=int(input("Cantidad de pollos a comprar: "))
precio=12
Iva=0.16
D1=0.12
D2=0.05
D3=0.10
D4=0.02
pd1=precio-(precio*D1)
pd2=precio-(precio*D2)
pd3=precio-(precio*D3)
pd4=precio-(precio*D4)
pdt1=pd2*cdp
pdt2=pd2*cdp
pdt3=pd3*cdp
pdt4=pd4*cdp
if edad>=65 and cdp>=5 or cdp<=10:
    print(f"Precio total a pagar es de {pdt1+Iva}$")
elif edad>=18 and cdp>=10:
    print(f"precio total a pagar es de {pdt2+Iva}$") 
elif edad>=18 and cdp>=20:
    print(f"precio total a pagar es de {pdt3+Iva}$")
else:
    print(f"presio total a pagar es de {pdt4+Iva}$")
print(f"gracias por su compra ")             