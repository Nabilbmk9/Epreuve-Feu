#Labyrinthe

from ast import Try
from pathlib import Path
from turtle import position

#Chemin des fichier
CUR_DIR = Path.cwd()

LABYRINTHE = CUR_DIR / "feu05_labyrinthe.txt"

Labyrinthe = [i for i in LABYRINTHE.read_text()]

#Transformer le fichier texte en tableau
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

labyrynthe = txt_to_array(Labyrinthe)


#Lecture du tableau
Taille_Laby = labyrynthe[0][0:5]
Obstacle = labyrynthe[0][5]
Chemin = labyrynthe[0][6]
Remplir = labyrynthe[0][7]
Entre = labyrynthe[0][8]
Sortie = labyrynthe[0][9]
del labyrynthe[0]


def resoudre_laby():
    sortie = False
    continuer = True
    ligne = [0]
    colonne = [0]
    valeur_haute = [100000000000000,0,0]
    
    #Trouver l'entrée du labyrinthe
    for i in range(0, len(labyrynthe)):
        for j in range(0, len(labyrynthe)):
            if labyrynthe[i][j] == Entre:

                #Remplacer les caracteres vide par des nombre. +1 par case depuis l'entrée
                while sortie == False:
                    sortie = True
                    for fin in labyrynthe:
                        for finfin in fin:
                            if finfin == Chemin:
                                for ligne in range(0, len(labyrynthe)):
                                    for colonne in range(0, len(labyrynthe)):
                                        if (labyrynthe[ligne][colonne].isnumeric()):
                                        
                                            if (labyrynthe[ligne][colonne+1]==Chemin):
                                                labyrynthe[ligne][colonne+1]=str(int(labyrynthe[ligne][colonne])+1)

                                            if (labyrynthe[ligne-1][colonne]==Chemin) :
                                                labyrynthe[ligne-1][colonne]=str(int(labyrynthe[ligne][colonne])+1)

                                            if (labyrynthe[ligne+1][colonne]==Chemin) :
                                                labyrynthe[ligne+1][colonne]=str(int(labyrynthe[ligne][colonne])+1)
                                            
                                            if (labyrynthe[ligne][colonne-1]==Chemin) :
                                                labyrynthe[ligne][colonne-1]=str(int(labyrynthe[ligne][colonne])+1)
                                            
                                    sortie=False
                
                #Trouver la sortie la plus proche et stocker la position dans un variable
                for ss in range(0,len(labyrynthe)):
                    for si in range(0,len(labyrynthe)):
                        if labyrynthe[ss][si]== Sortie:

                            if si != len(labyrynthe[0])-1:
                                if (labyrynthe[ss][si+1].isnumeric()) and (int(labyrynthe[ss][si+1])< int(valeur_haute[0])):
                                    valeur_haute = [labyrynthe[ss][si+1], ss, si+1]

                            if ss > 0:
                                if (labyrynthe[ss-1][si].isnumeric()) and (int(labyrynthe[ss-1][si]) <int(valeur_haute[0])) :
                                    valeur_haute = [labyrynthe[ss-1][si], ss-1, si]

                            if ss != len(labyrynthe)-1:
                                if (labyrynthe[ss+1][si].isnumeric()) and (int(labyrynthe[ss+1][si]) <int(valeur_haute[0])) :
                                    valeur_haute = [labyrynthe[ss+1][si], ss+1, si]
  
                            if si != 0:
                                if (labyrynthe[ss][si-1].isnumeric()) and (int(labyrynthe[ss][si-1])<int(valeur_haute[0])) :
                                    valeur_haute = [labyrynthe[ss][si-1], ss, si-1]

                # Commencer par la sortie la plus coute et aller vers les nombres les plus petit a chaque fois
                while continuer == True:
                    continuer = False

                    if (labyrynthe[valeur_haute[1]][valeur_haute[2]+1].isnumeric()) and (int(labyrynthe[valeur_haute[1]][valeur_haute[2]+1]) < int(valeur_haute[0])):
                        labyrynthe[valeur_haute[1]][valeur_haute[2]] = Remplir
                        valeur_haute = [labyrynthe[valeur_haute[1]][valeur_haute[2]+1], valeur_haute[1], valeur_haute[2]+1]
                        continuer = True

                    if (labyrynthe[valeur_haute[1]-1][valeur_haute[2]].isnumeric()) and (int(labyrynthe[valeur_haute[1]-1][valeur_haute[2]]) < int(valeur_haute[0])):
                        labyrynthe[valeur_haute[1]][valeur_haute[2]] = Remplir
                        valeur_haute = [labyrynthe[valeur_haute[1]][valeur_haute[2]-1], valeur_haute[1], valeur_haute[2]-1]
                        continuer = True
                    
                    if (labyrynthe[valeur_haute[1]+1][valeur_haute[2]].isnumeric()) and (int(labyrynthe[valeur_haute[1]+1][valeur_haute[2]]) < int(valeur_haute[0])):
                        labyrynthe[valeur_haute[1]][valeur_haute[2]] = Remplir
                        valeur_haute = [labyrynthe[valeur_haute[1]+1][valeur_haute[2]], valeur_haute[1]+1, valeur_haute[2]]
                        continuer = True
                    
                    if (labyrynthe[valeur_haute[1]][valeur_haute[2]-1].isnumeric()) and (int(labyrynthe[valeur_haute[1]][valeur_haute[2]-1]) < int(valeur_haute[0])):
                        labyrynthe[valeur_haute[1]][valeur_haute[2]] = Remplir
                        valeur_haute = [labyrynthe[valeur_haute[1]][valeur_haute[2]-1], valeur_haute[1], valeur_haute[2]-1]
                        continuer = True
                    
    #Affiche. Enlever les nombre
    for sa in range(0, len(labyrynthe)):
        for sb in range(0, len(labyrynthe[0])):
            if (labyrynthe[sa][sb].isnumeric()) and (labyrynthe[sa][sb] != Entre):
                labyrynthe[sa][sb] = ' ' 

    for finish in labyrynthe:
        print(finish)                       
     
resoudre_laby()