from tkinter import *
import sys
import gen_fief
import random
from village import Village
from liste_hab_village import village as liste_habitants
from roturiers import Paysan, Artisan
from noble import Noble
from gen_fief import positions
from eccleastique import Ecclesiastique

global chemin_images 
global root
global Villages_possibles 
global village_positions

################## DICTIONNAIRES ET RESSOURCES UTILISES  ##################

village_positions = {}  # Dictionnaire pour stocker les positions disponibles avec leurs coordonnées
Village_cree = {}
Village_infos = {}

chemin_images = {
    "village": "../res/terrain_map/Village.png"
}

Villages_possibles = {
    "village_1": "../res/terrain_map/village_1.png",
    "village_2": "../res/terrain_map/village_2.png",
    "village_3": "../res/terrain_map/village_3.png",
    "village_4": "../res/terrain_map/village_4.png",
    "village_5": "../res/terrain_map/village_5.png",
    "village_6": "../res/terrain_map/village_6.png"
}

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, string):
        self.widget.configure(state="normal")
        self.widget.insert("end", string, (self.tag,))
        self.widget.see("end")  
        self.widget.configure(state="disabled")

    def flush(self):
        pass  

class Tour:
    def __init__(self):
        self.phase_1 = 0  # État de la phase 1 (événement aléatoire)
        self.phase_2 = 0  # État de la phase 2 (action seigneur)
        self.phase_3 = 0  # État de la phase 3 (réactions)
        self.phase_4 = 0  # État de la phase 4 (fin de tour)

tour = Tour()

def MAJ_ACT():
    act_label.config(text=f"{act_actuel}/{act_max}")
##################  DIFFERENTS MENUS  ##################

def Menu_tour():
    clear_frame(button_frame)
    button_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)  # Place les boutons à droite
    # Phase 1
    Button(
        button_frame,
        text="❌ Phase 1" if tour.phase_1 == 0 else "✅ Phase 1",  # Ajout de la virgule ici
        font=("Courrier", 10),
        bg='white',
        fg='black',
        width=20,
        height=2,
        command=event_aleatoire
    ).pack(pady=5, padx=15, fill=X)

    # Phase 2
    Button(
        button_frame,
        text="❌ Phase 2" if tour.phase_2 == 0 else "✅ Phase 2",  # Ajout de la virgule ici
        font=("Courrier", 10),
        bg='white',
        fg='black',
        width=20,
        height=2,
        command=Menu_Action_1
    ).pack(pady=5, padx=15, fill=X)

    # Phase 3
    Button(
        button_frame,
        text="❌ Phase 3" if tour.phase_3 == 0 else "✅ Phase 3",  # Ajout de la virgule ici
        font=("Courrier", 10),
        bg='white',
        fg='black',
        width=20,
        height=2,
        command=phase_3
    ).pack(pady=5, padx=15, fill=X)

    # Phase 4
    Button(
        button_frame,
        text="❌ Phase 4" if tour.phase_4 == 0 else "✅ Phase 4",  # Ajout de la virgule ici
        font=("Courrier", 10),
        bg='white',
        fg='black',
        width=20,
        height=2,
        command=reset_tour
    ).pack(pady=10, padx=15, fill=X)

    # Bouton Quitter
    Button(
        button_frame,
        text="Quitter",
        font=("Arial", 10),
        bg='white',
        fg='black',
        width=20,
        height=2,
        command=menu_window.quit
    ).pack(pady=10, padx=15, side=RIGHT)

def Menu_Action_1(): #Menu d'action general 

    if  (tour.phase_1 ==1 and tour.phase_2 == 0) :

        clear_frame(button_frame)

        Button(
            button_frame,
            text="Ressources humaines",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command=Menu_RH 
        ).pack(pady=10, padx=15, fill=X)

        Button(
            button_frame,
            text="Construire",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command=Menu_village
        ).pack(pady=10, padx=15, fill=X)

        Button(
            button_frame,
            text="Taxes",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command=Menu_Argent 
        ).pack(pady=10, padx=15, fill=X)

        Button(
            button_frame,
            text="Bagarre",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command=Menu_Bagarre 
        ).pack(pady=10, padx=15, fill=X)

        Button(
            button_frame,
            text="Rien faire",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command= Rien_faire
        ).pack(pady=10, padx=15, fill=X)

        Button(
            button_frame,
            text="Retour",
            font=("Arial", 7),
            bg='white',
            fg='black',
            command=Menu_tour      
        ).pack(pady=15, padx=20, side=RIGHT)

        Button(
            button_frame,
            text="Quitter",
            font=("Arial", 10),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command=menu_window.quit
        ).pack(pady=10, padx=15, side=RIGHT)
    else :
        print("Erreur phase retour menu précedent")
        Menu_tour()

