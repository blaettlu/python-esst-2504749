

import random

le = '-'
sp1 = 'x'
sp2 = 'o'

#spielbrett = ['-','x','o','-','x','-','o','-','-']
#spielbrett = [le,sp1,sp2,le,sp1,le,sp2,le,le]
spielbrett = [le,le,le,le,le,le,le,le,le]

def ausgabe_spielbrett():
   print("Spielbrett:")
   brett = spielbrett
   print(brett[0],brett[1],brett[2])
   print(brett[3],brett[4],brett[5])
   print(brett[6],brett[7],brett[8])
  
def stein_setzen(sp):
   kr = 0
   while kr == 0:
      p = random.randint(0,8)
      if spielbrett[p] == le:
         spielbrett[p] = sp
         kr = 1

ausgabe_spielbrett()
for i in range(4):
   stein_setzen(sp1)
   stein_setzen(sp2)
ausgabe_spielbrett()

