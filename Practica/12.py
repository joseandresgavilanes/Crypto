from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import binascii

# Datos proporcionados
key_hex = 'E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74'
nonce_base64 = '9Yccn/f5nJJhAt2S'
plaintext = 'He descubierto el error y no volveré a hacerlo mal'

# Convertir clave de hexadecimal a bytes
key_bytes = binascii.unhexlify(key_hex)

# Convertir nonce de Base64 a bytes
nonce_bytes = base64.b64decode(nonce_base64)

# Convertir texto a bytes
plaintext_bytes = plaintext.encode()

# Crear el cifrador AES/GCM
cipher = Cipher(algorithms.AES(key_bytes), modes.GCM(nonce_bytes), backend=default_backend())
encryptor = cipher.encryptor()

# Cifrar el texto
ciphertext_bytes = encryptor.update(plaintext_bytes) + encryptor.finalize()

# Obtener el tag de autenticación
tag = encryptor.tag

# Convertir a formato hexadecimal y Base64
ciphertext_hex = binascii.hexlify(ciphertext_bytes).decode('utf-8')
ciphertext_base64 = base64.b64encode(ciphertext_bytes).decode('utf-8')
tag_hex = binascii.hexlify(tag).decode('utf-8')
tag_base64 = base64.b64encode(tag).decode('utf-8')

print("Texto en hexadecimal:", ciphertext_hex)
print("Texto en base64:", ciphertext_base64)
print("Tag hex:", tag_hex)
print("Tag base64:", tag_base64)

# Descifrar para verificar
cipher = Cipher(algorithms.AES(key_bytes), modes.GCM(nonce_bytes, tag), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_bytes = decryptor.update(ciphertext_bytes) + decryptor.finalize()

# Convertir bytes a texto
decrypted_text = decrypted_bytes.decode()
print("------------------------------------------Verificacion---------------------------------------------------")
print("Texto descifrado:", decrypted_text)

# Verificar longitud del nonce
print("Longitud del nonce en bytes:", len(nonce_bytes))