def Menu_RH():    
    if  (tour.phase_1 ==1 and tour.phase_2 == 0) :
        clear_frame(button_frame)

        Button(
            button_frame,
            text="Immigration",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command= Immigration
        ).pack(pady=10, padx=15, fill=X)


        Button(
            button_frame,
            text="Recruter Soldats",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command= Recruter_Soldats
        ).pack(pady=10, padx=15, fill=X)


        Button(
            button_frame,
            text="Retour",
            font=("Arial", 7),
            bg='white',
            fg='black',
            command=Menu_tour      
        ).pack(pady=15, padx=20, side=RIGHT)

        Button(
            button_frame,
            text="Quitter",
            font=("Arial", 10),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command=menu_window.quit
        ).pack(pady=10, padx=15, side=RIGHT)

def Menu_Bagarre():    
    if  (tour.phase_1 ==1 and tour.phase_2 == 0) :
        clear_frame(button_frame)

        Button(
            button_frame,
            text="Bataille",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command= Guerre
        ).pack(pady=15, padx=15, fill=X)

        Button(
            button_frame,
            text="Retour",
            font=("Arial", 7),
            bg='white',
            fg='black',
            command=Menu_tour      
        ).pack(pady=15, padx=20, side=RIGHT)

        Button(
            button_frame,
            text="Quitter",
            font=("Arial", 10),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command=menu_window.quit
        ).pack(pady=10, padx=15, side=RIGHT)

def Menu_Argent():    
    if  (tour.phase_1 ==1 and tour.phase_2 == 0) :
        clear_frame(button_frame)

        Button(
            button_frame,
            text="Impots",
            font=("Courrier", 9),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command= Impots
        ).pack(pady=10, padx=15, fill=X)

        Button(
            button_frame,
            text="Retour",
            font=("Arial", 7),
            bg='white',
            fg='black',
            command=Menu_tour      
        ).pack(pady=15, padx=20, side=RIGHT)

        Button(
            button_frame,
            text="Quitter",
            font=("Arial", 10),
            bg='white',
            fg='black',
            width=20,
            height=2,
            command=menu_window.quit
        ).pack(pady=10, padx=15, side=RIGHT)

def Menu_village():
    if  (tour.phase_1 ==1 and tour.phase_2 == 0) :

        clear_frame(button_frame)

        MAJ_village_positions()
        
        for position_ind in village_positions.keys():  # Parcourt les positions disponibles
            Button(
                button_frame,
                text=f"Construire village à {position_ind}",
                font=("Courrier", 7),
                bg='white',
                fg='black',
                width=20,
                height=2,
                command=lambda ind=position_ind: construire_village(ind)
            ).pack(pady=10, padx=15, fill=X)


        Button(
            button_frame,
            text="Retour",
            font=("Arial", 7),
            bg='white',
            fg='black',
            command=Menu_tour      
        ).pack(pady=15, padx=20, side=RIGHT)
    else :
        print("Phase déjà terminé une action a déjà été réalisée \n")


#J'ai besoin d'une variable stockant la position du village (s'il est dans la bibilothèque alors il est crée) ainsi que son image (il me faudrait aussi des caracteriques eglise ou pas..)
def assigner_villages(position_ind):
    global Liste_villages, Village_cree

    Liste_villages = {
        1: "../res/terrain_map/village_1.png",
        2: "../res/terrain_map/village_2.png",
        3: "../res/terrain_map/village_3.png",
        4: "../res/terrain_map/village_4.png",
        5: "../res/terrain_map/village_5.png",
        6: "../res/terrain_map/village_6.png",
    }

    # Générer une clé aléatoire

    village_choisi_ind = random.randint(1, len(Liste_villages))
    village_chemin_images = Liste_villages[village_choisi_ind]

    # Mettre à jour Village_cree
    Village_cree[position_ind] = {
        "image_ind": village_choisi_ind,
        "chemin_images": village_chemin_images
    }

    print(f"Village à {position_ind} assigné avec l'image {village_choisi_ind} ({village_chemin_images}).")
    return village_chemin_images


