import random

# mes liste de print pendu
pendu_1 = [
    """     +-----+-+
     |      \|
     |       |
             |
             |
             |
         ___/|\___""",

    """     +-----+-+
     |      \|
     |       |
     O       |
             |
             |
         ___/|\___""",

    """     +-----+-+
     |      \|
     |       |
     O       |
     |       |
             |
             |
         ___/|\___""",

    """     +-----+-+
     |      \|
     |       |
     O       |
    /|\      |
             |
             |
         ___/|\___""",

   """     +-----+-+
     |      \|
     |       |
     O       |
    /|\      |
    / \      |
             |
         ___/|\___"""
]

pendu_2 = [
    """   
            \|
             |
             |
             |
             |
         ___/|\___""",
    """     +-----+-+
            \|
             |
             |
             |
             |
         ___/|\___""",
    """     +-----+-+
     |      \|
     |       |
             |
             |
             |
         ___/|\___""",

    """     +-----+-+
     |      \|
     |       |
     O       |
             |
             |
         ___/|\___""",

    """     +-----+-+
     |      \|
     |       |
     O       |
     |       |
             |
             |
         ___/|\___""",

    """     +-----+-+
     |      \|
     |       |
     O       |
    /|\      |
             |
             |
         ___/|\___""",

   """     +-----+-+
     |      \|
     |       |
     O       |
    /|\      |
    / \      |
             |
         ___/|\___"""
]
# fonction récupere le mot
def fct_recup():
    with open("mots.txt", "r") as fichier:
        list_w = fichier.read().split()
    word_l = random.sample(list_w, 1)
    word = word_l[0].lower()
    word = list(word)
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

def fct_fill(new_word, lettre, index):
    new_word[index] = lettre
    return (new_word)

#fonction du jeu:
def fct_game(count_life, count_word, pendu):
    count_error = 0;
    while(count_word > 0 and count_life > 0):
        rep = False
        print(new_word)
        print("Vous avez " + str(count_life) + " vies pour y arriver !")
        lettre = input("veuillez saisir une lettre: ")
        if (len(lettre) == 1):
            if (64 < ord(lettre) < 91) or (96 < ord(lettre) < 123):
                for ii, i in enumerate(word):
                    if i == lettre:
                        fct_fill(new_word, lettre, ii)
                        count_word -= 1
                        rep = True
                        print(count_word)
                if rep == False:
                    count_life -= 1
                    print (pendu[count_error])
            else:
                print("Votre saisie est incorrect, recommencez !")
                fct_game(count_life, count_word)
        else:
            print("votre saisie est incorrect, recommencez !")
            fct_game(count_life, count_word)
    
    if count_word == 0 and count_life > 0:
        print("Bravo vous avez gagné en trouvant le mot " + ("".join(word)))
    else:
        print("Dommage vous avez perdu")

# algo niveau du jeu:
def fct_level():
    count_word = len(word)
    level = input("Quel niveau voulez-vous jouer 1, 2 ou 3 ? ")
    if len(level) == 1:
        if 0 < int(level) < 3:
            new_word[0] = word[0]
            new_word[len(word) - 1] = word[len(word) - 1]
            count_word -= 2
            if int(level) == 1:
                count_life = 7
                pendu = pendu_2
                fct_game(count_life, count_word, pendu)
            elif int(level) == 2:
                count_life = 5
                pendu = pendu_1
                fct_game(count_life, count_word, pendu)
        elif int(level) == 3:
            count_life = 5
            pendu = pendu_1
            fct_game(count_life, count_word, pendu)
        else:
            print("saisie incorrect recommencez !")
    else:
        print("saisie incorrect recommencez !")
        fct_level()
fct_level()
# fonction print du pendu
