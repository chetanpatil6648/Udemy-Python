# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************


#TREASURE ISLAND
print(" WELCOME TO THE TREASURE ISLAND..!\n YOUR MISSION IS TO FIND THE TREASURE..!\n BEST LUCK CHOOSE THE RIGHT PATH..!")

choice1 = input("You are at the cross road. where you want to go? type LEFT or RIGHT?\n").upper()

if choice1 == 'LEFT':
  print("You have taken right choice, your are safe now..!")
  choice2 = input("You are at the lake. There is an island in the middle of the lake. Type WAIT to wait for a boat to come or Type SWIM to swim across the lake?\n").upper()

  if choice2 == 'WAIT':
    print("You have taken right choice, your are safe now and arrive in the final stage, be more aware..!\n BEST OF LUCK PLAY WELL..!")
    choice3 = input("You have arrived at the island unharmed. There is a house with 3 doors. One RED, one YELLOW and one BLUE. Which colour do you choose?\n").upper()

    if choice3 == 'YELLOW':
      print("CONGRATS..!\nWINNER.\nWINNER.\nWINNER.\n You have taken right choice and You are a WINNER of this Game..!")
    elif choice3 == 'RED':
      print("You have taken WRONG choice, You are burned by fire..!\n THANK YOU FOR PLAYING..!\n YOUR GAME IS OVER YOU MAY CLOSE THE WINDOW..!")
    elif choice3 == 'BLUE':
      print("You have taken WRONG choice, You are eaten by beasts..!\n THANK YOU FOR PLAYING..!\n YOUR GAME IS OVER YOU MAY CLOSE THE WINDOW..!")
    else:
      print("You have taken WRONG choice...!\n THANK YOU FOR PLAYING..!\n YOUR GAME IS OVER YOU MAY CLOSE THE WINDOW..!")

  else:
    print("You have taken WRONG choice, You are attacked by trout..!\n THANK YOU FOR PLAYING..!\n YOUR GAME IS OVER YOU MAY CLOSE THE WINDOW..!")
  
else:
  print("You have taken WRONG choice, you are fall into the hole..!\n THANK YOU FOR PLAYING..!\n YOUR GAME IS OVER YOU MAY CLOSE THE WINDOW..!")