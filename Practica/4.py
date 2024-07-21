import jwt

# Clave secreta
secret_key = "Con KeepCoding aprendemos"

# JWT original
jwt_original = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE"

# JWT modificado por el hacker
jwt_hacker = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"

try:
    # Decodificar y validar el JWT original
    payload_original = jwt.decode(jwt_original, secret_key, algorithms=["HS256"])
    print("JWT original es válido.")
    print("Payload:", payload_original)
except jwt.InvalidTokenError as e:
    print("JWT original no es válido:", str(e))

try:
    # Decodificar y validar el JWT del hacker
    payload_hacker = jwt.decode(jwt_hacker, secret_key, algorithms=["HS256"])
    print("JWT del hacker es válido.")
    print("Payload:", payload_hacker)
except jwt.InvalidTokenError as e:
    print("JWT del hacker no es válido:", str(e))
