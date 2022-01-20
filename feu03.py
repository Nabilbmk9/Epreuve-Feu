#Sudoku

import sys
from pathlib import Path

#Chemin des fichier
CUR_DIR = Path.cwd()

SUDOKU = CUR_DIR / sys.argv[1]

Sudoku = [i for i in SUDOKU.read_text()]

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

sudoku = txt_to_array(Sudoku)



def sudok(sudoku):
    possibilite = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    def solve(sudoku):
        colonne = []
        carre = []
        #Parcours le sudoku
        for j in range(0, len(sudoku)):
            for k in range(0, len(sudoku[0])):
                if sudoku[j][k] == '.':
                    for x in possibilite:
                        #Parcours la ligne
                        if x not in sudoku[j]:
                            #Créer une variable avec la colonne
                            for z in range(0, len(sudoku)):
                                colonne.append(sudoku[z][k])

                            if x not in colonne:
                                #Créer un variable pour les carre de 3
                                for y in range(((j)//3)*3, ((j)//3)*3+3):
                                    for w in range(((k-1)//3)*3, ((k-1)//3)*3+3):
                                        carre.append(sudoku[y][w])
                                
                                if x not in carre:
                                    #Ni en ligne, ni en colonne, ni dans les carrés de 3
                                    sudoku[j][k] = x
                                    carre = []
                                    colonne = []

                                    #Recommencer jusqu'a que tout soit rempli
                                    for j2 in range(0, len(sudoku)):
                                        for k2 in range(0, len(sudoku[0])):
                                            if sudoku[j2][k2] == '.':
                                                solve(sudoku)

                                    else:
                                        for ml in sudoku:
                                            print(ml)
                                        print()
                                        sys.exit()
                            else :
                                colonne = []
    solve(sudoku)
sudok(sudoku)
