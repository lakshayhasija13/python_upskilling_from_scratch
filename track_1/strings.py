my_name = "Lakshay"
first_initial = my_name[0]

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)
print(new_account)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  return first_name[-3:] + last_name[-3:]

temp_password = password_generator(first_name, last_name)
print(temp_password)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]

password = "theycallme\"crazy\"91"

def get_length(word):
  return len(word)

def letter_check(word, letter):
  if letter in word:
    return True
  return False

def common_letters(string_one, string_two):
  lst = []
  for l in string_one:
    for i in string_two:
      if l == i and l not in lst:
        lst.append(l)
  return lst

def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    user_name = first_name + last_name
  else:
    user_name = first_name[:3] + last_name[:4]
  return user_name

def password_generator(user_name):
  password = user_name[-1] + user_name[:-1]
  return password

# THE END




