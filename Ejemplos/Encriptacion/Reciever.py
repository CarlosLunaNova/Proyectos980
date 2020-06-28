from Sender import *

salt = encriptado[0:SALT_SIZE]
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=IV_SIZE + KEY_SIZE)

iv = derived[0:IV_SIZE]
key = derived[IV_SIZE:]

desencriptado = AES.new(key, AES.MODE_CFB, iv).decrypt(encriptado[SALT_SIZE:])

print(desencriptado)
print("\n")