from tkinter import *
import time
import sys

width=425
height=650
wraplength=215

intervalle_temps = 200

fenetre_principal = None
fenetre_demarrage = None
fr=None
message_canvas=None
reponse_canvas=None
reponse_enigme=None
ligne_message=7

message_a_afficher = 1

liste_reponse={ 'r1' : 'Interroge sa mère pour savoir où il est allé en premier',
                'r2' : 'Tente de trouver des indices dans sa chambre',
                'r6' : 'Celui qui dit que Kevin est allé chez Pierre, un ami à lui dans une rue à droite',
                'r7' : 'Celui qui dit que Kevin est allé voir un de ses partenaires de travail dans une rue à gauche',
                'r10' : 'où Kevin est allé après être allé le voir',
                'r11' : 's\'il est au courant de quelque chose de louche qui pourrait être liée à la disparition de Kevin',
                'r12' : 'c\'est louche, on retourne dans la rue de droite',
                'r13' : 'on le suit',
                'r4' : 'Va chez son oncle',
                'r5' : 'Va chez Melina, c’est à 2 min d\'ici',
                'r8': 'Bon bah tant pis pars d\'ici on va essayer de trouver des indices ailleurs',
                'r9' : 'ça veut dire qu\'elle est à l\'intérieur, enfonce la porte, le temps presse',
                'r14' : 'Mme Peletier',
                'r15' : 'Camilia',
                'r16' : 'Essaie de lui faire cracher le morceau, elle doit couvrir Adam. Dis-lui qu\'on sait que c\'est Calvin et Adam qui ont fait le coup',
                'r17' : 'Demande à sa voisine, elle doit savoir quelque chose'}

# variable stockant les réponses des boutons radios
reponse_glob= ""

def rejouer():
    global message_a_afficher, fr, reponse_canvas, fenetre_principal
    message_a_afficher = 1
    supprimer_widget(fr)
    supprimer_widget(reponse_canvas)
    fenetre_principal.after(250, affichage_dialogue)

def quitter():
    sys.exit(0)

def selectionner_reponse(rep):
    global reponse_glob
    reponse_glob = rep

def supprimer_widget(widget_parent):
    for widget in widget_parent.grid_slaves():
        widget.destroy()


def traiter_reponse_enigme():
    global reponse_enigme, ligne_message, reponse_canvas, fenetre_principal, message_a_afficher, message_canvas
    # en minuscule
    reponse = reponse_enigme.get().lower()
    # supprime les espaces avant et après un mot
    reponse = reponse.strip()

    if reponse == "espoir" or reponse == "espérance" or reponse == "esperance" or reponse == "l'espoir":
        #Enigme résolu
        #Label(fr, text=liste_reponse["enigme_resolu"], borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        #supprimer_widget(reponse_canvas)
        message_a_afficher = 16
        fenetre_principal.after(200, affichage_dialogue)

    else:
        message_a_afficher = 200
        fenetre_principal.after(200, affichage_dialogue)
        #Label(fr, text=liste_reponse["enigme_non_resolu"], borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)

    # Mise à jour de la frame
    fr.update_idletasks()
    message_canvas.config(scrollregion=message_canvas.bbox("all"))
    message_canvas.yview_moveto(1)

