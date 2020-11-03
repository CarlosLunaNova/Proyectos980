import socket
import binascii
import os

SERVER_IP   = 'localhost'   #CFLN - Se conecta al server en el localhost
SERVER_PORT = 9800          #CFLN - Puerto al cual hay que conectarse
BUFFER_SIZE = 64 * 1024     #CFLN - Tamaño del buffer para la transferencia

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CFLN - Se conecta al puerto del servidor
server_address = (SERVER_IP, SERVER_PORT)
print('Conectando a localhost{} en el puerto {}'.format(*server_address))
sock.connect(server_address)

try:
    while True:
        #CLFN - Se envia una instruccion en hexadecimal
        instruccion = input("Instruccion para el server : ")
        instruccionBytes = instruccion.encode()
        sock.sendall(binascii.unhexlify(instruccionBytes)) #CFLN - Se envia una instruccion al server 

        print("\n\n")
        
        if instruccion=='02':
            buff = sock.recv(BUFFER_SIZE)
            archivo = open('201602491_client.wav', 'wb') 
            while buff:
                buff = sock.recv(BUFFER_SIZE) 
                archivo.write(buff.decode())
            archivo.close() #CFLN - Se cierra el archivo
            os.system('aplay 201602491_client.wav')
            

        if(instruccion=='03'):
            break

except KeyboardInterrupt:
        print('Forzando cierre del cliente por administrador')
        sock.close()

finally:
    print('\n\nConexion finalizada con el servidor')
    sock.close()