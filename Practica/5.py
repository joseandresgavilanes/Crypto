import hashlib

# Texto dado
texto = "En KeepCoding aprendemos cómo protegernos con criptografía."

# Generar SHA3-256
hash_sha3_256 = hashlib.sha3_256(texto.encode()).hexdigest()
print(hash_sha3_256)