def MAJ_village_positions():

    global village_positions
    village_positions.clear()  # Réinitialiser le dictionnaire avant mise à jour

    for pos, val in gen_fief.terrain_actif.items():
        if val == 1:  # Si la position est disponible
            village_positions[pos] = gen_fief.positions[pos]  # Ajout au dictionnaire

MAJ_village_positions()

##################  PHASE 1  ##################
def event_aleatoire():
    if  (tour.phase_1 == 0) :
        evenement_alea = random.randint(1, 100)
        if  (evenement_alea >= 1 and evenement_alea <= 5) :
            epidemmie 
        elif (evenement_alea >= 6 and evenement_alea <= 10):
            incendie
        elif (evenement_alea >= 11 and evenement_alea <= 20):
            pillage
        elif  (evenement_alea >= 21 and evenement_alea <= 40):
            famine
        elif (evenement_alea >= 41 and evenement_alea <= 64) :
            print("Rien ne se passe \n")
        elif (evenement_alea >= 65 and evenement_alea <= 84):
            Recolte(5,5)
        elif (evenement_alea >= 85 and evenement_alea <= 94):
            Immigration
        elif ((evenement_alea >= 95 and evenement_alea <= 99)):
            print("Rien ne se passe \n")
        else :
            print("J'ai pas d'inspi pour celui-là \n")

        tour.phase_1 = 1 
        Menu_tour()
    else :
        print("Event déjà réalisé, passez à la phase suivante")

def epidemmie():
    for position, village in Village_infos.items():  
        village.habitants = village.habitants[:len(village.habitants) - 6]
    print("Une épidemie a eu lieu des villageois sont morts \n")

def incendie():
    position_ind = random.choice(list(Village_infos.keys()))

    village_detruit = Village_infos[position_ind]
    del Village_infos[position_ind]

    print(f"Un incendie a eu lieu ! Le village {position_ind} a disparu\n")

def pillage():
    for position, village in Village_infos.items():  # Pour chaque village présent dans le fief
        ressources_disparues = 6
        argent_disparu = 6

    for habitant in village.habitants:
            habitant.ressources -= ressources_disparues 
            habitant.argent -= argent_disparu 
            habitant.humeur -=1
    print("Il y a eu un pillage dee l'or et des ressources ont été dérobées \n")

def famine():
    for position, village in Village_infos.items():  # Pour chaque village présent dans le fief
        ressources_disparues = 6

    for habitant in village.habitants:
            habitant.ressources -= ressources_disparues 
            habitant.argent += argent_obtenu + bonus_argent
            habitant.humeur -=1
    print("C'est la famine,les ressources commencent à manquer \n")


################## PHASE 2 ##################



def Rien_faire():    
        tour.phase_2 = 1
        Menu_tour()


def Recruter_Soldats():
    global act_actuel

    if act_actuel <= 1: #Verif
        print("ACT insuffisants !")
        return

    clear_frame(button_frame)

    print("Choisir un village pour y recruter des soldats :\n")

    # Afficher uniquement les villages où terrain_actif == 3
    for position_ind, val in gen_fief.terrain_actif.items():
        if val == 3:  # Si un village est présent
            Button(
                button_frame,
                text=f"Recruter soldats ({position_ind})",
                font=("Courrier", 9),
                bg='white',
                fg='black',
                width=25,
                height=2,
                command=lambda ind=position_ind: Realiser_Recrutement(ind)
            ).pack(pady=10, padx=20, fill=X)

    # Bouton de retour
    Button(
        button_frame,
        text="Retour",
        font=("Arial", 7),
        bg='white',
        fg='black',
        command=Menu_RH
    ).pack(pady=10, padx=15, side=RIGHT)


