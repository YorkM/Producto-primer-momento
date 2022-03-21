
from operator import index


print("Supermercado el Wilmar y el York")
print("**********************")
print("0. Digita 0 para salir")
print("1. Digita 1 para registrar producto #")
print("2. Digita 2 para ver los productos de la lista")
print("3. Digita 3 para buscar y editar un precio")
print("4. Digita 4 para buscar y eliminar producto")


print("**********************")

opcion = 1
productos = []
producto = {}

while(opcion != 0):
    opcion = int(input("Digita una opcion: "))

    if(opcion == 0):
        break
    elif(opcion == 1):
       producto['codigo'] = input("Digite el codigo del producto: ")
       producto['nombre'] = input("Digite el Nombre del producto: ")
       producto['precio'] = int(input("Digite el Precio del producto: "))
       productos.append(producto)
       producto = {}
    elif(opcion == 2):
        print(f"La cantidad de productos es: {len(productos)}")
        print(productos)
    elif(opcion == 3):
        buscar = input("Ingrese el codigo del producto que busca: ")
        for producto in productos:
            if(buscar == producto['codigo']):
               precioEditar = producto['precio']
               print(producto)
               producto['precio'] = int(input(f"Digite el nuevo Precio del producto: "))
               print(f"El nuevo precio es {producto['precio']}")
               break
        else:
            print("El producto no existe")
                
    
    elif(opcion == 4):
        eliminarProducto = input("Ingrese el codigo del producto que desea eliminar de la lista: ")
        index=-1
        for producto in productos:
            index+=1
            if(eliminarProducto == producto['codigo']): 
               print(producto)             
               del productos[index]
               print("Producto eliminado correctamente")
               break
        else:
            print("El producto no existe")
    
    
    else:
        print("La opción ingresada no está disponible")
                   
               
                 
  

