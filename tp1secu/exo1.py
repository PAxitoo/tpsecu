boite_S = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
clef = [5, 11]

def tour(k, s):
    return boite_S[k ^ s]

def chiffre_byte(clef, octet):
    t1 = octet & 15
    t2 = octet >> 4
    temp = [t1, t2]
    resultat = 0
    for i in range(len(clef)):
        t = tour(clef[0], int(temp[i]))
        temp[i] = tour(clef[1], int(t))
    temp[0] = temp[0] << 4
    for i in range(len(temp)):
        resultat += temp[i]
    return resultat

def dechiffre_byte(clef, octet):
    t1 = octet & 15
    t2 = octet >> 4
    temp = [t1, t2]
    resultat = 0
    for i in range(len(clef)):
        t = tour_inverse(clef[1], int(temp[i]))
        temp[i] = tour_inverse(clef[0], int(t))
    temp[0] = temp[0] << 4
    for i in range(len(temp)):
        resultat += temp[i]
    return resultat

def tour_inverse(k, s):
    return boite_S.index(s) ^ k


def chiffre_fichier(nom_fichier):
    f0 = open('./' + nom_fichier, "rb")
    donnees = f0.read()
    liste_donnees = list(donnees)
    f0.close()

    f1 = open('./' + nom_fichier + '.enc', "wb")

    for i in range(len(liste_donnees)):
        liste_donnees[i] = chiffre_byte(clef, liste_donnees[i])
    f1.write(bytearray(liste_donnees))
    f1.close()

#chiffre_fichier('image.jpg')


def dechiffre_fichier(nom_fichier):
    f0 = open('./' + nom_fichier + '.enc', "rb")
    donnees = f0.read()
    liste_donnees = list(donnees)
    f0.close()

    f1 = open('./' + nom_fichier + '.dec', "wb")

    for i in range(len(liste_donnees)):
        liste_donnees[i] = dechiffre_byte(clef, liste_donnees[i])
    f1.write(bytearray(liste_donnees))
    f1.close()

octet = ord('Z')
octet_chiffre = chiffre_byte(clef, octet)
print("Octet Chiffré:", bin(octet_chiffre)[2:].zfill(8))

octet_dechiffre = dechiffre_byte(clef, octet_chiffre)
print("Octet Déchiffré:", chr(octet_dechiffre))

dechiffre_fichier("test.jpg")

key = (9,0)

chiffre_fichier('coucou.txt')
