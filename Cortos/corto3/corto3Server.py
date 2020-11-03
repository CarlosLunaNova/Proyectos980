import socket
import binascii
import os 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #CFLN - Crear el socket TCP

IP_ADDR = 'localhost'  #CFLN - Se levanta el server en la direccion de host local
IP_ADDR_ALL = ''       #CFLN - Se habilitan todas las interfaces
IP_PORT = 9800         #CFLN - Los clientes deben conectarse especificamente a este puerto
SERVER_QUEUE = 10      #CFLN - Indica la cantidad de conexiones en cola

BUFFER_SIZE = 64 * 1024 #CFLN - Tamaño de buffer de 64 KB

 #CFLN - Para recibir en todas las interfaces y levantar el sever con
 #       la configuracion especificada
serverAddress = (IP_ADDR_ALL, IP_PORT) 
print('Iniciando servidor en localhost{}, puerto {}'.format(*serverAddress))
sock.bind(serverAddress) 
sock.listen(SERVER_QUEUE) 

while True:
    print('Esperando conexion remota del cliente')
    connection, clientAddress = sock.accept()
    try:
        print('Conexion establecida con el cliente: ', clientAddress)   #CFLN - Indica la direccion
                                                                        #       del cliente
        while True:
            data = connection.recv(BUFFER_SIZE)
            #confirmar = 0xCC
            if(data==binascii.unhexlify("01")):
                #CFLN - Mensaje de confirmacion
                print('Instruccion recibida 0x01') #CFLN - Se inicia la grabacion de audio en server
                os.system('arecord -d 8 -f U8 -r 8000 201602491_server.wav')
               
            elif(data==binascii.unhexlify("02")):
                #CFLN - Mensaje de confrmacion
                print('Instruccion recibida 0x02')               
                with open('201602491_server.wav', 'rb') as f: #CFLN - Se abre el archivo a enviar en BINARIO
                    connection.sendfile(f, 0)
                    f.close()

            elif(data==binascii.unhexlify("03")):
                #CFLN - Comando para cerrar socket
                print('Transmision finalizada desde el cliente ', clientAddress)
                break                   
    
    except KeyboardInterrupt:
        print('Forzando cierre del servidor por administrador')
        sock.close()

    finally:
        connection.close()