def traiter_reponse():
    global reponse_glob, ligne_message, message_canvas, fr, reponse_enigme, reponse_canvas, message_a_afficher
    ligne_message += 1
    Label(fr, text=liste_reponse[reponse_glob], borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
    # Mis à jour des paramètres du canvas et du frame pour que le scrollbar s'affiche et fasse défiler les réponses
    message_canvas.create_window(0, 0, window=fr)
    fr.update_idletasks()
    message_canvas.config(scrollregion=message_canvas.bbox("all"))
    if  (reponse_glob == "r1"):
        # Suite de dialogues entre Rose et Paul avant enigme
        message_a_afficher = 10
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r2"):
        message_a_afficher = 100
        # efface le canvas des réponses
        supprimer_widget(reponse_canvas)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r6"):
        message_a_afficher = 20
        supprimer_widget(reponse_canvas)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r7"):
        message_a_afficher = 22
        supprimer_widget(reponse_canvas)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r10"):
        message_a_afficher = 21.5
        supprimer_widget(reponse_canvas)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r11"):
        message_a_afficher = 21.5
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r12"):
        message_a_afficher = 20
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r13"):
        message_a_afficher = 24
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r4"):
        message_a_afficher = 14
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r5"):
        message_a_afficher = 104
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r8"):
        message_a_afficher = 106
        supprimer_widget(reponse_canvas)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r9"):
        message_a_afficher = 118
        supprimer_widget(reponse_canvas)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r14"):
        message_a_afficher = 110
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == "r15"):
        message_a_afficher = 114
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == 'r16'):
        message_a_afficher = 115
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

    elif (reponse_glob == 'r17'):
        message_a_afficher = 122
        fenetre_principal.after(intervalle_temps, affichage_dialogue)

