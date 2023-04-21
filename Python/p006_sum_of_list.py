def sum_of_list(param_list):
    total = 0
    for item in param_list:
        total += item
    return total


list1 = [1, 3, 5, 9]
list2 = [39, 23, 3, 3]
print(f"sum of {list2}:", sum_of_list(list2))
print(f"sum of {list1}:", sum_of_list(list1))


print(f"sum of {list2}:", sum(list2))
print(f"sum of {list1}:", sum(list1))