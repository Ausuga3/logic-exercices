
def registrar_cliente():
    while True:
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
        return cliente
        
def comprar_producto(productos,cliente):
    
    producto=input("Que deseas comprar?: ")
    if producto in productos and productos[producto]["stock"] > 0:
        if cliente["dinero"] >= productos[producto]["valor"]:
            cliente["dinero"] -= productos[producto]["valor"]
            productos[producto]["stock"] -= 1



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
            print(productos,clientes)
            
        elif opc ==3:
            pass
        elif opc == 4:
            print("Vuela pronto!")
            break    

