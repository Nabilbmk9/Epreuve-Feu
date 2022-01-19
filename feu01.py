#Évaluer une expression
import sys

 
argument = sys.argv[1]


#Transformer la chaine de caractere en Liste avec des int
def string_to_liste(suite):
    calcule = []
    calcule2 =[]
    chiffre = ""
    for j in range(0, len(suite)):

        if j == len(suite)-1:
            if suite[j]!=" ":
                if chiffre != "" or suite[j].isnumeric():
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

    return calcule2
 

#Calcule d'abord les * les / et les %, puis + et - 
def calcule_prioritaire(calcule2=argument): 
    argument2 = calcule2
    resultat_final=0

    #Calcule des *, /, % en priorité
    while ("*" in argument2) or ("/" in argument2) or ("%" in argument2):
        for m in range(0,len(argument2)):

            if argument2[m] == "*":
                argument2[m] = argument2[m-1]*argument2[m+1]
                del argument2[m-1]
                del argument2[m]
                break
                
            elif argument2[m] == "/":
                argument2[m] = argument2[m-1]/argument2[m+1]
                del argument2[m-1]
                del argument2[m]
                break

            elif argument2[m] == "%":
                argument2[m] = argument2[m-1]%argument2[m+1]
                del argument2[m-1]
                del argument2[m]
                break       
    #Calcule tant qu'il y a une addition ou une soustraction
    while ("+" in argument2) or ("-" in argument2):
        for l in range(0,len(argument2)):
            if argument2[l] == "+":
                argument2[l-1] += argument2[l+1]
                resultat_final = argument2[0]
                del argument2[l:l+2]
                break

            if argument2[l] == "-":
                argument2[l-1] -= argument2[l+1]
                resultat_final = argument2[0]
                del argument2[l:l+2]
                break
    
    return resultat_final

#Calcule de l'argument avec priorité sur les parenthese
def calcule_final(calcule2):
    argument2 = string_to_liste(calcule2)
    resultat_final=[]
    variable = []
    while "(" in argument2:
        for n in range(0,len(argument2)):
            if argument2[n]=="(":
                for o in range(0, len(argument2)):
                    if argument2[o] == ")":
                        #les parenthese dans une variable
                        variable.extend(argument2[n+1:o])
                        #Calculer la variable
                        chiffre = calcule_prioritaire(variable)
                        #remplacer les parentheses par le resultat de la variable
                        argument2[n] = chiffre
                        del argument2[n+1 : o+1]
                        variable = []
                        break
                break
         
    #Calculer le reste
    resultat_final = calcule_prioritaire(argument2)

    return print(resultat_final)

                     
calcule_final(argument)

