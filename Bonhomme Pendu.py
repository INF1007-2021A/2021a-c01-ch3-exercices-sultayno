import random
import math
import string

noMistake='''
      +-----=
            |
            |
            |
           ==='''
oneMistake='''
      +-----=
     o      |
            |
            |
           ==='''
twoMistake='''
      +-----=
     o      |
     |      |
            |
           ==='''
threeMistake='''
      +-----=
     o      |
    \|      |
            |
           ==='''
fourMistake='''
      +-----=
     o      |
    \|/     |
            |
           ==='''
fiveMistake='''
      +-----=
     o      |
    \|/     |
     |      |
           ==='''
sixMistake='''
      +-----=
     o      |
    \|/     |
     |      |
    /      ==='''
sevenMistake='''
      +-----=
     o      |
    \|/     |
     |      |
    / \    ==='''
wordList=["sophia","islam","mohamed","belkacem"]
choosenWord=random.choice(wordList)
mistakes=[noMistake,oneMistake,twoMistake,threeMistake,fourMistake,fiveMistake,sixMistake,sevenMistake]
numberOfMistakes=0
wrongLetters=[]
goodLetters=[]
while len(goodLetters)<len(choosenWord):
    list.append(goodLetters,"_")
alphabet=string.ascii_letters

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("On est back sur un des ptits jeux du SUL ou quoi lah")
userLetter=input("Choisis une lettre: ").lower()

while userLetter not in alphabet or len(userLetter)!=1:
    userLetter=input("Écris UNE lettre: ").lower()

while userLetter in choosenWord:
    useful = 0
    if userLetter in goodLetters:
        print("Tu as déjà mis cette lettre")
    elif userLetter not in goodLetters:
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("La lettre", userLetter, "est dans le mot secret. Bien joué!")
        print("Lettres incorrectes:")
        print(wrongLetters)
        print(mistakes[numberOfMistakes])
        for letter in choosenWord:
            if userLetter == letter:
                if goodLetters[choosenWord.index(letter)+useful]=="_":
                    goodLetters.pop(choosenWord.index(letter)+useful)
                    goodLetters.insert(choosenWord.index(letter)+useful,letter)
                    useful += 1
        print("Lettres trouvées:")
        print(goodLetters)
        if goodLetters.count("_")==0:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("Bravo! tu as découvert le mot", choosenWord,"! :)")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            break
    userLetter = input("Écris une lettre: ").lower()
    while userLetter not in alphabet or len(userLetter)!=1:
        userLetter = input("Écris UNE lettre: ").lower()

while userLetter not in choosenWord:
    if userLetter in wrongLetters:
        print ("Tu as déjà mis cette lettre")
    elif userLetter not in wrongLetters:
        numberOfMistakes += 1
        list.append(wrongLetters, userLetter)
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("La lettre", userLetter, "n'est pas dans le mot secret. Recommence")
        print("Lettres incorrectes:")
        print(wrongLetters)
        print(mistakes[numberOfMistakes])
        print("Lettres trouvées:")
        print(goodLetters)
    userLetter=input("Écris une lettre: ").lower()
    while userLetter not in alphabet or len(userLetter)!=1:
        userLetter = input("Écris UNE lettre: ").lower()
    if numberOfMistakes==6:
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print(sevenMistake)
        print("Perdu! :(")
        break
    while userLetter in choosenWord:
        useful = 0
        if userLetter in goodLetters:
            print("Tu as déjà mis cette lettre")
        elif userLetter not in goodLetters:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("La lettre", userLetter, "est dans le mot secret. Bien joué!")
            print("Lettres incorrectes:")
            print(wrongLetters)
            print(mistakes[numberOfMistakes])
            for letter in choosenWord:
                if userLetter == letter:
                    if goodLetters[choosenWord.index(letter) + useful] == "_":
                        goodLetters.pop(choosenWord.index(letter) + useful)
                        goodLetters.insert(choosenWord.index(letter) + useful, letter)
                        useful += 1
            print("Lettres trouvées:")
            print(goodLetters)
            if goodLetters.count("_") == 0:
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                print("Bravo! tu as découvert le mot", choosenWord,"! :)")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                break
        userLetter = input("Écris une lettre: ").lower()
        while userLetter not in alphabet or len(userLetter)!=1:
            userLetter = input("Écris UNE lettre: ").lower()