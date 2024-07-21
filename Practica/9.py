import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Clave AES proporcionada
clave_aes = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

# Calcular SHA-256 de la clave
hash_sha256 = hashlib.sha256(clave_aes).digest()

# Obtener los 3 primeros bytes del SHA-256
kcv_sha256 = hash_sha256[:3]

text_block = bytes(16)

iv = bytes(16)

# Crear el cifrador AES en modo CBC con la clave y IV
cipher = AES.new(clave_aes, AES.MODE_CBC, iv)

# Cifrar el bloque de texto
ciphertext = cipher.encrypt(pad(text_block, AES.block_size))

# Obtener los 3 primeros bytes del ciphertext
kcv_aes = ciphertext[:3]

print(kcv_sha256.hex(), kcv_aes.hex())

