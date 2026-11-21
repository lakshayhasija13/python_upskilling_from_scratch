my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

first_expression = 2 * 2 == 2 + 2
second_expression = 3 + 3 != 3 * 3 
third_expression = 3 * 3 == '9'

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")

statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")
elif not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
elif not credits >= 120 and not gpa >= 2.0 :
  print("You do not meet either requirement to graduate!")

# THE END
