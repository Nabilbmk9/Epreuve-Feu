#Évaluer une expression

import sys


argument = "4 + 21"



def evaluer(suite = argument):
    calcule = []
    calcule2 =[]
    chiffre = ""
    for j in range(0, len(suite)):

        if j == len(suite)-1:
            if suite[j]!=" ":
                if chiffre != "":
                    chiffre += suite[j]
                    calcule.append(chiffre)
                    break

        if suite[j].isnumeric():
            chiffre += suite[j]

        elif not suite[j].isnumeric():
            if suite[j] != " ":
                if chiffre != "":
                    calcule.append(chiffre)
                    chiffre = ""
                calcule.append(suite[j])
        
    
    for k in calcule:
        if k.isnumeric():
            calcule2.append(int(k))
        
        else :
            calcule2.append(k)
    
    #Calcule
    for l in range(0,len(calcule2)):
        if calcule2[l] == "+":
            print((calcule2[l-1])+(calcule2[l+1]))
            

evaluer()
