# From string (characters)
char_list = list("hello")
print(char_list)

# From tuple
tuple1 = (1, 2, 3)
list_from_tuple = list(tuple1)
print(list_from_tuple)

# From set
set1 = {1, 2, 3}
list_from_set = list(set1)
print(list_from_set)

# String to list (split)
sentence = "Python is awesome"
words = sentence.split()
print(words)

# List to string (join)
sentence_back = " ".join(words)
print(sentence_back)
