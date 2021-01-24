from classPendu import Word
from dessinPendu import *
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "journal.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = "w")
logger = logging.getLogger()

word1 = Word()
logger.info("Création d'une instance de classe Word")
word1.randWord()
logger.info("Choix aléatoire d'un mot dans ma liste de mot")
word = word1.name
word2 = Word()
logger.info("Création d'une instance de classe Word")
word2.fct_create(word)
logger.info("Je remplie la mot vide par des *")
new_word = word2.name

def fct_game(count_life, count_word, pendu):
    logger.info("La fonction game a démarré")
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
                        word2.fct_fill(lettre, ii)
                        count_word -= 1
                        rep = True
                        print(count_word)
                if rep == False:
                    count_life -= 1
                    print(pendu[count_error])
            else:
                print("Votre saisie est incorrect, recommencez !")
                fct_game(count_life, count_word, pendu)
        else:
            print("votre saisie est incorrect, recommencez !")
            fct_game(count_life, count_word, pendu)
    
    if count_word == 0 and count_life > 0:
        print("Bravo vous avez gagné en trouvant le mot " + ("".join(word)))
        fct_replay()
    else:
        print("Dommage vous avez perdu")
        fct_replay()

def fct_replay():
    replay = input("Voulez-vous rejouer ? O/N")
    if (replay == "O"):
        fct_level()
    elif (replay == "N"):
        print("OK à bientôt !")
    else:
        print("votre saisie est incorrect !")
        fct_replay()



# algo niveau du jeu:
def fct_level():
    logger.info("La fonction level a démarré")
    count_word = len(word)
    level = input("Quel niveau voulez-vous jouer 1, 2 ou 3 ? ")
    if (len(level) == 1 and level.isnumeric()):
        if 0 < int(level) < 4:
            new_word[0] = word[0]
            new_word[len(word) - 1] = word[len(word) - 1]
            count_word -= 2
            if int(level) == 1:
                count_life = 7
                pendu = pendu_2
                fct_game(count_life, count_word, pendu)
            if int(level) == 2:
                count_life = 5
                pendu = pendu_1
                fct_game(count_life, count_word, pendu)
            elif int(level) == 3:
                count_life = 5
                pendu = pendu_1
                fct_game(count_life, count_word, pendu)
        else:
            print("saisie incorrect recommencez !")
            fct_level()
    else:
        print("saisie incorrect recommencez !")
        fct_level()
fct_level()