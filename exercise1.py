
def registrar_cliente():
    id= -1
    while True:
        id=id+1
        print("---Registrarse!!---")
        nombre = input("Ingrese su nombre: ")
        apellido = input("ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        if edad < 18:
            print("Solo mayores de edad pueden comprar!")
            break
        dinero = int(input("Cuanto dinero tienes?: "))
        cliente={"nombre":nombre,
                "apellido":apellido,
                "edad":edad,
                "dinero":dinero}
        print(f"tu ID es: {id}")
        return cliente
        
def comprar_producto(productos,cliente):
    id_cliente=int(input(" cual es tu id?: "))
    producto=input("Que deseas comprar?: ")
    if producto in productos and productos[producto]["stock"] > 0:
        if cliente[id_cliente]["dinero"] >= productos[producto]["valor"]:
            cliente[id_cliente]["dinero"] -= productos[producto]["valor"]
            productos[producto]["stock"] -= 1
            print(productos,clientes)
        else:
            print("No tienes suficiente dinero!")    
    else:
        print("No existe este producto")


def devolver_prodcuto():
    pass

def mostrar_estado_tienda():
    pass

def mostrar_estado_cliente():
    pass
        

productos ={ 
    "camisa":{"valor":5000,"stock":10,"defectuoso":0},
    "pantalon":{"valor":7000,"stock":5,"defectuoso":0},
    "traje":{"valor":10000,"stock":82,"defectuoso":0}
    }
    
if __name__ == "__main__":
    clientes=[] 

    while True:
        opc = int(input("""Que deseas hacer:
                        1.registrarse
                        2.comprar
                        3.devolver producto
                        4.salir
                        : """))  
        if opc == 1:
            clientes.append(registrar_cliente() )    
            print(clientes)
        elif opc == 2:
            comprar_producto(productos,clientes)
            
            
        elif opc ==3:
            pass
        elif opc == 4:
            print("Vuela pronto!")
            break    