def Realiser_Recrutement(position_ind):
    global act_actuel

    print("Village_infos :", Village_infos)
    print("terrain_actif :", gen_fief.terrain_actif)

    village = Village_infos[position_ind]
    
    village.recruter_soldats(nombre_soldats=5) 

    print(f"Recrutement de 5 soldats pour {village.nom}.")
    act_actuel -= 1
    MAJ_ACT()
    tour.phase_2 = 1
    Menu_tour()


def Immigration():
    global act_actuel
    clear_frame(button_frame)

    if act_actuel <= 1: #Verif
        print("ACT insuffisants !")
        return    

    print("Choisir un village pour réaliser l'immigration :\n")

    # Afficher uniquement les villages où terrain_actif == 3
    for position_ind, val in gen_fief.terrain_actif.items():
        if val == 3:  # Si un village est présent
            Button(
                button_frame,
                text=f"Immigrer au village ({position_ind})",
                font=("Courrier", 9),
                bg='white',
                fg='black',
                width=25,
                height=2,
                command=lambda ind=position_ind: Realiser_immigration(ind)
            ).pack(pady=10, padx=15, fill=X)

    # Bouton de retour
    Button(
        button_frame,
        text="Retour",
        font=("Arial", 7),
        bg='white',
        fg='black',
        command=Menu_RH
    ).pack(pady=10, padx=15, side=RIGHT)


def Realiser_immigration(position_ind):
    global act_actuel
    village = Village_infos[position_ind]
    village.immigrer()
    print(f"Immigration réalisée pour village {village.nom}.")
    act_actuel -= 1
    MAJ_ACT()
    tour.phase_2 = 1
    Menu_tour()


def Guerre():
    #Le principe de guerre a été grandement simplifié ici
    #On ne combat pas un bot et l'issue du combat est determiné selon des probabilitée
    #Cependant les conséquences restent les mêmes : Victoire -> Gain / Defaite -> Perte 
    global act_actuel
    clear_frame(button_frame)

    if act_actuel <= 2: #Verif
        print("ACT insuffisants !")
        return    

    print("Choisir un village qui fera la guerre :\n")

    # Afficher uniquement les villages où terrain_actif == 3
    for position_ind, val in gen_fief.terrain_actif.items():
        if val == 3:  # Si un village est présent
            Button(
                button_frame,
                text=f"Village faisant la guerre : ({position_ind})",
                font=("Courrier", 7),
                bg='white',
                fg='black',
                width=25,
                height=2,
                command=lambda ind=position_ind: Realiser_Guerre(ind)
            ).pack(pady=15, padx=15, fill=X)

    # Bouton de retour
    Button(
        button_frame,
        text="Retour",
        font=("Arial", 7),
        bg='white',
        fg='black',
        command=Menu_RH
    ).pack(pady=10, padx=15, side=RIGHT)


