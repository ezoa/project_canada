# chercher_la_moyenne="entrez des note"
# francais=int(input("entrez un nombre de 1 a 10 POUR FRANCAIS"))
# anglais=int(input("entrez un nombre de 1 a 10 POUR ANGLAIS"))
# math=int(input("entre un nombre de 1 a 10 POUR MATH"))
# resultat=(francais+anglais+math)/3
# print("votre moyenne est ",resultat)
import tkinter as tk
root=tk.Tk
def moyenne():
    francais=int(input("entrez les notes de 1 a 10 en francais"))
    anglais =int(input("entrez les notes de 1 a 10 en anglais"))
    math=int(input("entrez les notes de 1 a 10 en math"))
    return francais,anglais,math
