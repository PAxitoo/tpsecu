sbox = [3, 14, 1, 10, 4, 9, 5, 6, 8, 11, 15, 2, 13, 12, 0, 7]
xobs = [14, 2, 11, 0, 4, 6, 7, 15, 8, 5, 3, 9, 13, 12, 1, 10]

import random

def round(msg, subkey):
    return sbox[(msg ^ subkey) % 16]

def round_inv(msg, subkey):
    return xobs[(msg ^ subkey) % 16]

def enc(msg, key):
    t0 = round(msg, key[0])
    t1 = round(t0, key[1])
    return t1


def simplified_enc(msg, key):
    t0 = round(msg, key[0])
    return t0 ^ key[1]

p = 11 #msg clair

key = (5, 10)

chiffrer = simplified_enc(p, key)

print("Message clair :", p)
print("Clé secrète :", key)
print("Message chiffré :", chiffrer)

def brute_force(p, c):
    for k1 in range(16):
        for k2 in range(16):
            c_key = (k1, k2)
            if enc(p, c_key) == c:
                return c_key
    return None


p = 11 #msg clair
c = 10 #msg chiffré

key = brute_force(p, c)
if key is not None:
    print(f"La clé secrète est {key}")
else:
    print("Aucune clé n'a été trouvée")




