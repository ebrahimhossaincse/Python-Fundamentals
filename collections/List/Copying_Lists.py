# Shallow copy
list_a = [1, 2, 3]
list_b = list_a.copy()
print(list_b)

list_b.append(4)
print(list_b)

# Deep copy (for nested lists)
import copy
nested_list = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested_list)
print(deep_copy)

deep_copy[0][0] = 99
print(deep_copy)
