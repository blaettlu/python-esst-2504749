# Listen sind eine Art Container, in dem Sie mehrere Werte speichern können.
meine_zahlen_liste = [1, 2, 3, 4, 5]
meine_buchstaben_liste = ["a", "b", "c", "d", "e"]
meine_gemischte_liste = [1, "a", 2, "b", 3, "c"]

# hinzufügen von Werten
meine_zahlen_liste.append(6)

# Wert ausgeben
print("meine_zahlen_liste:", meine_zahlen_liste)
print("1. Wert in der Liste meine_zahlen_liste:", meine_zahlen_liste[0])
print("2. Wert in der Liste meine_zahlen_liste:", meine_zahlen_liste[1])

# Wert löschen
print("meine_zahlen_liste vor dem Löschen:", meine_zahlen_liste)
meine_zahlen_liste.remove(3)
print("meine_zahlen_liste nach dem Löschen:", meine_zahlen_liste)

