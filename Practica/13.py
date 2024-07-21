from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Leer la clave privada RSA desde el archivo
with open('clave-rsa-oaep-priv.pem', 'r') as priv_file:
    private_key_rsa = RSA.import_key(priv_file.read())

# Crear el hash del mensaje
message = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
hash = SHA256.new(message.encode('utf-8'))

# Calcular la firma
signature_rsa = pkcs1_15.new(private_key_rsa).sign(hash)
signature_rsa_hex = signature_rsa.hex()

print(f"Firma RSA (hexadecimal): {signature_rsa_hex}")
