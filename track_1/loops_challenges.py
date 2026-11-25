# 1
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0 :
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2
#Write your function here
def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append('Hello, ' + name)
  return greeting

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# 3
#Write your function here
def delete_starting_evens(my_list):
  for i in range(len(my_list)):
    if my_list[0] % 2 == 0 :
      my_list.pop(0)
    else:
      break
  return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# 4
#Write your function here
def odd_indices(my_list):
  lst = []
  for i in range(len(my_list)):
    if i % 2 != 0 :
      lst.append(my_list[i])
  return lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5
#Write your function here
def exponents(bases, powers):
  lst = []
  for base in bases:
    for power in powers:
      lst.append(base ** power)
  return lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

