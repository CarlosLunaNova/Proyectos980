import socket

SERVER_IP   = '192.168.1.4'
SERVER_PORT = 9800
BUFFER_SIZE = 1024

# Se crea socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se conecta al puerto donde el servidor se encuentra a la escucha
server_address = (SERVER_IP, SERVER_PORT)
print('Conectando a {} en el puerto {}'.format(*server_address))
sock.connect(server_address)

while True:
    try:

        # Se envia un texto codificado EN BINARIO
        message = input('\nIngrese su mensaje: ').encode()
        print('\nEnviando el siguiente texto:  {!s}'.format(message))
        sock.sendall(message) #Se envia utilizando "socket.sendall" 
        print("\n")

    finally:
        print('\nMensaje enviado al server')
        #print('\n\nConexion finalizada con el servidor')
        #sock.close()

"""
# Esperamos la respuesta del ping servidor
bytesRecibidos = 0
bytesEsperados = len(message)

#TCP envia por bloques de BUFFER_SIZE bytes
while bytesRecibidos < bytesEsperados:
    data = sock.recv(BUFFER_SIZE)
    bytesRecibidos += len(data)
    print('\nRecibido: {!s}'.format(data))

"""