def Realiser_Guerre(position_ind):
    global act_actuel
    #On recupere le nombre de soldats de l'armée du village 

    village = Village_infos[position_ind]
    print(f"Village {village.nom} entre en guerre avec {village.armee_village} soldats.\n")

    #Ensuite un bref calcul tel que <nombre_soldat>/50 = % de victoire

    issue_guerre = 0

    ressources_gagnees = 0
    argent_gagnees =0
    ressources_perdues = 0
    argent_perdus = 0  

    proba_victoire = (village.armee_village/50) #100 aurait été trop -> besoin de bcp de soldats donc bcp de tour à recruter 
    print(f"Debug proba_victoire = {proba_victoire}")

    if (proba_victoire < 0.5): 
        issue_guerre = 0
    else : 
        issue_guerre = 1  
    print(f"Debug issue_guerre = {issue_guerre}")

    #Si victoire alors gain de ressources et d'argent total du village
    #Si defaite alors 50% de chances de perdre ressources et argent total du village et 50% d'avoir le village détruit 
    
    if issue_guerre == 1 :   
        ressources_gagnees = random.randint(5, 20)
        argent_gagnes = random.randint(5, 20)
        print("Victoire ! \n")
        print(f"Gain de {ressources_gagnees} ressources et {argent_gagnes} or\n")

        for habitant in village.habitants:
            habitant.ressources += ressources_gagnees // len(village.habitants)
            habitant.argent += argent_gagnes // len(village.habitants)

    
    if issue_guerre == 0 : 

        Destin = random.randint(0, 4) # 0 -> Destruction, les autres uniquement pertes

        if Destin == 0 :
            del Village_infos[position_ind]
            print("Pas de chance c'est la fin du village :( \n)")
        else : 
            ressources_perdues = random.randint(5, 20)
            argent_perdus = random.randint(5, 20)
            for habitant in village.habitants:
                habitant.ressources = max(habitant.ressources - (ressources_perdues // len(village.habitants)), 1)
                habitant.argent = max(habitant.argent - (argent_perdus // len(village.habitants)), 1)
        print(f"Perte de {ressources_perdues} ressources et {argent_perdus} or\n")

        act_actuel -= 2
        MAJ_ACT()
        tour.phase_2 = 2
        Menu_tour()
 
def Impots():

    global act_actuel
    clear_frame(button_frame)

    if act_actuel <= 2: #Verif
        print("ACT insuffisants !")
        return    

    print("Choisir un village a imposer :\n")

    for position_ind, val in gen_fief.terrain_actif.items():
        if val == 3:  # Si un village est présent
            Button(
                button_frame,
                text=f"Imposer au village : ({position_ind})",
                font=("Courrier", 7),
                bg='white',
                fg='black',
                width=25,
                height=2,
                command=lambda ind=position_ind: Realiser_Impots(ind)
            ).pack(pady=15, padx=15, fill=X)

    # Bouton de retour
    Button(
        button_frame,
        text="Retour",
        font=("Arial", 7),
        bg='white',
        fg='black',
        command=Menu_RH
    ).pack(pady=10, padx=15, side=RIGHT)

def Realiser_Impots(position_ind):
    global act_actuel

    village = Village_infos[position_ind]
    print(f"Village {village.nom} entre en guerre avec {village.armee_village} soldats.\n")


# Efface les widgets pour un nouveau menu
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def construire_village(position_ind):
    global act_actuel, village_positions, chemin_images, Village_cree, info_village

    MAJ_village_positions()

    print("##############\n")
    print("Villages positions :", village_positions)
    print("##############\n")

    if position_ind not in village_positions: #Verif
        print(f"Erreur : {position_ind} n'est pas une position disponible.")
        return

    if gen_fief.terrain_actif[position_ind] == 3: #Verif
        print(f"Un village est déjà actif à {position_ind}.\n")
        return

    if act_actuel <= 5: #Verif
        print("ACT insuffisants !")
        return

    # Récupération des coordonnées du village
    x, y = village_positions[position_ind]

    #On crée le village 
    Village_infos[position_ind] = Village(1, f"Village à {position_ind}", x, y)

    for habitant_nom, habitant_data in liste_habitants.items():
        if "Paysan" in habitant_nom:  
            statut, age, edv = habitant_data
            Village_infos[position_ind].ajouter_habitant(Paysan(habitant_nom, age, edv))
        elif "Artisan" in habitant_nom:  
            age, edv = habitant_data
            Village_infos[position_ind].ajouter_habitant(Artisan(habitant_nom, age, edv))
        elif "Noble" in habitant_nom:  
            age, argent = habitant_data
            Village_infos[position_ind].ajouter_noble(Noble(habitant_nom, age, argent))

    Village_infos[position_ind].ajouter_ecclesiastique()
    Village_infos[position_ind].ajouter_noble(liste_habitants["Noble1"])

    print("DEBUG- MAJ Village_infos dico :",Village_infos)

    # On ajoute le village sur la carte
    Village_cree[position_ind] = gen_fief.canvas.create_image(x, y, image=gen_fief.Village_image, anchor=CENTER, tags="village") 

    gen_fief.terrain_present(position_ind, 3) #Met à jour le fief -> Un village est désormais présent ici

    print("Debug - MAJ Village_cree dico :",Village_cree)
    
    assigner_villages(position_ind)

    Village_infos[position_ind].eglise = True  

    # Coup d'actions utilisé et donc mis à jour 
    act_actuel -= 5
    MAJ_ACT()
    tour.phase_2 = 1

    print(f"Village construit à {position_ind}.\n")
    Menu_tour()

# Menu principal
def reset_tour ():
    global act_actuel
    if  (tour.phase_1 ==1 and tour.phase_2 == 1 and tour.phase_3 == 1) :
        print("phase 4 OK -> RESET !\n")
        tour.phase_1 = 0
        tour.phase_2 = 0
        tour.phase_3 = 0
        act_actuel += 1
        Recolte(5,5)
        MAJ_ACT()
        print("ACT augmenté !\n")
        print("############\n")
        print("Nouveau tour ! \n")
        print("############")
        Menu_tour()


    else :
        print("Erreur phase")
        Menu_tour()

def Recolte(ressources_recolte, argent_obtenu):

    for position, village in Village_infos.items():  # Pour chaque village présent dans le fief
        bonus_ressources = 0
        bonus_argent = 0

        # Si on a le don augmentation_production
        for habitant in village.habitants:
            if isinstance(habitant, Ecclesiastique) and habitant.don == "augmentation_production":
                bonus_ressources = 3
                bonus_argent = 3
                print(f"Bonus appliqué : Ecclésiastique avec 'augmentation_production' dans le village {village.nom}.")
                break  
        # Recolte avec potentiel bonus
        for habitant in village.habitants:
            habitant.ressources += ressources_recolte + bonus_ressources
            habitant.argent += argent_obtenu + bonus_argent
            habitant.humeur += 1
    print("Fin du tour -> La récolte a eu lieu\n")



def phase_3():
    if  (tour.phase_1 ==1 and tour.phase_2 == 1 and tour.phase_3 == 0) :
        print("phase 3 OK !\n")
        tour.phase_3 = 1 
        Menu_tour()
    else :
        print("Erreur phase")
        Menu_tour()

#Ouvre la map sur laquelle on peut voir le fief
def open_map_window():
    global canvas_map

    map_window = Toplevel(root)
    map_window.title("Carte Fief")
    map_window.geometry("380x380")

    # Initialise le Canvas dans gen_fief
    gen_fief.init_fief(map_window)

    canvas_map = gen_fief.canvas

    gen_fief.generate_fief()

    canvas_map.tag_bind("village", "<Button-1>", on_canvas_click)
    print("Clic droit lié à canvas_map.")

#Ouvre le menu des actions
def open_menu_window() : 
    
    global menu_window, canvas, button_frame, village_image, act_label, act_actuel, act_max

    menu_window = Toplevel(root)  # Crée une nouvelle fenêtre
    menu_window.title("Menu Fief")
    menu_window.geometry("600x450")
    menu_window.config(background="#25b3c9")
    menu_window.maxsize(600, 450)
    menu_window.minsize(600, 450)

    frame = Frame(menu_window, bg="grey")
    frame.pack(side=TOP, fill=BOTH, expand=YES)

    output_text = Text(frame, wrap=WORD, width=40, height=20, bg="white", fg="black")
    output_text.pack(side=RIGHT, fill=Y, padx=10, pady=10)
    sys.stdout = TextRedirector(output_text)

    act_actuel = 8
    act_max = 8
    act_frame = Frame(frame, bg="#25b3c9")
    act_frame.place(x=210, y=10)
    act_label = Label(act_frame, text=f"{act_actuel}/{act_max}", font=("Courrier", 14), bg="#25b3c9", fg="white")
    act_label.pack()

    button_frame = Frame(frame, bg="#25b3c9")
    button_frame.pack(side=BOTTOM, fill=X)

    print("\n\n")
    Menu_tour()

# Associe la position sur le fief à la position du village pour le clic 
def definir_position (x,y):
    if ((x >= 30 and x < 110) and ((y >= 30) and (y < 110))):
        return ("Position 1")
    if ((x >= 110 and x < 190) and ((y >= 30) and (y < 110))):
        return ("Position 2")
    if ((x >= 190 and x < 270) and ((y >= 30) and (y < 110))):
        return ("Position 3")
    if ((x >= 270 and x < 350) and ((y >= 30) and (y < 110))):
        return ("Position 4")
    if (x >= 350  and ((y >= 30) and (y < 110))):
        return ("Position 5")
    ####
    if ((x >= 30 and x < 110) and ((y >= 110) and (y < 190))):
        return ("Position 6")
    if ((x >= 110 and x < 190) and ((y >= 110) and (y < 190))):
        return ("Position 7")
    if ((x >= 190 and x < 270) and ((y >= 110) and (y < 190))):
        return ("Position 8")
    if ((x >= 270 and x < 350) and ((y >= 110) and (y < 190))):
        return ("Position 9")
    if (x >= 350  and ((y >= 110) and (y < 190))):
        return ("Position 10")
    ####
    if ((x >= 30 and x < 110) and ((y >= 190) and (y < 270))):
        return ("Position 11")
    if ((x >= 110 and x < 190) and ((y >= 190) and (y < 270))):
        return ("Position 12")
    if ((x >= 190 and x < 270) and ((y >= 190) and (y < 270))):
        return ("Position 13")
    if ((x >= 270 and x < 350) and ((y >= 190) and (y < 270))):
        return ("Position 14")
    if (x >= 350  and ((y >= 190) and (y < 270))):
        return ("Position 15")
    ####
    if ((x >= 30 and x < 110) and ((y >= 270) and (y < 350))):
        return ("Position 16")
    if ((x >= 110 and x < 190) and ((y >= 270) and (y < 350))):
        return ("Position 17")
    if ((x >= 190 and x < 270) and ((y >= 270) and (y < 350))):
        return ("Position 18")
    if ((x >= 270 and x < 350) and ((y >= 270) and (y < 350))):
        return ("Position 19")
    if (x >= 350  and ((y >= 270) and (y < 350))):
        return ("Position 20")
    ####
    if ((x >= 30 and x < 110) and (y >= 350)):
        return ("Position 21")
    if ((x >= 110 and x < 190) and (y >= 350)):
        return ("Position 22")
    if ((x >= 190 and x < 270) and (y >= 350)):
        return ("Position 23")
    if ((x >= 270 and x < 350) and (y >= 350)):
        return ("Position 24")
    if (x >= 350  and (y >= 350)):
        return ("Position 25")
    ####

def on_canvas_click(event):
    global canvas_map
    print("Debug - on_canvas_click déclenché")
    
    item = canvas_map.find_closest(event.x, event.y)
    tags = canvas_map.gettags(item)
    print(f"Élément cliqué : {item}, Tags : {tags}")
    
    p = definir_position(event.x, event.y)

    if "village" in tags:
        print(f"Village cliqué : {item}")
        afficher_image_village(p)
    else:
        print("Clic sur une zone non définie.")


def afficher_image_village(position_ind): 
    # On verifie que le village existe 
    if position_ind not in Village_cree:
        print(f"Aucun village trouvé à la position {position_ind}")
        return

    if position_ind not in Village_infos:
        print(f"Aucune information trouvée pour le village à {position_ind}")
        return

    village = Village_infos[position_ind]
    chemin_images = Village_cree[position_ind]["chemin_images"]

    total_ressources = village.somme_ressources()
    total_argent = village.somme_argent()

    display_window = Toplevel()
    display_window.title(f"Village à {position_ind}")
    display_window.geometry("720x480")
    display_window.config(background='#4065A4')

    frame_image = Frame(display_window, bg="#4065A4", width=360)
    frame_image.pack(side=LEFT, fill=Y, padx=10, pady=10)

    frame_info = Frame(display_window, bg="#4065A4")
    frame_info.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

    # Ajoute l'image dans le frame_image
    village_image = PhotoImage(file=chemin_images)
    label_image = Label(frame_image, image=village_image, bg="#4065A4")
    label_image.image = village_image  # Conserver la référence pour éviter la collecte
    label_image.pack()

    # Ajoute les informations dans l'autre frame'
    infos = [
        f"Nom : {village.nom}",
        f"Position : {village.position}",
        f"Nombre d'habitants : {village.population()}",
        f"Église : {'Oui' if village.eglise else 'Non'}",
        f"Ressources totales : {total_ressources}",
        f"Argent total : {total_argent}",
        f"Armée : {village.armee_village} soldats"
    ]

    for info in infos:
        Label(frame_info, text=info, font=("Arial", 14), bg="#4065A4", fg="white").pack(pady=5)

    display_window.mainloop()


def main():
    global root
    root = Tk()
    root.title("Gestion Fief")
    root.geometry("200x100")

    Button(root, text="Ouvrir la carte", command=open_map_window).pack(pady=5)
    Button(root, text="Ouvrir le menu", command=open_menu_window).pack(pady=5)
    Button(root, text="Quitter", command=root.destroy).pack(pady=5)

    root.mainloop()
