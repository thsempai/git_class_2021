from random import randint

nombre = input("Entrez un nombre entre 1 et 10: ")
if nombre == randint(1,10):
    print("Yay!")
else:
    print("Raté !")
