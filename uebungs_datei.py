# TicTakToe mit Zufallsgenerator



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
  
def stein_setzen_random(sp):
	kr = 0
	while kr == 0:
		p = random.randint(0,8)
		if spielbrett[p] == le:
			spielbrett[p] = sp
			kr = 1

def stein_setzen(sp):
	user_eingabe = 0
	while user_eingabe < 1 or user_eingabe > 9:
		eingabe = input('Position (1..9) für ' + str(sp) + ' : ')
		user_eingabe = int(eingabe)
	spielbrett[user_eingabe - 1] = sp
	ausgabe_spielbrett()
 
def check_gewinner(sp):
	brett = spielbrett
	if brett[0] == sp and brett[1] == sp and brett[2] == sp:
		return True
	if brett[3] == sp and brett[4] == sp and brett[5] == sp:
		return True
	if brett[6] == sp and brett[7] == sp and brett[8] == sp:
		return True
	if brett[0] == sp and brett[3] == sp and brett[6] == sp:
		return True
	if brett[1] == sp and brett[4] == sp and brett[7] == sp:
		return True
	if brett[2] == sp and brett[5] == sp and brett[8] == sp:
		return True
	if brett[0] == sp and brett[4] == sp and brett[8] == sp:
		return True
	if brett[6] == sp and brett[4] == sp and brett[2] == sp:
		return True
	else:
		return False
	

ausgabe_spielbrett()
wi = 0
for i in range(4):
	stein_setzen(sp1)
	if check_gewinner(sp1) == True:
		print("Spieler " + sp1 + " hat gewonnen")
		wi = 1
		break
	stein_setzen(sp2)
	if check_gewinner(sp2) == True:
		print("Spieler " + sp2 + " hat gewonnen")
		wi = 1
		break
	#ausgabe_spielbrett()
if wi == 0:
	print("Unentschieden")
