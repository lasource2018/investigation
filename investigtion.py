from tkinter import *
import pygame
import threading
import time
import jeu_principal
import sys

# variable définissant l'événement du morceau sonore d'intro terminé
INTRO_FINI = 23

# La fonction son_fini nous permet de savoir à quel moment le morceau sonore est terminée grâce à
# l'événement PAS_MUSIC
def son_fini():
    while True:
        musique_finie = pygame.event.get(INTRO_FINI)
        if musique_finie:
            # Création de la fenêtre de jeu principal, exécution du jeu
            jeu_principal.jeu_principal(fenetre_accueil)
            break
        else:
            time.sleep(0.3)

# La fonction jouer est exécutée lorsque le bouton jouer est cliqué
def jouer():

    # cache le cadre accueil
    cadre_accueil.pack_forget()
    messagerie = PhotoImage(file="messagerie2.png")

    canvas_messagerie = Canvas(cadre_msg, width=393, height=700)
    # Il faut attacher le PhotoImage au widget du Canvas pour ne pas que l'image soit perdu http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
    canvas_messagerie.messagerie = messagerie
    canvas_messagerie.create_image(0, 0, anchor=NW, image=messagerie)
    canvas_messagerie.pack()
    cadre_msg.pack()

    pygame.init()

    # chargement du morceau à jouer
    #pygame.mixer.music.load("message vocal de rose2.mp3")
    pygame.mixer.music.load("test.mp3")
    pygame.mixer.music.set_endevent(INTRO_FINI)
    pygame.mixer.music.play()

    # Création d'un autre fil (thread) d'exécution pour attraper l'événement de fin de morceau sonore
    t = threading.Thread(target=son_fini)
    t.start()

#début du corps principal du code

# création de la fenêtre principale
fenetre_accueil = Tk()
fenetre_accueil.configure(background="white")
fenetre_accueil.wm_minsize(600, 700)
fenetre_accueil.wm_maxsize(600, 700)
fenetre_accueil.wm_title("Investigation")

# création d'un cadre accueil
cadre_accueil=Frame(fenetre_accueil, bg="white")
cadre_accueil.pack()

# cadre pour la messagerie
cadre_msg=Frame(fenetre_accueil)

titre_label = Label(cadre_accueil, text="INVESTIGATION", font=("Broadway", 35), bg="white")
titre_label.pack()

photo = PhotoImage(file="detective.png")
canvas_photo = Canvas(cadre_accueil, width=550, height=550, bg="white")
canvas_photo.create_image(0, 5, anchor=NW, image=photo)
canvas_photo.pack()

jouer_bouton = Button(cadre_accueil, width=20, height=5, text="JOUER", font=("calibri", 20), bg="light slate blue", command=jouer)
jouer_bouton.pack()

fenetre_accueil.mainloop()
