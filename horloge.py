from tkinter import *
import time

root = Tk()

root.title("Heure")
root.geometry("1920x1040+0+0")
root.config(bg="black")

def recupereHeure():
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
    
    # Mettre à jour le texte des labels
    lbl_heure.config(text=h)
    lbl_minute.config(text=m)
    lbl_seconde.config(text=s)

    # Actualiser toutes les 1000 ms (1 seconde)
    root.after(1000, recupereHeure)

# Heure
lbl_heure = Label(root, text="12", font=("arial", 50, "bold"), bg="blue")
lbl_heure.place(x=600, y=300, width=200, height=130)

heure = Label(root, text="Heure", font=("arial", 20, "bold"), bg="blue")
heure.place(x=600, y=450, width=200, height=30)

# Minute
lbl_minute = Label(root, text="30", font=("arial", 50, "bold"), bg="white")
lbl_minute.place(x=850, y=300, width=200, height=130)

minute = Label(root, text="Minute", font=("arial", 20, "bold"), bg="white")
minute.place(x=850, y=450, width=200, height=30)

# Seconde
lbl_seconde = Label(root, text="50", font=("arial", 50, "bold"), bg="red")
lbl_seconde.place(x=1100, y=300, width=200, height=130)

seconde = Label(root, text="Seconde", font=("arial", 20, "bold"), bg="red")
seconde.place(x=1100, y=450, width=200, height=30)

# Appeler la fonction pour mettre à jour l'heure
recupereHeure()

root.mainloop()
