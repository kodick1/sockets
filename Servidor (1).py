#Servidor
from socket import *
global exit
exit=True
def conexion():
    print("Servidor")
    host = input("Digite ip del Host: ")
    port = int(input("Digite Puerto: "))
    return host,port

def crearsocket():
    conex = socket(AF_INET, SOCK_STREAM)
    return conex

def conectar(conex,host,port):
    while True:
        try:
            conex.bind((host, port))
            break
        except error as e:
            print("Error:",e)
    conex.listen(1)
    conexion, addr = conex.accept()
    print ("nueva conexion establecida!")
    print (addr)
    return conexion



conex = crearsocket()  
host,port = conexion()
conexion = conectar(conex,host,port)
mensaje =("Bienvenido al servidor")
conexion.send(mensaje.encode("UTF-8"))
while exit==True:
    peticion = conexion.recv(2048)
    lpeticion= peticion.decode("UTF-8")
    if lpeticion=="cliente: cerrar":
        print("el cliente se salio")
        exit=False
    else:        
        print (lpeticion)
        mensaje =("Servidor: "+ input("Escribir mensaje: "))
        conexion.send(mensaje.encode("UTF-8"))

conexion.close()
print ("conexion cerrada")
