import math

print("wsh bg, tva utiliser ma ptite calculatrice de soustraction")
a=int(input("ecris un num: "))
while type(a) != int:
    a = int(input("ecris un num: "))

b=input("ecris loperation '-': ")
while b != "-":
    b= (input("ecris loperation '-': "))

c=int(input("ecris ton deuxieme num: "))

while type(c) != int:
    c = int(input("ecris ton deuxieme num: "))

print ("Voila ta reponse pti bg")
print(a-c)
