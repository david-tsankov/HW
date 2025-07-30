# legend: ✅-got correct output
#         ❌-couldnt get correct output 

# ---------------------------------------------------------------------------- #
#                             Задачи върху списъци                             #
# ---------------------------------------------------------------------------- #

# --------------------------------- Задача 1. -------------------------------- #✅
# Напишете програма, която чете цели числа въведени от потребителя и ги
# съхранява в списък. Програма трябва да продължи да чете стойности, докато
# потребителят не въведе 0. След това тя трябва да покаже всички стойности, въведени от
# потребителя (с изключение на 0), подредени от най-малката до най-голямата стойност.
# Пример:
#     вход: 2,3,1,6,5,4,2,0
#     изход:1,2,2,3,4,5,6,

# YOUR CODE HERE
# list1=[]
# def user_input(x=None):
#     while x!=0:
#         x=int(input("Enter a whole number: "))
#         list1.append(x)
#     return list1

# def sorting_list():
#     del list1[-1]
#     new_list=[]
#     lenght=len(list1)
#     for i in range(lenght):
#         index=0
#         current_MIN=list1[0]
#         for i in range((len(list1))):
#             if current_MIN<list1[index]:
#                 pass
#             else:
#                 current_MIN=list1[index]
#             index+=1
#         new_list.append(current_MIN)
#         list1.remove(current_MIN)
#     return new_list
        
# user_input()
# print(sorting_list())

# --------------------------------- Задача 2. -------------------------------- #✅
# Да се създаде програма, която чете думи като вход от клавиатурата, докато
# потребителят не въведе празен ред. След като потребителят въведе празен ред,
# програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж.
# Думите трябва да се показват в същия ред, в който са били въведени.
# Пример:
#   вход: first; second; first; third; second
#   изход:first; second; third

# YOUR CODE HERE

#### METHOD 1:
# list2=[]
# def user_input():
#     word=None
#     while word!="":
#         word=input("Please enter a word: ")
#         list2.append(word)
#     del list2[-1]
#     return list2

# def remove_duplicted():
#     list_no_duplicates=[]
#     for i in list2:
#         if i not in list_no_duplicates:
#             list_no_duplicates.append(i)
#     return list_no_duplicates

# user_input()
# print(remove_duplicted())
        
#### METHOD 2:
# list2=[]
# def user_input():
#     word=None
#     while word!="":
#         word=input("Please enter a word: ")
#         list2.append(word)
#     del list2[-1]
#     return list2

# def remove_duplicates():
#     dict_no_duplicates=dict.fromkeys(list2)
#     return list(dict_no_duplicates.keys())
# user_input()
# print(remove_duplicates())

# --------------------------------- Задача 3. -------------------------------- #✅
# Да се създаде програма, която да чете цели числа въведени от потребителя,
# докато не бъде въведен празен ред. След като всичките числа са прочетени, програмата
# трябва да показва всички отрицателни числа, последвани от нули, последвани от всички
# положителни числа. Във всяка група номерата трябва да се показват в същия ред, в
# който са въведени от потребителя.
# Пример:
#   вход:   3, -4, 1, 0, -1, 0, -2
#   изход: -4, -1, -2, 0, 0, 3, 1

# YOUR CODE HERE

# def user_input():
#     list_numbers=[]
#     while True:
#         number=input("Please enter a number: ")
#         if number=="":
#             break
#         else:
#             number=int(number)
#             list_numbers.append(number)
#     return list_numbers

# list_numbers=user_input()
# list_sorted_numbers=[]

# def sorting_numbers():
#     for number in list_numbers:
#         if number<0:
#             list_sorted_numbers.append(number)
#     for number in list_numbers:
#         if number==0:
#             list_sorted_numbers.append(number)
#     for number in list_numbers:
#         if number>0:
#             list_sorted_numbers.append(number)
#     return list_sorted_numbers

# print(sorting_numbers())




