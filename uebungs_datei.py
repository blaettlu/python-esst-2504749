# Das ist ein Kommentar in Ihrer Uebungsdatei


zahl1 = 2.2
zahl2 = 2.6
zahl3 = 4.8

def meine_vergleichsfunktion(p1, p2, p3):
  bl1 = False
  if (p1 < p2) and (p2 < p3): bl1 = True
  return bl1

#print('zahl1 < zahl2 < zahl3 ? ',meine_vergleichsfunktion(zahl1,zahl2,zahl3))
print(str(zahl1) + ' < ' + str(zahl2) + ' < ' + str(zahl3) + ' ?: ',meine_vergleichsfunktion(zahl1,zahl2,zahl3))



