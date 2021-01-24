import random

class Word:

    def __init__(self):
        self.name = []
        self.len = []

    def randWord(self):
        with open("mots.txt", "r") as fichier:
            list_w = fichier.read().split()
        word_l = random.sample(list_w, 1)
        word = word_l[0].lower()
        word = list(word)
        self.name = word
    
    def fct_create(self, word):
        self.name = list(len(word) * "*")
    
    def fct_fill(self, lettre, index):
        self.name[index] = lettre

    def fct_wordEasy(self, word):
        self.name[0] = word[0]
        self.name[len(word) - 1] = word[len(word) - 1]



