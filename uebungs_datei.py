# 1.Aufgabe

my_list = [0,10,100]

def ausgabe_meine_liste(paramliste):
  for zahl in paramliste:
    print('Das aktuelle Element ist: ',zahl)

ausgabe_meine_liste(my_list)

# 2.Aufgabe

gkzahl1 = 3.1
gkzahl2 = 4.0

def meine_multiplikation(zahl1, zahl2):
  # multipl = zahl1 * (zahl2+2)
  return zahl1 * (zahl2+2)

print('Das Ergebnis ist: ',meine_multiplikation(gkzahl1,gkzahl2))


# 3.Aufgabe

zahl1 = 2.2
zahl2 = 2.6
zahl3 = 4.8

def meine_vergleichsfunktion(p1, p2, p3):
  if (p1 < p2) and (p2 < p3): return True
  else:
    return False

#print('zahl1 < zahl2 < zahl3 ? ',meine_vergleichsfunktion(zahl1,zahl2,zahl3))
print(str(zahl1) + ' < ' + str(zahl2) + ' < ' + str(zahl3) + ' ?: ',meine_vergleichsfunktion(zahl1,zahl2,zahl3))



