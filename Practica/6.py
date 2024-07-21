import hmac
import hashlib

# Clave en hexadecimal
hex_key = "A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB"
# Convertir la clave a bytes
key = bytes.fromhex(hex_key)

# Texto para el que queremos calcular el HMAC-SHA256
text = "Siempre existe más de una forma de hacerlo, y más de una solución válida."
# Convertir el texto a bytes
message = text.encode()

# Crear el objeto HMAC con la clave y el hash SHA256
hmac_obj = hmac.new(key, message, hashlib.sha256)

# Obtener el resultado del HMAC en hexadecimal
hmac_result = hmac_obj.hexdigest()

print(hmac_result)
