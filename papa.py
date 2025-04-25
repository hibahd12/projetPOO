import csv
import tkinter as tk
from tkinter import messagebox

class GestionnaireConge:
    """Classe pour gérer l'enregistrement des demandes de congé."""
    
    def __init__(self, fichier):
        self.fichier = fichier
        self.creer_fichier_si_inexistant()

    def creer_fichier_si_inexistant(self):
        """Crée le fichier CSV avec un en-tête s'il n'existe pas."""
        try:
            with open(self.fichier, mode="x", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Nom", "Date de début", "Date de fin", "Motif"])
        except FileExistsError:
            pass

    def enregistrer_conge(self, nom, date_debut, date_fin, motif):
        """Ajoute une demande de congé dans le fichier CSV"""
        if not nom or not date_debut or not date_fin or not motif:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires !")
            return
        
        with open(self.fichier, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([nom, date_debut, date_fin, motif])
        
        messagebox.showinfo("Succès", f"✅ La demande de congé de {nom} a été enregistrée !")
        self.effacer_champs()

    def effacer_champs(self):
        """Efface les champs après l'enregistrement."""
        entree_nom.delete(0, tk.END)
        entree_date_debut.delete(0, tk.END)
        entree_date_fin.delete(0, tk.END)
        entree_motif.delete(0, tk.END)

root = tk.Tk()
root.title("Gestion des Congés")
root.geometry("400x300")

tk.Label(root, text="Nom:").pack()
entree_nom = tk.Entry(root)
entree_nom.pack()

tk.Label(root, text="Date de début (YYYY-MM-DD):").pack()
entree_date_debut = tk.Entry(root)
entree_date_debut.pack()

tk.Label(root, text="Date de fin (YYYY-MM-DD):").pack()
entree_date_fin = tk.Entry(root)
entree_date_fin.pack()

tk.Label(root, text="Motif:").pack()
entree_motif = tk.Entry(root)
entree_motif.pack()

gestionnaire = GestionnaireConge("demandes_conge.csv")

bouton_enregistrer = tk.Button(root, text="Enregistrer", command=lambda: gestionnaire.enregistrer_conge(
    entree_nom.get(), entree_date_debut.get(), entree_date_fin.get(), entree_motif.get()
))
bouton_enregistrer.pack()

root.mainloop()
