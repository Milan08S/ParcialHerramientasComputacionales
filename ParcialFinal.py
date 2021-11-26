##
## Jose Daniel Ramirez Delgado - 8968586
## Miguel Angel Sanchez
##
## Desarrollo Parcial Final Herramientas

def descuentosCafeteria(d):
    cedula = int(input("Digita tu cedula: "))
    rol = input("Estudiante o Profesor: ")
    print(d)
    producto = int(input("Digite codigo de producto: "))
    cantidad = int(input("Digite cantidad: "))
    total = d[producto][1] * cantidad
    if rol == 'Profesor':
        total = total * 0.8
    if rol == 'Estudiante':
        total = total * 0.5
        print("El " + str(rol) + " con Cedula " + str(cedula) + " debe pagar " + str(total) + " por el producto " + str(producto))

d = {23:["Gaseosa", 3000], 45:["Cheetos", 2200]}
descuentosCafeteria(d)    
