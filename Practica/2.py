from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Datos proporcionados
key_hex = 'A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72'
cipher_text_b64 = 'TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4US t3aB/i50nvvJbBiG+le1ZhpR84oI='
iv_hex = '00000000000000000000000000000000'  # iv de ceros binarios

# Decodificar los datos
key = bytes.fromhex(key_hex)
iv = bytes.fromhex(iv_hex)
cipher_text = base64.b64decode(cipher_text_b64.replace(' ', ''))

# Configurar el descifrador
cipher = AES.new(key, AES.MODE_CBC, iv)

# Descifrar el texto cifrado con PKCS7
try:
    plain_text_pkcs7 = unpad(cipher.decrypt(cipher_text), AES.block_size, style='pkcs7')
    print("Texto descifrado con PKCS7:", plain_text_pkcs7.decode('utf-8'))
except (ValueError, UnicodeDecodeError) as e:
    print(f"Error descifrando con PKCS7: {e}")

# Descifrar el texto cifrado con x923 padding
try:
    plain_text_x923 = unpad(cipher.decrypt(cipher_text), AES.block_size, style='x923')
    try:
        print("Texto descifrado con x923:", plain_text_x923.decode('utf-8'))
    except UnicodeDecodeError as e:
        print("Texto descifrado con x923 (bytes):", plain_text_x923)
        print(f"Error decodificando con x923: {e}")
except ValueError as e:
    print(f"Error descifrando con x923: {e}")

# Verificar el padding añadido en PKCS7
padding_len_pkcs7 = AES.block_size - (len(plain_text_pkcs7) % AES.block_size)
print(f"Padding añadido (PKCS7): {padding_len_pkcs7} bytes")
