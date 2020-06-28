import hashlib
import math
import os

from Crypto.Cipher import AES

IV_SIZE = 16 # 128 bit
KEY_SIZE = 32 # 256 bit
SALT_SIZE = 16 # Tamaño arbitrario

mensaje = "HOla este es el mensaje"

cleartext = mensaje.encode()
print(cleartext)
print("\n")
password = b'contrasenia altamente segura'
salt = os.urandom(SALT_SIZE)
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=IV_SIZE+KEY_SIZE)

iv = derived[0:IV_SIZE]
key = derived[IV_SIZE:]

encriptado = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext)
print(encriptado)
print("\n")


