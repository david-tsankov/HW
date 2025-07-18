# legend: ✅-got correct output
#         ❌-couldnt get correct output 

# ---------------------------------- Task 1 ---------------------------------- #✅
""" DESCRIPTION:
    Write a program that takes an integer n and prints a triangle pattern of stars (*). The number of stars in the first line is 1, in the second line is 2, and so on up to n stars in the n-th line.
"""

### Your code here

# int=int(input("Please enter an integer: "))
# index=0
# for i in range(1,int+1):
#     print(f"{i*"*"}")

### EXPECTED OUTPUT:
# Enter stars number: 4
# *
# **
# ***
# ****


# ---------------------------------- Task 2 ---------------------------------- #✅
""" DESCRIPTION:
    Write a script that prompts the user to enter words, one at a time.
    The user should continue to enter words until they enter '0'.
    After the user enters '0', the script should display all the words that start with a vowel (a, e, i, o, u).
"""

### Your code


# list=[]
# word=""
# while word!="0":
#     word=input("Enter a word: ")
#     list.append(word)
# index=0

# list_vowels=[]
# for i in list:
#     if i[0] in ["a", "e", "i", "o", "u"]:
#         list_vowels.append(i)
# print(f"List of words which start with a vowel: {list_vowels}")


### EXPECTED OUTPUT:
# Enter a word (or '0' to stop): atom
# Enter a word (or '0' to stop): see
# Enter a word (or '0' to stop): end
# Enter a word (or '0' to stop): 0
# Words that start with a vowel: ['atom', 'end']


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a script that takes a list of strings and returns a dictionary,
    where each key is a string length and each value is a list of strings of that length.
"""

### Given:
words = ["hello", "world", "python", "is", "fun", "and", "usefull"]

### Your code here

# dict={

# }
# index=0
# for i in range(0,7):
#     dict[len(words[i])]=""
# print(dict)

# for key,value in dict:
#     value.append()
# print(dict)

    

### EXPECTED OUTPUT:
# {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun', 'and'], 7: ['usefull']}


# ---------------------------------- Task 4 ---------------------------------- #✅
# """ DESCRIPTION:
#     In a supermarket inventory system, there are two sets of product categories:
#     1. Categories that need refrigeration.
#     2. Categories on sale this week.

#     Write a script, which performs the following tasks:
#     a. Find and print the categories that are both refrigerated and on sale.
#     b. Find and print categories that are on sale but do not require refrigeration.
#     c. Suggest new sale categories from the refrigerated items which are not yet on sale.

#     Note: The category names are assumed to be in lowercase.
# """

### Given
# refrigerated = {'dairy', 'meats', 'frozen foods', 'seafood', 'deli'}
# sale = {'cereals', 'dairy', 'snacks', 'frozen foods', 'beverages'}

### Your code here

# refrigerated_and_sale=refrigerated & sale
# refrigerated_not_needed=sale-refrigerated
# new_items_not_on_sale=refrigerated-sale
# list=[refrigerated_and_sale, refrigerated_not_needed, new_items_not_on_sale]
# for i in list:
#     print(i)

### EXPECTED OUTPUT:
# Categories both refrigerated and on sale: {'dairy', 'frozen foods'}
# Sale categories not needing refrigeration: {'snacks', 'beverages', 'cereals'}
# Suggested new sale categories from refrigerated items: {'seafood', 'deli', 'meats'}