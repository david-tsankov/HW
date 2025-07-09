# Task:
# Write a Python program that calculates the total duration (in astronomical hours) of a Python course consisting of 64 academical hours, including the respective breaks.
# Given:
# 1 astronomical hour = 60 minutes
# 1 academical hour = 40 minutes
# The course is structured in sessions, where:
# Each session consists of 4 academical hours
# Each session includes a 20-minute break
# Expected Output
# Total duration in astronomical hours: 48.00
# Copy
# Requirements:
# Your solution should be readable and easy to maintain.
# Write your code in: HW/acad_to_astro_hours.py.

# Solution:

academic_hours=(64*40)/60 #calculates hours spent studying
break_hours=((64/4)*20)/60 #calculates hours spent in breaks
print(f'Total duration in astronomical hours: {academic_hours+break_hours}')