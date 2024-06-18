print(f"WELCOME TO THE SUN-MOON ROLLERCOASTER..!\n   Note: \n     1. Child tickets are 5 RS and 7 RS. \n     2. Adult tickets are 12 Rs.")

height = int(input("What is your height in cm?\n"))
bill = 0
if height > 120 :
  print("Congrats..!\nYou are eligible to ride a rollercoaster.")
  age = int(input("what is your age in years?  \n"))
  if age < 12:
    bill += 5
    print("You have to pay 5 Rs, Beacuse your age is below 12")
  elif age <= 18 :
    bill += 7
    print("You have to pay 7 Rs, Because your age is below 18 Rs and above 12 Rs")
  else:
    bill += 12
    print("You have to pay 12 Rs, Because your age is above 18 Rs.")
  want_photo = input("If you want a photograph then type Y and if do not want a photograph please type N.\n")
  if want_photo == 'Y':
    bill += 3
    print("You have to pay extra 3 Rs,for photo.")
    print(f"Your Total Bill is = {bill} Rs")
  else:
      print(f"Your Total Bill is = {bill} Rs")
else:
  print("You are not eligible to ride a Rollercoaster..!\nPlease come back when you are taller than 120 cm.\n Thank You..")