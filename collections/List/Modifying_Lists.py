numbers = [1, 2, 3, 4, 5]

# Changing an element
numbers[2] = 10
print(f'After changing the value of position 2: ', numbers)

# Adding elements
numbers.append(6)
print(f'After adding the value: ', numbers)

numbers.insert(2, 99)
print(f'After inserting the value at position 2: ', numbers)

# Extending list
numbers.extend([7, 11])
print(f'After adding the value: ', numbers)

# Removing elements
numbers.remove(99)
print(f'After removing the value: ', numbers)

del numbers[3]
print(f'After removing the value: ', numbers)

popped = numbers.pop()
print(f'After removing the value: ', numbers)

# Clearing the list
numbers.clear()
print(f'After clearing the value: ', numbers)