def affichage_dialogue():
    global message_a_afficher, message_canvas, reponse_canvas, fr, ligne_message, reponse_enigme
    # Premiers messages
    if message_a_afficher == 1:
        Label(fr, text="Je vais t'aider Rose", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=0, column=1, sticky=E)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher += 1
    elif message_a_afficher == 2:
        Label(fr, text="Parfait. Tu es prêt à rester connecter avec moi 24h sur 24? ", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=1, column=0, sticky=W)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher += 1
    elif message_a_afficher == 3:
        Label(fr, text="Je n'ai pas vraiment le choix de toute façon non ?", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=2, column=1, sticky=E)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher += 1
    elif message_a_afficher == 4:
        Label(fr, text="haha oui... je pensais commencer par chez-lui ", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=3, column=0, sticky=W)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher += 1
    elif message_a_afficher == 5:
        Label(fr, text="ok mais euh tu vas te pointer chez ses parents comme ça : \"bonjour je pense que la vie de votre fils est en danger, auriez-vous des renseignements pour que je le retrouve ?\"", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=4, column=1, sticky=E)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher += 1
    elif message_a_afficher == 6:
        Label(fr, text="Mais non imbécile j'inventerai une excuse bidon genre j'ai oublié un devoir chez lui!", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=5, column=0, sticky=W)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher += 1
    elif message_a_afficher == 7:
        Label(fr, text="Ah oui pas bête!", borderwidth=2, relief="ridge", bg="pale green").grid(row=6, column=1, sticky=E)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher += 1
    elif message_a_afficher == 8:
        Label(fr, text="Je suis arrivée chez lui. Je commence par quoi?", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=7, column=0, sticky=W)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher += 1
    elif message_a_afficher == 9:
        reponse = StringVar()
        radio1 = Radiobutton(reponse_canvas, text=liste_reponse["r1"], variable=reponse, value="r1", command=lambda: selectionner_reponse("r1"), wraplength=wraplength)
        radio2 = Radiobutton(reponse_canvas, text=liste_reponse["r2"], variable=reponse, value="r2", command=lambda: selectionner_reponse("r2"), wraplength=wraplength)
        radio1.select()
        selectionner_reponse("r1")
        radio2.deselect()
        radio1.grid(row=0, column=0)
        radio2.grid(row=0, column=1)
        okbutton = Button(reponse_canvas, text="OK", command=traiter_reponse)
        # columnspan est un paramètre qui permet d'étendre le widget à plusieurs colonnes
        okbutton.grid(row=1, column=0, columnspan=2)
    elif message_a_afficher == 10:
        ligne_message += 1
        Label(fr, text="Bon elle n’est pas très bavarde mais elle m’a quand même appris des trucs. Selon elle, Kevin est parti voir Amélie", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 11:
        ligne_message += 1
        Label(fr, text="Ok bon bah va la voir, elle traine toujours au café en face de chez lui.", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 12:
        ligne_message += 1
        Label(fr, text="Oui je viens de la croiser, elle m’a dit  qu’elle et Kevin devait déjeuner hier ensemble vers 12h mais qu’il est parti voir son oncle sans raison donc je me dirige vers chez lui", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 13:
        ligne_message += 1
        Label(fr, text="ok", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 14:
        ligne_message += 1
        Label(fr, text="Son oncle dit qu’il veut bien nous aider à condition qu’on réponde à une énigme", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 15:
        # Enigme de l'oncle
        ligne_message += 1
        Label(fr, text="Voici l'énigme de l'oncle :\"L’échec ne l’arrête pas, il va de pair avec la foi, on dit qu’il fait vivre\"", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        # efface le canvas des réponses
        supprimer_widget(reponse_canvas)
        # mettre le champ de texte pour réponse
        reponse_enigme = Entry(reponse_canvas)
        reponse_enigme.grid(row=0, column=0, columnspan=2)
        Button(reponse_canvas, text="OK", command=traiter_reponse_enigme).grid(row=1, column=0, columnspan=2)
    elif message_a_afficher == 16:
        ligne_message +=1
        Label(fr, text="Bien joué, c’est ça ! Son oncle m’a expliqué qu’il était paniqué quand il est passé le voir car il avait reçu un SMS étrange qui disait « nous te surveillons Kévin ». Il est ensuite allé rue Martini, j'y vais.", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        supprimer_widget(reponse_canvas)
        message_a_afficher +=1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 200:
        ligne_message += 1
        Label(fr, text="L\'oncle dit que ce n\'est pas cela, essaie autre chose.", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
    elif message_a_afficher == 17:
        ligne_message += 1
        Label(fr, text="Tu vois quelqu'un ?", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher +=1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 18:
        ligne_message += 1
        Label(fr, text="Oui deux commerçants mais qui ont une version différente. Lequel j'écoute ?", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher +=1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 19:
        reponse = StringVar()
        radio1 = Radiobutton(reponse_canvas, text=liste_reponse["r6"], variable=reponse, value="r1", command=lambda: selectionner_reponse("r6"), wraplength=wraplength)
        radio2 = Radiobutton(reponse_canvas, text=liste_reponse["r7"], variable=reponse, value="r2", command=lambda: selectionner_reponse("r7"), wraplength=wraplength)
        radio1.select()
        selectionner_reponse("r6")
        radio2.deselect()
        radio1.grid(row=0, column=0)
        radio2.grid(row=0, column=1)
        okbutton = Button(reponse_canvas, text="OK", command=traiter_reponse)
        # columnspan est un paramètre qui permet d'étendre le widget à plusieurs colonnes
        okbutton.grid(row=1, column=0, columnspan=2)
    elif message_a_afficher == 20:
        ligne_message += 1
        Label(fr, text="Je suis chez Pierre, je lui demande quoi?", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 21:
        reponse = StringVar()
        radio1 = Radiobutton(reponse_canvas, text=liste_reponse["r10"], variable=reponse, value="r1", command=lambda: selectionner_reponse("r10"), wraplength=wraplength)
        radio2 = Radiobutton(reponse_canvas, text=liste_reponse["r11"], variable=reponse, value="r2", command=lambda: selectionner_reponse("r11"), wraplength=wraplength)
        radio1.select()
        selectionner_reponse("r10")
        radio2.deselect()
        radio1.grid(row=0, column=0)
        radio2.grid(row=0, column=1)
        okbutton = Button(reponse_canvas, text="OK", command=traiter_reponse)
        # columnspan est un paramètre qui permet d'étendre le widget à plusieurs colonnes
        okbutton.grid(row=1, column=0, columnspan=2)
    elif message_a_afficher == 21.5:
        ligne_message += 1
        Label(fr, text="Pierre m'a dit qu'après être allé chez lui, Kevin est allé voir Melina", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        supprimer_widget(reponse_canvas)
        message_a_afficher = 104
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 22:
        ligne_message += 1
        Label(fr, text="J'ai croisé un homme dans la rue, il dit qu'il sait où est Kevin. Je fais quoi?", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        supprimer_widget(reponse_canvas)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 23:
        reponse = StringVar()
        radio1 = Radiobutton(reponse_canvas, text=liste_reponse["r12"], variable=reponse, value="r1", command=lambda: selectionner_reponse("r12"), wraplength=wraplength)
        radio2 = Radiobutton(reponse_canvas, text=liste_reponse["r13"], variable=reponse, value="r2", command=lambda: selectionner_reponse("r13"), wraplength=wraplength)
        radio1.select()
        selectionner_reponse("r12")
        radio2.deselect()
        radio1.grid(row=0, column=0)
        radio2.grid(row=0, column=1)
        okbutton = Button(reponse_canvas, text="OK", command=traiter_reponse)
        # columnspan est un paramètre qui permet d'étendre le widget à plusieurs colonnes
        okbutton.grid(row=1, column=0, columnspan=2)
    elif message_a_afficher == 24:
        # PARTIE PERDUE
        ligne_message += 1
        Label(fr, text="L'homme m'a conduit à un garçon nommé Kevin. Mais ça n'est pas notre Kevin.", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 25:
        # PARTIE PERDUE
        ligne_message += 1
        Label(fr, text="Oh non...j'y ai tellement cru...", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 26:
        # PARTIE PERDUE
        ligne_message += 1
        Label(fr, text="Oh non Paul, mon dieu...", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 27:
        # PARTIE PERDUE
        ligne_message += 1
        Label(fr, text="Quoi? Qu'est-ce qu'il y a?", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 28:
        # PARTIE PERDUE
        ligne_message += 1
        Label(fr, text="J'ai reçu un appel, le corps de Kevin a été retrouvé par un passant, une balle dans la poitrine.", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        supprimer_widget(reponse_canvas)
        Button(reponse_canvas, text="Rejouer", command=rejouer).grid(row=1, column=0)
        Button(reponse_canvas, text="Quitter", command=quitter).grid(row=1, column=1)
    elif message_a_afficher == 100:
        ligne_message += 1
        Label(fr, text="J’ai trouvé un post-it sur lequel il y a marqué \"samedi 14h rdv avec Pierre\" il habite pas loin j’y vais ", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 101:
        ligne_message += 1
        Label(fr, text="Ok demande lui s’il est au courant d’un truc qui aurait un lien avec la disparition de Kevin", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 102:
        ligne_message += 1
        Label(fr, text="Je viens de le faire . Il m’a dit qu’il avait entendu quelqu’un dire \"si dimanche 18h30, Kevin ne nous l’a pas donné, on l’élimine\" Par contre il ne sait rien d’autre et le temps presse. Je vais où ?", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 103:
        reponse = StringVar()
        radio1 = Radiobutton(reponse_canvas, text=liste_reponse["r4"], variable=reponse, value="r1", command=lambda: selectionner_reponse("r4"), wraplength=wraplength)
        radio2 = Radiobutton(reponse_canvas, text=liste_reponse["r5"], variable=reponse, value="r2", command=lambda: selectionner_reponse("r5"), wraplength=wraplength)
        radio1.select()
        selectionner_reponse("r4")
        radio2.deselect()
        radio1.grid(row=0, column=0)
        radio2.grid(row=0, column=1)
        okbutton = Button(reponse_canvas, text="OK", command=traiter_reponse)
        # columnspan est un paramètre qui permet d'étendre le widget à plusieurs colonnes, ici on veut le centrer
        okbutton.grid(row=1, column=0, columnspan=2)
    elif message_a_afficher == 104:
        ligne_message +=1
        Label(fr, text="ça y est je suis devant chez Melina, mais elle ne répond pas. Y a de la lumière à l’intérieur, je fais quoi ?", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 105:
        reponse = StringVar()
        radio1 = Radiobutton(reponse_canvas, text=liste_reponse["r8"], variable=reponse, value="r1", command=lambda: selectionner_reponse("r8"), wraplength=wraplength)
        radio2 = Radiobutton(reponse_canvas, text=liste_reponse["r9"], variable=reponse, value="r2", command=lambda: selectionner_reponse("r9"), wraplength=wraplength)
        radio1.select()
        selectionner_reponse("r8")
        radio2.deselect()
        radio1.grid(row=0, column=0)
        radio2.grid(row=0, column=1)
        okbutton = Button(reponse_canvas, text="OK", command=traiter_reponse)
        # columnspan est un paramètre qui permet d'étendre le widget à plusieurs colonnes
        okbutton.grid(row=1, column=0, columnspan=2)
    elif message_a_afficher== 106:
        ligne_message += 1
        Label(fr, text="Ok je passe dans la rue derrière, purée, je vois un truc, on dirait le gant que j’ai offert à Kevin. Y a deux personnes dans la rue, je vais les interroger", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength ).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher== 107:
        ligne_message += 1
        Label(fr, text="Et alors ?", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher== 108:
        ligne_message += 1
        Label(fr, text="Mme Peletier dit qu’elle a aperçu un jeune Homme poursuivi par deux autres personnes et Camilia affirme qu’elle a vu Kevin marchait seul. A ton avis, laquelle ment ?", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher== 109:
        reponse = StringVar()
        radio1 = Radiobutton(reponse_canvas, text=liste_reponse["r14"], variable=reponse, value="r1", command=lambda: selectionner_reponse("r14"), wraplength=wraplength)
        radio2 = Radiobutton(reponse_canvas, text=liste_reponse["r15"], variable=reponse, value="r2", command=lambda: selectionner_reponse("r15"), wraplength=wraplength)
        radio1.select()
        selectionner_reponse("r14")
        radio2.deselect()
        radio1.grid(row=0, column=0)
        radio2.grid(row=0, column=1)
        okbutton = Button(reponse_canvas, text="OK", command=traiter_reponse)
        # columnspan est un paramètre qui permet d'étendre le widget à plusieurs colonnes, ici on veut le centrer
        okbutton.grid(row=1, column=0, columnspan=2)
    elif message_a_afficher== 110:
        ligne_message += 1
        Label(fr, text="Ok j’ai interrogé Mme Peletier et elle a dit la même chose", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 111:
        # PARTIE PERDUE
        ligne_message += 1
        Label(fr, text="Oh non Paul, mon dieu...", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 112:
        # PARTIE PERDUE
        ligne_message += 1
        Label(fr, text="Quoi? Qu'est-ce qu'il y a?", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 113:
        # PARTIE PERDUE
        ligne_message += 1
        Label(fr, text="J'ai reçu un appel, le corps de Kevin a été retrouvé par un passant, une balle dans la poitrine.", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        supprimer_widget(reponse_canvas)
        Button(reponse_canvas, text="Rejouer", command=rejouer).grid(row=1, column=0)
        Button(reponse_canvas, text="Quitter", command=quitter).grid(row=1, column=1)
    elif message_a_afficher == 114:
        ligne_message += 1
        Label(fr, text="Ok je vais la réinterroger du coups pour tenter d'en apprendre plus", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 115:
        ligne_message += 1
        Label(fr, text="ça n'a pas été facile mais elle a fini par me parler. Elle savait que Calvin et Adam en voulait à Kevin et a donc voulu couvrir Adam au cas où il se passerait quelque chose. Mais elle n'imaginait pas qu'ils pourraient s'en prendre à lui... Quand je lui ai parlé, elle a réalisé la gravité de la situation. Elle m'a dit que Calvin et Adam avait parlé d'un hangard à 100 mètres d'ici", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 116:
        #partie gagnée
        ligne_message += 1
        Label(fr, text="super !", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 117:
        #partie gagnée
        ligne_message += 1
        Label(fr, text="Kevin est là Paul!!! On a réussi, merci bp pour ton aide !", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        supprimer_widget(reponse_canvas)
        Button(reponse_canvas, text="Rejouer", command=rejouer).grid(row=1, column=0)
        Button(reponse_canvas, text="Quitter", command=quitter).grid(row=1, column=1)


    elif message_a_afficher == 118:
        ligne_message += 1
        Label(fr, text="J’ai bien fait de rentrer, elle me dit que Kevin vendait un produit dopant et qu’il ne voulait pas le vendre à Adam et Calvin. ", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 119:
        ligne_message += 1
        Label(fr, text="Ok, demande à Camila ce qu’elle sait, elle est proche de Adam.", borderwidth=2, relief="ridge", bg="pale green", wraplength=wraplength).grid(row=ligne_message, column=1, sticky=E)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 120 :
        ligne_message += 1
        Label(fr, text="Elle dit qu’elle ne sait rien, qu'est ce que je fais ?", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        message_a_afficher += 1
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
    elif message_a_afficher == 121:
        reponse = StringVar()
        radio1 = Radiobutton(reponse_canvas, text=liste_reponse["r16"], variable=reponse, value="r1", command=lambda: selectionner_reponse("r16"), wraplength=wraplength)
        radio2 = Radiobutton(reponse_canvas, text=liste_reponse["r17"], variable=reponse, value="r2", command=lambda: selectionner_reponse("r17"), wraplength=wraplength)
        radio1.select()
        selectionner_reponse("r16")
        radio2.deselect()
        radio1.grid(row=0, column=0)
        radio2.grid(row=0, column=1)
        okbutton = Button(reponse_canvas, text="OK", command=traiter_reponse)
        # columnspan est un paramètre qui permet d'étendre le widget à plusieurs colonnes, ici on veut le centrer
        okbutton.grid(row=1, column=0, columnspan=2)
    elif message_a_afficher == 122:
        ligne_message += 1
        Label(fr, text="Elle a dit qu'elle avait vu un jeune homme se faire poursuivre par deux autres dans sa rue. Ils l'ont ensuite attrappé et sont rentrés dans un hangar. Elle m'a montré où il était, j'y vais.", borderwidth=2, relief="ridge", bg="white", wraplength=wraplength).grid(row=ligne_message, column=0, sticky=W)
        fenetre_principal.after(intervalle_temps, affichage_dialogue)
        message_a_afficher = 116

    # Mise à jour de la frame
    fr.update_idletasks()
    message_canvas.config(scrollregion=message_canvas.bbox("all"))
    message_canvas.yview_moveto(1)

def jeu_principal(fenetre_accueil):
    global width, height, fr, reponse_canvas, message_canvas, fenetre_principal, fenetre_demarrage

    fenetre_principal = Tk()

    fenetre_principal.wm_minsize(width, height)
    #fenetre_principal.wm_maxsize(500, 600)
    fenetre_principal.wm_title("Interface messages")

    #Afficher le nom du contact
    nomContact = Label(fenetre_principal, text="Rose", bg="white")
    nomContact.grid(row=0, column=0)

    #création d'une barre de défilement
    barre_defiler = Scrollbar(fenetre_principal, orient=VERTICAL)
    #création d'un canvas pour mettre la frame des message
    message_canvas=Canvas(fenetre_principal, width=width, height=height - 100)

    # Lorsque le contenu dépasse la scrollbar va permettre de faire défiler le contenu qui dépasse
    barre_defiler.config(command=message_canvas.yview)
    message_canvas.config(yscrollcommand=barre_defiler.set)

    message_canvas.grid(row=1, column=0)
    barre_defiler.grid(row=1, column=1, sticky=N+S)

    fr = Frame(message_canvas, width=width, height=height - 100)

    fenetre_principal.grid_rowconfigure(1, weight=1)
    fenetre_principal.grid_columnconfigure(0, weight=1)

    # méthode pour mettre en place le scrollbar
    message_canvas.create_window(0, 0, window=fr)
    # définition du scroll pour faire défiler les widgets dans le canvas, placer pour que les messages soient placés au milieu de la frame
    message_canvas.configure(scrollregion=message_canvas.bbox("all"))

    #création d'un cadre pour insérer les choix de réponse (un cadre principale, un cadre par serie de choix de réponses
    reponse_canvas = Canvas(fenetre_principal, width=width, height=100)
    reponse_canvas.grid(row=2, column=0)

    # affichage des messages après 500ms
    fenetre_principal.after(250, affichage_dialogue)

    fenetre_principal.mainloop()