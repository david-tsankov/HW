# legend: ✅-got correct output
#         ❌-couldnt get correct output 

# ---------------------------------- Task 1 ---------------------------------- #✅
"""DESCRIPTION:
Write a function named 'calculate_area' that takes two parameters (length and width)
and returns the area of a rectangle.
"""


### YOUR CODE HERE

# def calculate_area(lenght,width):
#     area=lenght*width
#     print(area)
# calculate_area(10,5)


### TEST:
# print(calculate_area(10, 5))

### EXPECTED OUTPUT:
# 50


# ---------------------------------- Task 2 ---------------------------------- #✅
""" DESCRIPTION:
Create a function 'is_even' that takes a single integer argument and returns True
if the number is even, and False otherwise.
"""


### YOUR CODE HERE

# def is_even(number):
#     if number%2==0:
#         return(True)
#     else:
#         return(False)
# print(is_even(5))

### TEST:
# print(is_even(4))
# print(is_even(5))

### EXPECTED OUTPUT
# True
# False


# ---------------------------------- Task 3 ---------------------------------- #✅
# note(cant make it take a list, only the normal *args)

""" DESCRIPTION:
Write a function named 'multiply_elements' that takes a list of integers and returns the product of all the elements in the list.
"""


### YOUR CODE HERE

# def multiply_elements(*args):
#     product=1
#     for number in args:
#         product=number*product
#     return product

### TEST:
# print(multiply_elements(1,2,3,4,5,6,7,8,9,10))

### EXPECTED OUTPUT:
# 24


# ---------------------------------- Task 4 ---------------------------------- #✅
""" DESCRIPTION:
Create a function 'count_vowels' that takes a string and returns the count of vowels (a, e, i, o, u) in the string.
"""


### YOUR CODE HERE

# def count_vowels(string):
#     """Only string parameters allowed"""
#     string=string.lower()
#     index=0
#     for letter in string:
#         if letter in ["a","i","e","o","u"]:
#             index=index+1
#     return index

        


### TEST:
# print(count_vowels("hello"))
# print(count_vowels("world"))

### EXPECTED OUTPUT:
# 2
# 1


# ---------------------------------- Task 5 ---------------------------------- #✅
""" DESCRIPTION:
Write a lambda function 'reverse_string' that takes a string and returns the string reversed.
"""

### YOUR CODE HERE

# reverse_string=lambda string:string[::-1]

### TEST:
# print(reverse_string("skib skib"))

### EXPECTED OUTPUT:
# "olleh"


# ---------------------------------- Task 6 ---------------------------------- #✅
""" DESCRIPTION:
Write a function 'find_max' that takes a list of numbers and returns the largest number in the list.
"""


### YOUR CODE HERE
# import math
# def find_max(*args):
#     index=-math.inf
#     for number in args:
#         if number>index:
#             max=number
#             index=number
#         else:max=index
#     return max



### TEST:
# print(find_max(-1, 3, 2, 8, 100000000000))

### EXPECTED OUTPUT:
# 8


# ---------------------------------- Task 7 ---------------------------------- #✅
""" DESCRIPTION:
Create a function 'remove_duplicates' that takes a list and removes duplicate elements, returning a new list with unique elements.
"""


### YOUR CODE HERE

# def remove_duplicates(*args):
#     args=list(set(args))
#     return args


### TEST:
# print(remove_duplicates(1, 2, 2, 3, 4, 3))

### EXPECTED OUTPUT:
# [1, 2, 3, 4]


# ---------------------------------- Task 8 ---------------------------------- #✅
""" DESCRIPTION:
Write a lambda function 'is_palindrome' that checks if a given string is a palindrome.
"""

### YOUR CODE HERE

# is_palindrome=lambda string: string.lower()==string.lower()[::-1]

### TEST:
# print(is_palindrome("madam"))
# print(is_palindrome("hello"))

### EXPECTED OUTPUT:
# True
# False


# ---------------------------------- Task 9 ---------------------------------- #✅
""" DESCRIPTION:
Write a lambda function 'add' that takes two arguments and returns their sum.
"""

### YOUR CODE HERE

# add=lambda x,y: x+y

### TEST:
# print(add(9, 3))

### EXPECTED OUTPUT:
# 5


# ---------------------------------- Task 10 ---------------------------------- #✅
""" DESCRIPTION:
Create a function 'filter_words' that takes a list of words and a minimum length, and
returns a list of words that are longer than the given minimum length.
"""


### YOUR CODE HERE

# def filter_words(min_lenght=0,*args):
#     words=[]
#     for word in args:
#         if len(word)>min_lenght:
#             words.append(word)
#     return words


### TEST:
# print(filter_words(["apple", "pear", "banana", "cherry"], 5))---->doesnt work for me, as variable arguments before positional in this

# my test:
# print(filter_words(5,"apple", "pear", "banana", "cherry"))

### EXPECTED OUTPUT:
# ['banana', 'cherry']


# ---------------------------------- Task 11 ---------------------------------- #✅
""" DESCRIPTION:
Write a lambda expression 'sort_by_last_letter' that sorts a list of strings based on
the last letter of each string. Use this lambda expression to sort a given list,
using the sorted() built-in function.
"""

### YOUR CODE HERE

# sort_by_last_letter=lambda x:x[-1]

### TEST:
# print(sorted(["cherry", "banana", "apple"], key=sort_by_last_letter))

### EXPECTED OUTPUT:
# ['banana', 'apple', 'cherry']