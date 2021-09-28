import math
import random

print ("Salut petit white-it, on va voir si tu va trouver l'bon num ouquoi la")


a= int(input ("Choisis un chiffre entre 0 & 9: "))
b =math.floor(random.random() * 10)
while a != b    :
    print(b)
    print("sal zgeg recommence")
    b = math.floor(random.random() * 10)
    a = int(input ("Choisis un chiffre entre 0 & 9: "))
print("bg")
