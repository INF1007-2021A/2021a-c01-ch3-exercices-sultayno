import math
import random

#Le programme génère un prix rond aléatoire.
#Le but pour l’utilisateur est de deviner le prix. Chaque fois que l’utilisateur se trompe,
#l’ordinateur lui dit si c’est plus ou moins que le prix qu’il a donné. À chaque aide de l’ordinateur,
#le score final atteignable par le joueur baisse.
print ("Wsh pti bg dla tess, alors comme ça on veut deviner lprix ou quoi la")
print("Vzy laise l'ordi générer un prix rond aléatoire entre '0' et '10 000' (qui finis par '0')...")
print("...")
print("...")
print("...")
pcuNumber=(random.randint(0,10000))
while pcuNumber%10!=0:
    pcuNumber=(random.randint(0, 10000))
print("C'est bon! ")
userNumber=int(input("À toi de jouer, devine: "))
numberOfChances=10
possibilities=(range(0,10000,10))
for i in possibilities:
    while userNumber not in possibilities:
        print("-------------------------------------------------------------------------------------")
        print("Il faut inscrire un nombre rond (qui finis par '0') entre '0' et '10 000'!")
        userNumber=int(input("rééssaye: "))

while userNumber>pcuNumber:
    print("-------------------------------------------------------------------------------------")
    numberOfChances += -1
    if numberOfChances == 0:
        print("Ta perdu :'(")
        print("\u2764\ufe0f")
        print("La réponse était: ")
        print(pcuNumber)
        break
    print("C'est moins :(")
    print("Nombre de chances restantes:")
    print(numberOfChances)
    userNumber = int(input("rééssaye: "))
    for i in possibilities:
        while userNumber not in possibilities:
            print("-------------------------------------------------------------------------------------")
            print("Il faut inscrire un nombre rond (qui finis par '0') entre '0' et '10 000'!")
            userNumber = int(input("rééssaye: "))
    while userNumber < pcuNumber:
        print("-------------------------------------------------------------------------------------")
        numberOfChances += -1
        if numberOfChances==0:
            print("Ta perdu :'(")
            print("\u2764\ufe0f")
            print("La réponse était: ")
            print(pcuNumber)
            break
        print("C'est plus :(")
        print("Nombre de chances restantes:")
        print(numberOfChances)
        userNumber = int(input("rééssaye: "))
        for i in possibilities:
            while userNumber not in possibilities:
                print("-------------------------------------------------------------------------------------")
                print("Il faut inscrire un nombre rond (qui finis par '0') entre '0' et '10 000'!")
                userNumber = int(input("rééssaye: "))

while userNumber<pcuNumber:
    print("-------------------------------------------------------------------------------------")
    numberOfChances += -1
    if numberOfChances == 0:
        print("Ta perdu :'(")
        print("\u2764\ufe0f")
        print("La réponse était: ")
        print(pcuNumber)
        break
    print("C'est plus :(")
    print("Nombre de chances restantes:")
    print(numberOfChances)
    userNumber=int(input("rééssaye: "))
    for i in possibilities:
        while userNumber not in possibilities:
            print("-------------------------------------------------------------------------------------")
            print("Il faut inscrire un nombre rond (qui finis par '0') entre '0' et '10 000'!")
            userNumber = int(input("rééssaye: "))
    while userNumber > pcuNumber:
        print("-------------------------------------------------------------------------------------")
        numberOfChances += -1
        if numberOfChances==0:
            print("Ta perdu :'(")
            print("\u2764\ufe0f")
            print("La réponse était: ")
            print(pcuNumber)
            break
        print("C'est moins :(")
        print("Nombre de chances restantes:")
        print(numberOfChances)
        userNumber = int(input("rééssaye: "))
        for i in possibilities:
            while userNumber not in possibilities:
                print("-------------------------------------------------------------------------------------")
                print("Il faut inscrire un nombre rond (qui finis par '0') entre '0' et '10 000'!")
                userNumber = int(input("rééssaye: "))

if userNumber==pcuNumber:
    print("-------------------------------------------------------------------------------------")
    print(u"\u2605")
    print("Bravo!")
    print(u"\u2605")
