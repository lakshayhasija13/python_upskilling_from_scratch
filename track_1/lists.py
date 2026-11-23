orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders

broken_prices = [5, 3, 4, 5, 4] + [4]

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(index5_element)
print(last_element)

# Your code below:
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)

# Your code below: 
order_list = [
  "Celery",
  "Orange Juice",
  "Orange",
  "Flatbread"
]
print(order_list)
order_list.remove("Flatbread")
print(order_list)

new_store_order_list = [
  "Orange",
  "Apple",
  "Mango",
  "Broccoli",
  "Mango"
]
print(new_store_order_list)

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights.append(["Vik", 68])
ages = [
  ["Aaron", 15],
  ["Dhruti", 16]
]

#Your code below:
class_name_test = [
  ["Jenny", 90],
  ["Alexus", 85.5],
  ["Sam", 83],
  ["Ellie", 101.5]
]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)

#Your code below:
incoming_class = [
  ["Kenny", "American", 9],
  ["Tanya", "Ukrainian", 9],
  ["Madison", "Indian", 7]
]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)

# Your code below: 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
customer_data = [
  ["Ainsley", "Small", True],
  ["Ben", "Large", False],
  ["Chani", "Medium", True],
  ["Depak", "Medium", False]
]
print(customer_data)
customer_data[2][2] = False
customer_data[1].remove(False)
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)


data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(-2)
print(data_science_topics)


# Your code below: 

number_list = range(9)
print(list(number_list))
zero_to_seven = range(8)
print(list(zero_to_seven))

# Your code below: 

range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below: 
print(beginning)

middle = suitcase[2:4]
print(middle)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count('Jake')
print(jake_votes)

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()
print(sorted_cities)
cities.sort(reverse = True)
print(cities)

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 =  inventory[:3]
twin_beds = inventory.count('twin bed')
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory.sort()
print(inventory)

# 1
# Write your function here
def append_sum(my_list):
  for i in range(3):
    my_list.append(my_list[-2] + my_list[-1])
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# 2
# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  return False

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# 3
#Write your function here
def middle_element(lst):
  if len(lst) % 2 != 0:
    mid = (len(lst) - 1) // 2
    return lst[mid]
  else:
    mid = (lst[len(lst)//2] + lst[(len(lst) // 2) - 1]) // 2
    return mid


#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))


# THE END
