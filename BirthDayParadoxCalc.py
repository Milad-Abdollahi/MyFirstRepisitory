# Generet 23 random numbers
import random
number_of_people = int(input('enter number of people '))
number_of_iterations = int(input('enter number of iterations '))
groups_with_duplicate = 0
for i in range(number_of_iterations):
   list_of_birthdays = []

   for j in range(number_of_people):
      n = random.randint(1,366)
      list_of_birthdays.append(n)


   has_a_duplicate = 0
   for k in list_of_birthdays:
      if list_of_birthdays.count(k) != 1:
         has_a_duplicate += 1

   duplicatedbdays = has_a_duplicate//2
   if duplicatedbdays != 0:
      groups_with_duplicate += 1

chanse_of_duplicated = 100 * groups_with_duplicate/number_of_iterations


print(f' in a group of {number_of_people} people there is a {chanse_of_duplicated} % chanse '
    f'of duplicated birth day')
