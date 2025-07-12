# legend: ✅-got correct output
#         ❌-couldnt get correct output   

# ---------------------------------- Task 1 ---------------------------------- #✅
"""DESCRIPTION:
Create a dictionary to represent person's data:
    name      : Ivan
    age       : 30
    city      : Sofia


Print the data as shown:
"""
### YOUR CODE HERE

# data={
#     "name" : "Ivan",
#     "age" : 30,
#     "city" : "Sofia"
# }
# print(data)


### EXPECTED OUTPUT:
# name      : Ivan
# age       : 30
# city      : Sofia

# ---------------------------------- Task 2 ---------------------------------- #✅
""" DESCRIPTION:
    Given the person dictionary above, add a new key-value pair: "job":"Developer"
"""

### Your code here

# data={
#     "name" : "Ivan",
#     "age" : 30,
#     "city" : "Sofia"
# }

# data["job"] = "developer"
# print(data)

### EXPECTED OUTPUT:
# {'name': 'Ivan', 'age': 30, 'city': 'Sofia', 'job': 'Developer'}


# ---------------------------------- Task 3 ---------------------------------- #✅
""" DESCRIPTION:
    Given a dictionary, update the value of an existing key and print the updated dictionary.
"""

### Your code here

# data={
#     "name" : "Ivan",
#     "age" : 30,
#     "city" : "Sofia"
# }

# data["age"]=31
# print(data)

### EXPECTED OUTPUT:
# {'name': 'Ivan', 'age': 31, 'city': 'Sofia'}


# ---------------------------------- Task 4 ---------------------------------- #✅
""" DESCRIPTION:
    Given a dictionary, remove a key-value pair and print the updated dictionary.
"""

### Your code here

# data={
#     "name" : "Ivan",
#     "age" : 30,
#     "city" : "Sofia"
# }

# del data["age"]
# print(data)

### EXPECTED OUTPUT:
# {'name': 'Ivan', 'city': 'Sofia'}


# ---------------------------------- Task 5 ---------------------------------- #✅
""" DESCRIPTION:
    Given a dictionary, check if a specific key exists and print the result.
"""

### Your code here

# data={
#     "name" : "Ivan",
#     "age" : 30,
#     "city" : "Sofia"
# }
# key=input("Please enter a key you'de like to check: ")
# key_bool=key in data.keys()
# if key_bool==True:
#     print(f"The key is in the dictionary")
# else:
#     print(f"The key is not in the dictionary")


### EXPECTED OUTPUT:
# True


# ---------------------------------- Task 6 ---------------------------------- #✅
""" DESCRIPTION:
    Given two dictionaries, merge them into one and print the result.
"""

### Your code here

# applicant={
#     "name": "Ivan",
#     "age": 30,
#     "city": "Sofia"
# }
# position={
#     "job": "Developer",
#     "salary": 50000
# }
# union_set=set(applicant.items()) | set(position.items())
# print(union_set)

### EXPECTED OUTPUT:
# {'name': 'Ivan', 'age': 30, 'city': 'Sofia', 'job': 'Developer', 'salary': 50000}


# ---------------------------------- Task 7 ---------------------------------- #✅
""" DESCRIPTION:
    Given a dictionary, print all key-value pairs in the format "key: value".
"""

### Your code here

# data={
#     "name" : "Ivan",
#     "age" : 30,
#     "city" : "Sofia"
# }

# for key,value in data.items():
#     print(f"{key}: {value}")

### EXPECTED OUTPUT:
# name: Ivan
# age: 30
# city: Sofia