#Trouver une forme
import sys
from pathlib import Path

#Chemin des fichier
CUR_DIR = Path.cwd()
Board = CUR_DIR / sys.argv[1]
To_find = CUR_DIR / sys.argv[2]

#Fichier transformer en liste
board = [i for i in Board.read_text()]
to_find = [i for i in To_find.read_text()]

#Variable pour savoir quand est ce que l'objet est trouvé. (utilisé plus bas avec la fonction len())
nbr_de_tour =[]
for i in to_find:
    if i != "\n":
        nbr_de_tour.append(i)

#Liste transformer en tableau
def txt_to_array(liste):
    tab=[]
    while liste != []:
        for i in range(0,len(liste)):
            if i == len(liste)-1:
                tab.extend([liste[0:]])
                del liste[0:]
                break

            elif liste[i]=="\n":
                tab.extend([liste[0:i]])
                del liste[0:i+1]
                break
    return tab


tab = txt_to_array(board)
trouver = txt_to_array(to_find)
tab_final=[]

#Fonction Final
def trouver_forme():
    position_total=[]
    tour = 0
    tour2 = 0

    #Parcours le tableau
    for i in range(0, len(tab)):
        for j in range(0, len(tab[0])):
            if tab[i][j]== trouver[0][0]:
                print(f"i : {i}, j : {j}")

                for k in range(0, len(trouver)):
                    for l in range(0, len(trouver)):
                        if trouver[k][l]==" ":
                            tour+=1
                            continue
                        elif tab[i+k][j+l] == trouver[k][l]:
                            tour+=1

                            #Variable pour l'affiche
                            position_total.extend([i+k, j+l])

                            if tour == len(nbr_de_tour):
                                print("Trouvé!")
                                print(f"Coordonées : {i}, {j}")

                                #Enlever les elements du tableau, sauf l'objet trouvé
                                for o in range(0, len(tab)):
                                    for p in range(0, len(tab[0])):
                                        if position_total != []:
                                            if (o == position_total[tour2]) and (p == position_total[tour2+1]):
                                                position_total.pop(tour2)
                                                position_total.pop(tour2)
                                                continue
                                            else:
                                                tab[o][p]="-"
                                        else:
                                            tab[o][p]="-"

                                #Affichage du nouveau tableau
                                for q in tab:
                                    for r in q:
                                        print(r, end="")
                                    print()
                                return                     
                        else:
                            tour =0
                            position_total = []
    return print("Introuvable")

trouver_forme()