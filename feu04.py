#Trouver le plus grand carré

from pathlib import Path

#Chemin des fichier
CUR_DIR = Path.cwd()

PLATEAU = CUR_DIR / "feu04_plateau.txt"

Plateau = [i for i in PLATEAU.read_text()]

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

plateau = txt_to_array(Plateau)
nbr_de_ligne = plateau[0][0]
vide = plateau[0][1]
obstable = plateau[0][2]
remplir = plateau[0][3]
del plateau[0]

emplacement_carre = [0]

def trouver_carre():
    tour_i =0
    tour_j = 0

    while (tour_i<(len(plateau)) and (tour_j< len(plateau[0]))):
        #Parcour le tableau jusqu'a trouver un obstacle
        for i in range(0, len(plateau)):
            tour_i += i
            for j in range(0, len(plateau[0])):
                tour_j += j
                if plateau[i][j] == obstable:
                    #Parcour le tableau, jusqu'a trouver un autre obstacle
                    for i2 in range(i, len(plateau)):
                        for j2 in range(j+2, len(plateau[0])):
                            if (plateau[i2][j2] == obstable) and (obstable not in plateau[i][j+1:j2]):
                                #Parcour les ligne et colonne entre les 2 obstacles
                                for ix in range(i+1, i2+1):
                                    if (obstable in plateau[ix][j+1:j2]):
                                        break

                                    #trouver le dernier obstacle
                                    for i3 in range(i2+1, len(plateau)):
                                        for j3 in range(j+1, j2):                #Calcule pour connaitre le plus grand carre         
                                            if (plateau[i3][j3] == obstable) and (((j2 - j) * (i3 - i)) > emplacement_carre[0]):
                                                for xz in range(i, i3+1):
                                                    print(xz)
                                                    if obstable in plateau[xz][j+1:j2]:
                                                        break

                                                print(f"xz : {xz}, J : {j}, J2 : {j2}")
                                                print(plateau[xz][j+1:j2])
                                                del emplacement_carre[0:]
                                                emplacement_carre.append((j2 - j) * (i3 - i))
                                                emplacement_carre.extend([i,j,i2,j2,i3,j3])
                                                print(emplacement_carre)

    for f in range(emplacement_carre[1], emplacement_carre[5]):
        for fi in range(emplacement_carre[2]+1, emplacement_carre[4]):
            for xi in range(0, emplacement_carre[1]):
                if obstable not in plateau[xi][emplacement_carre[2]+1:emplacement_carre[4]]:
                    plateau[xi][fi] = remplir  
            plateau[f][fi] = remplir                                      
    for z in plateau:
        print(z)
trouver_carre()