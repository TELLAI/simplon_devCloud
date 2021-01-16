import logging
import random

# Recuperer la liste de mots
with open("mots.txt", "r") as fichier:
    liste_m = fichier.read().split()

# Choisir un mot avec random
mot_l = random.sample(liste_m, 1)
print(mot_l)
mot = mot_l[0]
len_mot = len(mot)
l_mot = list(mot)

# Démarrer un compteur pour les vies
count_vie = 5
count_mot = len_mot
jeu_fini = False
mot_recherche = []
mot_recherche = len_mot * "*"
trou_let = {}

print(mot_recherche)

def trouver_lettre(lettre):
    lettre_trouve = False
    trou_let[lettre_trouve] = mot_recherche
    for i in range(0, (len_mot + 1)):
        if l_mot[i] == lettre:
            mot_recherche[i] = l_mot[i]
            count_mot -= 1
            lettre_trouve = True
    return trou_let


while((jeu_fini != True) or (count_vie > 0)):
    lettre = input("veuillez proposer une lettre: ")
    res = {}
    res = trouver_lettre(lettre)
    if res.keys() is False:
        count_vie -= 1
    else:
        print(res.value())









