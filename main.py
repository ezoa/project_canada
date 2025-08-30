# chercher_la_moyenne="entrez des note"
# francais=int(input("entrez un nombre de 1 a 10 POUR FRANCAIS"))
# anglais=int(input("entrez un nombre de 1 a 10 POUR ANGLAIS"))
# math=int(input("entre un nombre de 1 a 10 POUR MATH"))
# resultat=(francais+anglais+math)/3
# print("votre moyenne est ",resultat)
from tkinter import *


r= Tk()
r.title("caculatrice de moyenne")
Label(r, text="Français").grid(row=0, column=0)
francaisentry = Entry(r)
francaisentry.grid(row=0, column=1)

Label(r, text="Anglais").grid(row=1, column=0)
ANGLAISentry = Entry(r)
ANGLAISentry.grid(row=1, column=1)

Label(r, text="Math").grid(row=2, column=0)
mathentry = Entry(r)
mathentry.grid(row=2, column=1)


def ajouter():
    try:     
        francais = int(francaisentry.get())
        anglais = int(ANGLAISentry.get())      
        math = int(mathentry.get()) 
        resultat = (francais + anglais + math) / 3
        Label(r, text=f"votre moyenne est  {resultat}",fg="green").grid(row=4, column=0, columnspan=2)
        # print("votre moyenne est ", resultat)
    except ValueError:
        Label(r, text="Veuillez entrer des nombres valides ou sinon je vous ban.",fg="red").grid(row=4, column=0, columnspan=2)
        # print("Veuillez entrer des nombres valides ou sinon je vous ban.")

Button(r, text="calculer la moyenne", command=ajouter).grid(row=3, column=0, columnspan=2)
r.mainloop()
 
