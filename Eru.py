import math
import random


p= "pierre"
f= "feuille"
c= "ciseaux"
liste_ordi= [p,f,c]
reponse_ordi=random.choice(liste_ordi)
points_utilisateur=0
points_ordi=0

print("Alors ptit bg, on est de retour sur un d'mes jeux ouquoi lah?")
reponse_utilisateur=input( "Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
while reponse_utilisateur != p and reponse_utilisateur !=f and reponse_utilisateur !=c:
    print ("ecris bien wsh: ")
    reponse_utilisateur=input( "Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

while reponse_utilisateur == p or reponse_utilisateur ==f or reponse_utilisateur ==c:
    if reponse_utilisateur == p and reponse_ordi==p:
        print(reponse_ordi)
        print("bon bah ptite égalité")
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_ordi=random.choice(liste_ordi)
        reponse_utilisateur=input( "Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

    elif reponse_utilisateur == p and reponse_ordi==f:
        print(reponse_ordi)
        print("bon bah ta perdu")
        reponse_ordi = random.choice(liste_ordi)
        points_ordi+=1
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_utilisateur=input( "Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

    elif reponse_utilisateur == p and reponse_ordi == c:
        print(reponse_ordi)
        print("bon bah ta gagné")
        reponse_ordi = random.choice(liste_ordi)
        points_utilisateur += 1
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

    elif reponse_utilisateur == f and reponse_ordi == f:
        print(reponse_ordi)
        print("bon bah ptite égalité")
        reponse_ordi = random.choice(liste_ordi)
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

    elif reponse_utilisateur == f and reponse_ordi == c:
        print(reponse_ordi)
        print("bon bah ta perdu")
        reponse_ordi = random.choice(liste_ordi)
        points_ordi += 1
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

    elif reponse_utilisateur == f and reponse_ordi == p:
        print(reponse_ordi)
        print("bon bah ta gagné")
        reponse_ordi = random.choice(liste_ordi)
        points_utilisateur += 1
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

    elif reponse_utilisateur == c and reponse_ordi == c:
        print(reponse_ordi)
        print("bon bah ptite égalité")
        reponse_ordi = random.choice(liste_ordi)
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

    elif reponse_utilisateur == c and reponse_ordi == p:
        print(reponse_ordi)
        print("bon bah ta perdu")
        reponse_ordi = random.choice(liste_ordi)
        points_ordi += 1
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")

    elif reponse_utilisateur == c and reponse_ordi == f:
        print(reponse_ordi)
        print("bon bah ta gagné")
        points_utilisateur += 1
        print("Tes points:")
        print(points_utilisateur)
        print("Points ordi:")
        print(points_ordi)
        reponse_ordi = random.choice(liste_ordi)
        reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")
        while reponse_utilisateur != p and reponse_utilisateur != f and reponse_utilisateur != c:
            print("ecris bien wsh: ")
            reponse_utilisateur = input("Choisis entre 'pierre' 'feuille' ou 'ciseaux': ")


