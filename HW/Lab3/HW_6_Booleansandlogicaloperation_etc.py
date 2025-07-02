# logical_expressions_and_conditional_statements_tasks.py

# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes a number as input and checks if it is positive, negative, or zero.
"""

### Your code here

# number=input("Enter a real number: ")
# number=float(number)
# if number>0:
#     print(f'Number {number} is positive.')
# elif number<0:
#     print(f'Number {number} is negative.')
# else:
#     print(f'Number {number} is 0.')

### EXPECTED OUTPUT:
# "Enter a number: -2.45"
# "Number -2.45 is negative."


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program to check whether a year input by the user is a leap year or not. Use the rule for Gregorian calendar:
    Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
    For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
"""

### Your code here

# year=input("Enter a year: ")
# year=int(year)
# if year%4==0 and year%400==0 and year%100==0:
#     print(f'Year is a leap year')
# elif year%4==0 and not year%100==0:
#     print(f'Year is a leap year')
# else:
#     print (f'Year is not a leap year')



### EXPECTED OUTPUT:
# Enter a year: 2024
# 2024 is a leap year

# Enter a year: 2050
# 2050 is not leap year.


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Develop a simple temperature converter program that converts temperatures from Fahrenheit to Celsius and vice versa based on user choice. Make a user-friendly interface as given in EXPECTED OUTPUT:.

    Temperature conversions use the following formulas:
    Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
    Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
"""

### Your code here

# print(f'{10*"*"}Fahrenheit/Celsius Converter {11*"*"}')
# print(f'# 1 => Convert to Fahrenheit                     #')
# print(f'# 2 => Convert to Celsius                        #')
# print(f'{50*"*"}')
# choice=input("Enter your choice [1/2]: ")
# if int(choice)==1:
#     temp=input("Enter temperature in C: ")
# else:weight (Severe thinness)
#     temp=input("Enter temperature in F: ")
# if int(choice)==1:
#     print(f'{round(float(temp),1)}C = {round(float(temp)*(9/5)+32,1)}F')
# else:
#     print(f'{round(float(temp),1)}F = {round((float(temp)-32)*(5/9),1)}C')


### EXPECTED OUTPUT:
# **********Fahrenheit/Celsius Converter ***********
# # 1 => Convert to Fahrenheit                     #
# # 2 => Convert to Celsius                        #
# **************************************************
# Enter your choice [1/2]: 1
# Enter temperature in C: 20
# 20.0C = 68.0F


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a Body mass index (BMI) calculator program, which asks the user for:
    weight in kilograms
    height in meters

    Calculate the BMI = W / (H*H)
    where:
    W = weight in kilograms
    H = height in meters

    Display to the user the BMI and basic category, using next table:

    | ------------------------------- | ----------- |
    | category                        | BMI         |
    | ------------------------------- | ----------- |
    | Under   | < 16.0      |
    | Underweight (Moderate thinness) | 16.0 - 16.9 |
    | Underweight (Mild thinness)     | 17.0 - 18.4 |
    | Normal range                    | 18.5 - 24.9 |
    | Overweight (Pre-obese)          | 25.0 - 29.9 |
    | Obese (Class I)                 | 30.0 - 34.9 |
    | Obese (Class II)                | 35.0 - 39.9 |
    | Obese (Class III)               | ≥ 40.0      |
    | ------------------------------- | ----------- |
"""

### Your code here

# W=input("Enter weight in kilograms: ")
# H=input("Enter height in meters: ")
# W=float(W)
# H=float(H)
# BMI=W/(H**2)
# if BMI<16.0:
#     print(f'Your BMI = {round(BMI,2)}, Category: Underweight (Big bad thinness)')
# elif 16.0<=BMI<16.95:
#     print(f'Your BMI = {round(BMI,2)}, Category: Underweight (Moderate thinness)')
# elif 16.95<=BMI<18.45:
#     print(f'Your BMI = {round(BMI,2)}, Category: Underweight (Mild thinness)')
# elif 18.45<=BMI<24.95:
#     print(f'Your BMI = {round(BMI,2)}, Category: Normal range')
# elif 24.95<=BMI<29.95:
#     print(f'Your BMI = {round(BMI,2)}, Category: Overweight (Pre-obese)')
# elif 29.95<=BMI<34.95:
#     print(f'Your BMI = {round(BMI,2)}, Category: Obese (Class I)')
# elif 34.95<=BMI<39.95:
#     print(f'Your BMI = {round(BMI,2)}, Category: Obese (Class II)')
# elif BMI>=39.95:
#     print(f'Your BMI = {round(BMI,2)}, Category: Obese (Class III)')

# print(round(BMI,2))
### EXPECTED OUTPUT:
# Enter weight in kilograms: 92
# Enter height in meters: 1.78
# Your BMI = 29.04, Category: Overweight (Pre-obese)