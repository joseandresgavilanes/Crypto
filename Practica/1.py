# Parte 1
clave_fija_hex = "B1EF2ACFE2BAEEFF"
clave_final_hex = "91BA13BA21AABB12"

clave_fija_bin = bin(int(clave_fija_hex, 16))[2:].zfill(128)
clave_final_bin = bin(int(clave_final_hex, 16))[2:].zfill(128)

clave_properties_bin = ''.join(str(int(a) ^ int(b)) for a, b in zip(clave_fija_bin, clave_final_bin))
clave_properties_hex = hex(int(clave_properties_bin, 2))[2:].upper().zfill(16)

print("Parte 1: Clave en properties para desarrollo:", clave_properties_hex)

# Parte 2
parte_dinamica_hex = "B98A15BA31AEBB3F"

parte_dinamica_bin = bin(int(parte_dinamica_hex, 16))[2:].zfill(128)

clave_memoria_bin = ''.join(str(int(a) ^ int(b)) for a, b in zip(clave_fija_bin, parte_dinamica_bin))
clave_memoria_hex = hex(int(clave_memoria_bin, 2))[2:].upper().zfill(16)

print("Parte 2: Clave en memoria en producción:", clave_memoria_hex)
