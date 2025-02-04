numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)


even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(labels)


x = 5
while x > 0: print(x); x -= 1

