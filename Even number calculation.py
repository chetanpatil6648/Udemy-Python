#Total of all even number between range

target = int(input("Enter number for calculation: \n")) 
 
if target > 1000 or target < 0:
  print("You type invalid number..! Type number between 0 to 1000")
else:
  total = 0
  for number in range(2,target,2):
    total += number
  print(f"Total of all Even number beetween 0 to {target} is {total}")