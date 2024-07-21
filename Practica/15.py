from Crypto.Cipher import DES3
from binascii import unhexlify

# Clave de transporte
key_transport = unhexlify("A1A10101010101010101010101010102")

# Clave protegida (en formato hexadecimal)
wrapped_key = unhexlify("42766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B")

# Crear el objeto de desencriptación (unwrap) de la clave usando 3DES
cipher = DES3.new(key_transport, DES3.MODE_ECB)

# Desencriptar la clave (unwrap)
unwrapped_key = cipher.decrypt(wrapped_key)

# Mostrar la clave desencriptada
print("Clave desencriptada:", unwrapped_key.hex())
