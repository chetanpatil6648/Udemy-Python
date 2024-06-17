# Tip Calculator
print("WELCOME TO THE TIP CALCULATOR...!!")
bill = float( input("what is th total bill amount? \n"))
tip = input(f"how much tip you want give?, 10,12 or 15 \n")
tip_int = int(tip) * (15 / 100)
total_bill = bill + tip_int
per = int(input("how many person should pay the bill?\n"))
per_person = str(total_bill / per)[0:5]
print(f"Each Person Should Pay {per_person} ")
