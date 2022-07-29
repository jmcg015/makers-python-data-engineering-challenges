import random

random_number = random.randint(1, 5)

print(random_number)
if random_number == 1:
  print("One")
elif random_number == 2:
  print("Two")
else:
  print("More")

# Print "One" if `random_number` is 1
# Print "Two" if `random_number` is 2
# Print "More" if `random_number is above 2