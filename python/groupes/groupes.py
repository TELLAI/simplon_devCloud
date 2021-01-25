
import sys, random, json, logging

#creation et configuration du logger:
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "journal.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = "w")
logger = logging.getLogger()

# test du logger
logger.info("salut")

print(logger.level)

with open("liste_noms.txt", "r") as fichier:
    liste_n = fichier.read().split()
    print(liste_n)

for arg in sys.argv:
    st =  arg
nb =int(st)
print(type(nb))

def create_group(liste_n, nb):
    all_groupes = {}
    x = 0

    while (len(liste_n)) > 0:

        if (len(liste_n)) >= nb:
            groupe = random.sample(liste_n, nb)
            x += 1
            all_groupes[x] = groupe

        else:
            groupe = random.sample(liste_n, len(liste_n))
            x += 1
            all_groupes[x] = groupe

        for i in groupe:
            liste_n.remove(i)

    with open("groupes.json", "w") as groupe_f:
        json.dump(all_groupes, groupe_f, indent=4)
    return all_groupes

print(create_group(liste_n, nb))