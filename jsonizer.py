import jwt

print(jwt.decode("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ4dXkiOiJqb3BhIn0.8YRf7fgWoXvYdLnQDsPsF92N80eR8iI9ydMNfUSn-oA", options={"verify_signature": False}))
# private_key = b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
# public_key = b"-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEAC..."
# encoded = jwt.encode({"xuy": "jopa"}, private_key)

# print(encoded)