# --------------------------------- Задача 4. -------------------------------- #
# Напишете програма на Python, която намира най-дългата последователност от
# еднакви елементи в списък. Ако има няколко такива редици с еднаква дължина,
# върнете първата срещната.
# Пример:
#     дадено: numbers=[2, 1, 1, 2, 3, 3, 2, 2, 2],          изход:  [2, 2, 2]
#     дадено: numbers=[4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4],    изход:  [2, 2, 2]

# YOUR CODE HERE

# def user_input():
#     list_numbers=[]
#     while True:
#         number=input("Please enter a number: ")
#         if number=="":
#             break
#         else:
#             number=int(number)
#             list_numbers.append(number)
#     return list_numbers

# list_numbers=user_input()
# list_tupples=[]

# def find_longest_series():
#     index=0
#     tupple_list_repeats=[]
#     for i in range(len(list_numbers)+1):
#         if list_numbers[index]==list_numbers[index+1]:
#            tupple_list_repeats.append(list_numbers[index]) 
#            print(tupple_list_repeats)
#         else:
#             tupple_list_repeats.append(list_numbers[index])
#             list_tupples.append(tupple_list_repeats)
#             print(tupple_list_repeats)
#             print(list_tupples)
#             for i in tupple_list_repeats:
#                 del i
#         index+=1
#     return list_tupples

# print(find_longest_series())

# --------------------------------- Задача 5. -------------------------------- #✅
# Напишете програма, която създава следната квадратна матрица m(n*n), по
# зададен от потребителя размер (n).
# Пример:
#     вход: n=3
#     изход:
#         [1, 4, 7]
#         [2, 5, 8]
#         [3, 6, 9]

#     вход: n=4
#     изход:
#         [1, 5, 9, 13]
#         [2, 6, 10, 14]
#         [3, 7, 11, 15]
#         [4, 8, 12, 16]

# YOUR CODE HERE

# def user_input():
#     n=int(input("Please enter size of matrix (nxn): "))
#     return n

# n=user_input()


# def matrix_row_constructor():
#     matrix={}
#     for i in range(n):
#         matrix[i]=[]
#     return matrix
# matrix=matrix_row_constructor()
# def matrix_row_filler():
#     for key in matrix.keys():
#         for i in range(int(key)+1,n**2+1,n):
#             matrix[key].append(i)
#     return matrix
# matrix=matrix_row_filler()
# def row_extractor():
#     for list in matrix.values():
#         print(list)
#     return
        
# row_extractor()



# --------------------------------- Задача 6. -------------------------------- #
# Напишете програма, която създава следната квадратна матрица (n*n), по
# зададен от потребителя размер (n).
# Пример:
#     вход: n=3
#     изход:
#         [1, 6, 7]
#         [2, 5, 8]
#         [3, 4, 9]

#     вход: n=4
#     изход:
#         [1, 8, 9, 16]
#         [2, 7, 10, 15]
#         [3, 6, 11, 14]
#         [4, 5, 12, 13]

# YOUR CODE HERE

def user_input():
    n=int(input("Please enter size of matrix (nxn): "))
    return n
n=user_input()
def matrix_row_constructor():
    matrix={}
    for i in range(n):
        matrix[i]=[]
    return matrix
matrix=matrix_row_constructor()
def matrix_row_filler():
    for key in matrix.keys():
        for i in range(n*int(key)+1,(int(key)+1)*n+1,1):
            matrix[key].append(i)
    return matrix
matrix=matrix_row_filler()
def row_inverter():
    for key in matrix.keys():
        if key in range(1,n,2):
            matrix[key]=matrix[key][::-1]
    return matrix
matrix=row_inverter()
def matrix_transposer():

# --------------------------------- Задача 7. -------------------------------- #
# Напишете програма, която намира всички последователности от поне два еднакви
# елемента в списък и ги показва. Редът на показването няма значение.

# Пример:
#     вход: numbers=[2, 1, 1, 2, 3, 3, 2, 2, 2, 1],
#     изход:
#           [1,1]
#           [3,3]
#           [2,2,2]

#     вход: numbers=[4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4],
#     изход:
#          [4, 4]
#          [2, 2, 2]
#          [3, 3]
#          [4, 4, 4]


# YOUR CODE HERE
