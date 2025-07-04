

import random

#while True:
for i in range(5):

  user_eingabe_short = input('Schere S, Stein T oder Papier P ?: ')

  match user_eingabe_short:
    case 's':
      user_eingabe = 'Schere'
    case 'S':
      user_eingabe ='Schere'
    case 't':
      user_eingabe ='Stein'
    case 'T':
      user_eingabe ='Stein'
    case 'p':
      user_eingabe ='Papier'
    case 'P':
      user_eingabe ='Papier'
    case _:
      user_eingabe ='Ungültige Eingabe'

  print('User    : ',user_eingabe)


  computer_eingabe_num = random.randint(0,3)

  match computer_eingabe_num:
    case 0:
      computer_eingabe = 'Schere'
    case 1:
      computer_eingabe = 'Stein'
    case 2:
      computer_eingabe = 'Papier'
  print('Computer: ',computer_eingabe)

  if user_eingabe == 'Schere' and computer_eingabe == 'Schere':
    winner = 'Unentschieden'
  elif user_eingabe == 'Schere' and computer_eingabe == 'Stein':
    winner = 'Computer'
  elif user_eingabe == 'Schere' and computer_eingabe == 'Papier':
    winner = 'User'
  elif user_eingabe == 'Stein' and computer_eingabe == 'Schere':
    winner = 'User'
  elif user_eingabe == 'Stein' and computer_eingabe == 'Stein':
    winner = 'Unentschieden'
  elif user_eingabe == 'Stein' and computer_eingabe == 'Papier':
    winner = 'Computer'
  elif user_eingabe == 'Papier' and computer_eingabe == 'Schere':
    winner = 'Computer'
  elif user_eingabe == 'Papier' and computer_eingabe == 'Stein':
    winner = 'User'
  elif user_eingabe == 'Papier' and computer_eingabe == 'Papier':
    winner = 'Unentschieden'
  else:
    winner = 'ungültig'

  print('Winner  : ', winner)


