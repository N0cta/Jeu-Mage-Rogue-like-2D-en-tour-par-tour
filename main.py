max_mana = 20
mana = max_mana
boost_mana = 0

sorts = {
    "Boule de feu": {"cout": 2, "boost": 2},
    "Soin": {"cout": 2, "boost": 2},
    "Eclair": {"cout": 4, "boost": 4},
    "Barriere magique": {"cout": 4, "boost": 4},
    "Invocation d'ombre": {"cout": 5, "boost": 5},
}

while mana >= 1:
    choix = input("Quel sort veux-tu utiliser ? ")

    if choix in sorts:
        cout = sorts[choix]["cout"]
        boost = sorts[choix]["boost"]

        if mana >= cout:
            mana -= cout
            print(f"Tu as lancé {choix} ! (-{cout} mana, boost stocké +{boost})")
        else:
            print("Pas assez de mana pour ce sort !")
    else:
        print("Sort inconnu, essaie encore.")

print("\nTu n’as plus de mana, la partie est finie !")
