from cryptography.hazmat.primitives.ciphers import aead
import base64

# Clave proporcionada en hexadecimal
key_hex = "AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120"

# Convertir la clave hexadecimal a bytes
key = bytes.fromhex(key_hex)

# Nonce proporcionado en base64
nonce_base64 = "9Yccn/f5nJJhAt2S"

# Convertir el nonce de base64 a bytes
nonce = base64.b64decode(nonce_base64)

# Texto a cifrar
data = "KeepCoding te enseña a codificar y a cifrar".encode('utf-8')

# Crear el cifrador ChaCha20-Poly1305
cipher = aead.ChaCha20Poly1305(key)

# Cifrar el texto
ciphertext = cipher.encrypt(nonce, data, None)

# Convertir el texto cifrado a hexadecimal para su almacenamiento o visualización
ciphertext_hex = ciphertext.hex()
print(f"Cifrado (hex): {ciphertext_hex}")

# Desencriptar el texto
decrypted_data = cipher.decrypt(nonce, ciphertext, None)

# Mostrar el texto descifrado
print(f"Texto descifrado: {decrypted_data.decode('utf-8')}")
