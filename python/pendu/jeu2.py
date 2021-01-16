import random

import random

# variable globale:
# fonction récupere le mot

def fct_recup():
    with open("mots.txt", "r") as fichier:
        list_w = fichier.read().split()
    word_l = random.sample(list_w, 1)
    word = list(word_l[0])
    print(word)
    return (word)

# variable global
word = fct_recup()

# fonction print du mot vide
def fct_create(word):
    new_word = list(len(word) * "*")
    return (new_word)

# variable global
new_word = fct_create(word)

# fonction comparaison du mot avec la lettre
"""
def fct_compare():
    print(new_word)
    lettre = input("veuillez entrer une lettre: ")
    rep = False
    res = {}
    res[rep] = new_word
    for ii, i in enumerate(word):
        if i == lettre:
            new_word[ii] = word[ii]
            rep = True
    return (res)
print(fct_compare())


#variable global:
dict_log = {}
dict_log = fct_compare()"""

def fct_fill(new_word, lettre, index):
    new_word[index] = lettre
    return (new_word)

#fonction du jeu:
def fct_game():
    rep = False
    count_life = 5
    count_word = len(word)
    while(count_word > 0 and count_life > 0):
        print(new_word)
        lettre = input("veuillez entrer une lettre: ")
        for ii, i in enumerate(word):
            if i == lettre:
                fct_fill(new_word, lettre, ii)
                count_word -= 1
                rep = True
                print(count_life)
        if rep == False:
            count_life -= 1
            print(count_life)
print(fct_game())

# algo principale du jeu:
# fonction print du pendu