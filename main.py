# Application de gestion des tâches (console) - Partie 1
taches = []


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")
def rechercher_tache():
    mot = input("Mot-clé : ").strip().lower()
    trouve = False
    for i in range(len(taches)):
        if mot in taches[i].lower():
            print(f"{i + 1}. {taches[i]}")
            trouve = True
    if not trouve:
        print("Aucune tâche trouvée.")

def menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")


choix = ""
while choix != "0":
    menu()
    choix = input("Votre choix : ").strip()
    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Option invalide, veuillez réessayer.")
        