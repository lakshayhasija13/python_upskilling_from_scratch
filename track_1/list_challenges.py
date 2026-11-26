# 1
# Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))


# 2
# Write your function here
def append_sum(my_list):
  for i in range(3):
    my_list.append(my_list[-2] + my_list[-1])
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


# 3
# Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) > len(my_list2):
    return my_list1[-1]
  elif len(my_list1) < len(my_list2):
    return my_list2[-1]
  return my_list1[-1]

# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# 4
# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  return False

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# 5
# Write your function here
def combine_sort(my_list1, my_list2):
  sorted_list = sorted(my_list1 + my_list2)
  return sorted_list

# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


================================================================

# 1
#Write your function here
def every_three_nums(start):
  lst = [i for i in range(start, 101, 3)]
  return lst

#Uncomment the line below when your function is done
print(every_three_nums(91))


# 2
#Write your function here
def remove_middle(my_list, start, end):
  for i in my_list[start:end+1]:
    my_list.remove(i)
  return my_list

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# 3
#Write your function here
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) > my_list.count(item2):
    return item1
  elif my_list.count(item1) < my_list.count(item2):
    return item2
  return item1

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# 4
#Write your function here
def double_index(my_list, index):
  if index < len(my_list):
    my_list[index] = 2 * my_list[index]
  return my_list

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

# 5
#Write your function here
def middle_element(my_list):
  if len(my_list) % 2 != 0:
    return my_list[(len(my_list) - 1) // 2]
  else:
    sum = my_list[len(my_list) // 2] + my_list[(len(my_list) // 2) - 1]
    return sum//2

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))


# THE END






