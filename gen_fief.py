from tkinter import *
import random

global compteur_terrain
compteur_terrain = 0

global chemin_images 
chemin_images = { #60x60 pixels pour les terrains et 380x380 pour les maps 
    "Map_test": "../res/terrain_map/Map_test.png",
    "Map_vierge": "../res/terrain_map/Map_vierge.png",
    "Chateau" : "../res/terrain_map/Chateau.png",
    "Foret": "../res/terrain_map/Foret.png",
    "Lac": "../res/terrain_map/Lac.png",
    "Montagne": "../res/terrain_map/Montagne.png",
    "Terrain": "../res/terrain_map/Terrain.png",
    "Village": "../res/terrain_map/Village.png",
}


terrain_actif = { #0 c'est un terrain dispo, 1 terrain non dispo, 2 c'est autre chose, 3 il y a un village  
    "Position 1": 0,
    "Position 2": 0,
    "Position 3": 0,
    "Position 4": 0,
    "Position 5": 0,
    "Position 6": 0,
    "Position 7": 0,
    "Position 8": 0,
    "Position 9": 0,
    "Position 10": 0,
    "Position 11": 0,
    "Position 12": 0,
    "Position 13": 0,
    "Position 14": 0,
    "Position 15": 0,
    "Position 16": 0,
    "Position 17": 0,
    "Position 18": 0,
    "Position 19": 0,
    "Position 20": 0,
    "Position 21": 0,
    "Position 22": 0,
    "Position 23": 0,
    "Position 24": 0,
    "Position 25": 0,

}

positions = {  # Il y aura 25 positions différentes, la bande rouge fait 20 ?
    "Position 1": (30, 30),
    "Position 2": (110, 30),
    "Position 3": (190, 30),
    "Position 4": (270, 30),
    "Position 5": (350, 30),
    "Position 6": (30, 110),
    "Position 7": (110,110),
    "Position 8": (190,110),
    "Position 9": (270,110),
    "Position 10": (350,110),
    "Position 11": (30,190),
    "Position 12": (110,190),
    "Position 13": (190,190),
    "Position 14": (270,190),
    "Position 15": (350,190),
    "Position 16": (30,270),
    "Position 17": (110,270),
    "Position 18": (190,270),
    "Position 19": (270,270),
    "Position 20": (350,270),
    "Position 21": (30,350),
    "Position 22": (110,350),
    "Position 23": (190,350),
    "Position 24": (270,350),
    "Position 25": (350,350)

}

Chateau_cree = {}
Foret_cree = {}
Lac_cree = {}
Montagne_cree = {}
Village_cree = {}
Terrain_cree = {}

def terrain_present(pos, val):
    """
    Met à jour l'état d'un village (1 pour actif, 0 pour inactif).
    """
    global terrain_actif
    terrain_actif[pos] = val

def terrain_proche(i) :
    global terrain_actif

    if (i >= 7):   
        if terrain_actif[f"Position {i-1}"] == 1 :
            return False 
        if terrain_actif[f"Position {i-4}"] == 1 :
            return False 
        if terrain_actif[f"Position {i-5}"] == 1 :
            return False 
        if terrain_actif[f"Position {i-6}"] == 1 :
            return False 
        else : 
            return True 
    else :
        return True 

def construire_chateau(pos):
    global Chateau_image
    x, y = positions[pos]
    Chateau_cree[pos] = canvas.create_image(x, y, image=Chateau_image, anchor=CENTER)
    terrain_present(pos, 2)
    #print("Debug - construire_chateau (gen_fief)")

def construire_village(pos):
    global Village_image
    x, y = positions[pos]
    Village_cree[pos] = canvas.create_image(x, y, image=Village_image, anchor=CENTER, tags="village")
    terrain_present(pos, 3)


def construire_terrain(pos):
    global Terrain_image,compteur_terrain
    x, y = positions[pos]  
    Terrain_cree[pos] = canvas.create_image(x, y, image=Terrain_image, anchor=CENTER)
    terrain_present(pos, 1)
    compteur_terrain += 1 

    
def construire_Lac(pos):
    global Lac_image
    x, y = positions[pos]
    Lac_cree[pos] = canvas.create_image(x, y, image=Lac_image, anchor=CENTER)
    terrain_present(pos, 2)


def construire_Montagne(pos):
    global Montagne_image
    x, y = positions[pos]
    Montagne_cree[pos] = canvas.create_image(x, y, image=Montagne_image, anchor=CENTER)
    terrain_present(pos, 2)


def construire_Foret(pos):
    global Foret_image
    x, y = positions[pos]
    Foret_cree[pos] = canvas.create_image(x, y, image=Montagne_image, anchor=CENTER)
    terrain_present(pos, 2)

def laisser_plaine(pos):
    pass

def init_fief(window):
    global canvas, Chateau_image, Foret_image, Lac_image, Montagne_image, Terrain_image, Village_image, map_image

    canvas = Canvas(window, width=1080, height=720, bg="black") #Ce canvas est pour celui de la map dans gen_fief.canvas fait reference à la map.
    
    canvas.pack()

    # Charger les images
    Chateau_image = PhotoImage(file=chemin_images["Chateau"])
    Foret_image = PhotoImage(file=chemin_images["Foret"])
    Lac_image = PhotoImage(file=chemin_images["Lac"])
    Montagne_image = PhotoImage(file=chemin_images["Montagne"])
    Terrain_image = PhotoImage(file=chemin_images["Terrain"])
    Village_image = PhotoImage(file=chemin_images["Village"])
    map_image = PhotoImage(file=chemin_images["Map_vierge"])

    # Afficher la carte de base
    canvas.create_image(0, 0, image=map_image, anchor=NW)

    
def gen(pos,i):
    global terrain_actif

    fonctions = {
        1: construire_terrain,
        2: construire_Lac,
        3: construire_Montagne,
        4: construire_Foret,
        5: laisser_plaine
    }

    fonction_alea = random.randint(1, len(fonctions))

    if terrain_proche(i) == True and compteur_terrain < 4: #On se limite à 4 villages possibles et aucun doit etre aux alentours.
        fonctions[fonction_alea](pos)
    else :
        laisser_plaine

def generate_fief():
    
    # Construire les 25 terrains
    for i in range(25):
        pos = f"Position {i+1}"
        gen(pos,i)


    #Pose le chateau du seigneur 
    for i in range(25):
        if terrain_actif[f"Position {i+1}"] == 0 and terrain_actif[f"Position {i+1}"] != 2 : #Si le terrain est vide et qu'il n'y a pas de biomes installé (foret..)
            construire_chateau(f"Position {i+1}") 
            break

    #Pose du 1er village 

    for i in range(25):
        if terrain_actif[f"Position {i+1}"] == 0 and terrain_actif[f"Position {i+1}"] != 2 :
            construire_village(f"Position {i+1}") 
            break


if __name__ == "__main__":
    global village
    Village = PhotoImage(file=chemin_images["Village"])
    init_fief()  # Initialise correctement le canvas global
    generate_fief()  # Utilise le canvas global pour dessiner les éléments
    window.mainloop()  # Lance la boucle principale

