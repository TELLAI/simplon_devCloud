import random

# fonction récupere le mot

def fct_recup():
    with open("mots.txt", "r") as fichier:
        list_w = fichier.read().split()
    word_l = random.sample(list_w, 1)
    word = list(word_l[0])
    return (word)
print(fct_recup())


def fct_create():
    new_word = len(fct_recup()) * "*"
    return (new_word)
print(fct_create())

