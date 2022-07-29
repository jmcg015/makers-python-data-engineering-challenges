my_list = ["Cat", "Mouse", "Frog"]

# Write some code to amend the list here.
my_list[0] = 'Mouse'
my_list[1] = 'Lynx'
my_list[2] = 'Cat'
my_list.append('Frog')

print(my_list)
# Should print:
# ['Mouse', 'Lynx', 'Cat', 'Frog']

my_list = ["Cat", "cat", "frog", "cat", "dog", "Dog"]
counters = {}

# Write some code to count the items in the list here
for animal in my_list:
  lowercase_animal = animal.lower()
  if lowercase_animal in counters:

    counters[lowercase_animal] += 1
  else:
    counters[lowercase_animal] = 1


print(counters)
# Should print (in any order)
# { 'cat': 3, 'dog': 2, 'frog': 1 }

my_cohort = ["Peter", "Tony", "Steve", "Natasha", "Rose", "Sophie"]
letter_counter = {}

for name in my_cohort:
  if name[0] in letter_counter:
    letter_counter[name[0]] += 1
  else:
    letter_counter[name[0]] = 1

print(letter_counter)

# Program should print a dictionary with each of the letters of the alphabet
# and the number of people whose first name begins with that letter.
# E.g. { 'a': 2, 'b': 0, ... }