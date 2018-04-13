from tkinter import *

def bulles_messages():
    bulles=Canvas()

def jeu_principal():

    fenetrePrincipale = Tk()

    fenetrePrincipale.wm_minsize(600, 700)
    fenetrePrincipale.wm_maxsize(600, 700)
    fenetrePrincipale.wm_title("Interface messages")

    #Afficher le nom du contact
    cadreContact = Canvas(fenetrePrincipale, width=600, height=50)
    cadreContact.pack(side="top")
    nomContact = Label(cadreContact, text="Rose", bg="pale green")
    nomContact.pack()

    #création d'un cadre pour insérer les choix de réponse (un cadre principale, un cadre par serie de choix de réponses
    cadreReponse = Canvas(fenetrePrincipale, width=600, height=200, bg="pale green")
    cadreReponse.pack(side="bottom")

    #création d'un cadre pour le défilement des messages
    cadreMessages = Canvas(fenetrePrincipale, widt=600, height="500", bg="ivory")
    cadreMessages.pack()

    #création d'une barre de défilement
    BarreDefiler = Scrollbar(cadreMessages, orient="vertical")
    BarreDefiler.pack()


    fenetrePrincipale.mainloop()

