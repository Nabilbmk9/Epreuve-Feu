#Echauffement

import sys


#Gestion d'erreurs

if len(sys.argv) != 3:
    print("erreur.")
    sys.exit()

for x in sys.argv[1:]:
    if not x.isnumeric():
        print("erreur.")
        sys.exit()


#Argument par defaut
larg = sys.argv[1]
long = sys.argv[2]

#Fonction
def echauffement(largeur=larg, longeur=long):

    if largeur == "1":
        print("o")

    else:
        print("o" + "-"*(int(largeur)-2)+"o")

    for i in range(1, int(longeur)):
        if i != int(longeur)-1:
            print("|" + " "*(int(largeur)-2)+"|" )
        else:
            print("o" + "-"*(int(largeur)-2)+"o")

echauffement()