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