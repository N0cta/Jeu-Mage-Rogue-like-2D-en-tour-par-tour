vie_max = 20
max_mana = 20

vie = vie_max
mana = max_mana
boost_mana = 0

atk = {
    "Épée en bois": {"degat": 2},
}

sorts = {
    "Boule de feu": {"cout": 2, "boost": 2},
    "Soin": {"cout": 2, "boost": 2},
    "Eclair": {"cout": 4, "boost": 4},
    "Barriere magique": {"cout": 4, "boost": 4},
    "Invocation d'ombre": {"cout": 5, "boost": 5},
}

sac = {
    "Potion de soin": {"heal": 10, "mana": 0},
    "Potion de mana": {"heal": 0, "mana": 5},
}

def clamp_stats():
    global vie, mana, max_mana, vie_max
    if vie > vie_max:
        vie = vie_max
    if vie < 0:
        vie = 0
    if mana > max_mana:
        mana = max_mana
    if mana < 0:
        mana = 0

def afficher_stats():
    print(f"\nVie : {vie}/{vie_max} | Mana : {mana}/{max_mana} | Compteur up mana : {boost_mana}/20")

def up_max_mana_si_palier():
    global max_mana, boost_mana
    while boost_mana >= 20:
        max_mana += 1
        boost_mana -= 20
        print(f"→ Ton MAX MANA augmente ! Il est maintenant de {max_mana}.")

def menu(liste):
    noms = list(liste.keys())
    for i, nom in enumerate(noms, 1):
        print(f"{i}. {nom}")
    choix = input("> ")
    if choix.isdigit():
        idx = int(choix) - 1
        if 0 <= idx < len(noms):
            return noms[idx]
    if choix in liste:
        return choix
    return ""

while True:
    afficher_stats()
    print("\nActions :")
    print("1. Attaquer")
    print("2. Lancer un sort")
    print("3. Utiliser un objet du sac")
    print("4. Passer le tour")
    print("q. Quitter")

    action = input("Choix ? ").strip().lower()

    if action == "q":
        print("Fin de partie.")
        break

    elif action == "1":
        print("\n== Attaques ==")
        choix_atk = menu(atk)
        if not choix_atk:
            print("Attaque inconnue.")
        else:
            deg = atk[choix_atk]["degat"]
            print(f"Tu frappes avec {choix_atk} et infliges {deg} dégâts.")

    elif action == "2":
        print("\n== Sorts ==")
        choix_sort = menu(sorts)
        if not choix_sort:
            print("Sort inconnu.")
        else:
            cout = sorts[choix_sort]["cout"]
            if mana >= cout:
                mana -= cout
                boost_mana += cout
                print(f"Tu as lancé {choix_sort} ! (-{cout} mana)")
                up_max_mana_si_palier()

                if choix_sort == "Soin":
                    vie += 5
                    print("Tu te soignes de 5 PV.")

            else:
                print("Pas assez de mana pour ce sort.")

    elif action == "3":
        print("\n== Sac ==")
        choix_obj = menu(sac)
        if not choix_obj:
            print("Objet inconnu.")
        else:
            effet = sac[choix_obj]
            heal = effet.get("heal", 0)
            mana_gain = effet.get("mana", 0)

            if heal:
                vie += heal
                print(f"Tu utilises {choix_obj} et récupères {heal} PV.")
            if mana_gain:
                mana += mana_gain
                print(f"Tu utilises {choix_obj} et récupères {mana_gain} mana.")

    elif action == "4":
        print("Tu passes ton tour.")

    else:
        print("Choix invalide.")

    clamp_stats()
