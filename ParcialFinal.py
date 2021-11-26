##
## Jose Daniel Ramirez Delgado - 8968586
## Miguel Angel Sanchez
##
## Desarrollo Parcial Final Herramientas

def descuentosCafeteria(d):
    ce = int(input("Digita tu cedula: "))
    rol = input("Estudiante o Profesor: ")
    print(d)
    res = int(input("Digite codigo de producto: "))
    ca = int(input("Digite cantidad: "))
    total = d[res][1] * ca
    if rol == 'Profesor':
        total = total * 0.8
    if rol == 'Estudiante':
        total = total * 0.5
        print("El " + str(rol) + " con Cedula " + str(ce) + " debe pagar " + str(total) + " por el producto " + str(res))
    else:
        print("No hay cantidad del producto")
d = {23:["Gaseosa", 3000], 45:["Cheetos", 2200]}
descuentosCafeteria(d)    
