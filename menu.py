from tkinter import *
import subprocess
import menu_fief


# Chemin du dossier conte-nant les images
image_folder = r"res/bouttons"

def nouvelle_partie():
    window.destroy()  # Ferme la fenêtre 
    if __name__ == "__main__":
        menu_fief.main()


#Peut etre qu'il faudrait juste close la fenetre et executer menu_fief
def menu():
    global window 
    # Création de la fenêtre
    window = Tk()
    window.title("Projet IHM")
    window.geometry("1080x720")
    window.config(background="#25b3c9")

    # Canvas
    canvas = Canvas(window, width=1080, height=720, bg="#2A2F4F", highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    # Images pour faire les boutoons
    boutton_image1 = PhotoImage(file="../res/bouttons/boutton_1_cyan.png")
    boutton_image2 = PhotoImage(file="../res/bouttons/boutton_1_cyan.png")
    boutton_image3 = PhotoImage(file="../res/bouttons/boutton_1_cyan.png")
    boutton_image4 = PhotoImage(file="../res/bouttons/boutton_2_cyan.png")

    # Ajouter un titre
    canvas.create_text(
        540, 50, text="Projet IHM ", font=("Arial", 40, "bold"), fill="white", anchor="center"
    )

    #  1
    boutton1 = Button(
        window,
        text="Nouvelle Partie",
        font=("Arial", 20),
        image=boutton_image1,
        compound="center",  
        bg="#2A2F4F",
        fg="black",
        borderwidth=0,
        command= lambda :nouvelle_partie()  # Appelle la fonction pour exécuter menu_fief.py
    )
    boutton1.place(x=400, y=150)


    boutton2 = Button(
        window,
        text="Charger Partie",
        font=("Arial", 20),
        image=boutton_image2,
        compound="center",
        bg="#2A2F4F",
        fg="black",
        borderwidth=0,
        command=lambda: print("Bouton 2 cliqué")
    )
    boutton2.place(x=400, y=250)


    boutton3 = Button(
        window,
        text="Jsp",
        font=("Arial", 20),
        image=boutton_image3,
        compound="center",
        bg="#2A2F4F",
        fg="black",
        borderwidth=0,
        command=lambda: print("Bouton 3 cliqué")
    )
    boutton3.place(x=400, y=350)

    boutton4 = Button(
        window,
        text="Quitter",
        font=("Arial", 15),
        image=boutton_image4,
        compound="center",
        bg="#2A2F4F",
        fg="black",
        borderwidth=0,
        command=window.quit
    )
    boutton4.place(relx=0.95, rely=0.9, anchor=SE)

    window.mainloop()

if __name__ == "__main__":
    global window 
    menu()



