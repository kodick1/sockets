#Cliente
from socket import *
import sys
global exit
exit = True
def conectar(conex,host,port):
    conex.connect( (host, port) )
    print("Conectado al Servidor")

def crearsocket():
    conex = socket(AF_INET, SOCK_STREAM)
    return conex

def conexion():
    print ("Cliente")
    host = input("Digite ip del Host: ")
    port = int(input("Digite Puerto: "))
    return host,port

misocket = crearsocket()
host,port = conexion()
conectar(misocket,host,port)
respuesta = misocket.recv(2048)
lrespuesta =respuesta.decode("UTF-8")
print (lrespuesta)
while exit==True:       
    mensaje =("cliente: "+ input("Enviar mensaje : "))
    misocket.send(mensaje.encode("UTF-8"))  
    if mensaje=="cliente: cerrar":
        misocket.close        
        exit=False
    else: 
        respuesta = misocket.recv(2048)
        lrespuesta =respuesta.decode("UTF-8")
        print (lrespuesta)

misocket.close()
print("conexion cerrada")
