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
