from Crypto.Util.number import getPrime
import hashlib

# Fonction pour générer une paire de clés RSA
def generer_paire_cles_rsa(bits):
    p = getPrime(bits // 2)
    q = getPrime(bits // 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi_n)
    cle_publique = (e, n)
    cle_privee = (d, n)
    return cle_publique, cle_privee
#print(generer_paire_cles_rsa(2048))

cle_publique, cle_privee = generer_paire_cles_rsa(2048)

# Fonction pour chiffrer un message avec une clé publique RSA
def rsa_chiffrer(message, cle_publique):
    e, n = cle_publique
    msg_bytes = message.encode('utf-8')
    msg_int = int.from_bytes(msg_bytes, 'big')
    ciphertext = pow(msg_int, e, n)
    return ciphertext

message_chiffre = rsa_chiffrer('Salut', cle_publique)
print("Message chiffré:", message_chiffre)

# Fonction pour déchiffrer un message chiffré avec une clé privée RSA
def rsa_dechiffrer(ciphertext, cle_privee):
    d, n = cle_privee
    decrypted_int = pow(ciphertext, d, n)
    decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big')
    return decrypted_bytes.decode('utf-8')

message_dechiffre = rsa_dechiffrer(message_chiffre, cle_privee)
print("Message déchiffré:", message_dechiffre)

def h(message):
    hash_obj = hashlib.sha256(str(message).encode('utf-8')).hexdigest()
    return int(hash_obj, 16) 


print(h(14))

def rsa_sign(message, private_key):
    c = h(message)
    signature = pow(c, private_key, cle_privee[1])
    return (c, signature)

def rsa_verify(message, signature, public_key):
    c, signed_c = signature
    if pow(c, public_key, cle_publique[1]) == c:
        return True
    else:
        return False


# Bob signe un message et envoie à Alice
message_bob = "Bonjour Alice, c'est Bob."
signature_bob = rsa_sign(message_bob, cle_privee[0])

# Alice reçoit le message de Bob et vérifie la signature
message_recu = message_bob
signature_recu = signature_bob
if rsa_verify(message_recu, signature_recu, cle_publique[0]):
    print("Message de Bob vérifié :", message_recu)
else:
    print("Signature non valide. Le message pourrait avoir été altéré.")






