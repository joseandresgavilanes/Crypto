from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Datos iniciales
clave_maestra_hex = "E377152B3F1ACFA0148FB3A426DB72"
device_id_hex = "e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3"

# Convertir datos hexadecimales a bytes
clave_maestra = bytes.fromhex(clave_maestra_hex)
device_id = bytes.fromhex(device_id_hex)

# Usar HKDF para derivar una nueva clave
hkdf = HKDF(
    algorithm=hashes.SHA512(),
    length=32,  # 256 bits
    salt=None,
    info=device_id,
    backend=default_backend()
)

clave_aes = hkdf.derive(clave_maestra)

# Imprimir la clave AES en formato hexadecimal
print(f"Clave AES derivada: {clave_aes.hex()}")
