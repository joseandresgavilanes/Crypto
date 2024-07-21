from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import binascii

# Leer la clave privada desde el archivo
with open('clave-rsa-oaep-priv.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Leer la clave pública desde el archivo
with open('clave-rsa-oaep-publ.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Texto cifrado proporcionado
ciphertext_hex = (
    "b72e6fd48155f565dd2684df3ffa8746d649b11f0ed4637fc4c99d18283b32e1"
    "709b30c96b4a8a20d5dbc639e9d83a53681e6d96f76a0e4c279f0dffa76a329d"
    "04e3d3d4ad629793eb00cc76d10fc00475eb76bfbc1273303882609957c4c0ae"
    "2c4f5ba670a4126f2f14a9f4b6f41aa2edba01b4bd586624659fca82f5b49701"
    "86502de8624071be78ccef573d896b8eac86f5d43ca7b10b59be4acf8f8e0498"
    "a455da04f67d3f98b4cd907f27639f4b1df3c50e05d5bf63768088226e2a9177"
    "485c54f72407fdf358fe64479677d8296ad38c6f177ea7cb74927651cf24b01d"
    "ee27895d4f05fb5c161957845cd1b5848ed64ed3b03722b21a526a6e447cb8ee"
)

# Convertir el texto cifrado de hexadecimal a bytes
ciphertext = binascii.unhexlify(ciphertext_hex)

# Descifrar el texto cifrado con la clave privada
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

try:
    print("Texto descifrado:", plaintext.decode('utf-8'))
except UnicodeDecodeError:
    print("El contenido descifrado no es texto UTF-8. Imprimiendo en formato hexadecimal.")
    print(binascii.hexlify(plaintext).decode('utf-8'))

# Cifrar la clave simétrica nuevamente con la clave pública
new_ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Convertir el nuevo texto cifrado a hexadecimal para mostrarlo
new_ciphertext_hex = binascii.hexlify(new_ciphertext).decode('utf-8')
print("Nuevo cifrado:", new_ciphertext_hex)

