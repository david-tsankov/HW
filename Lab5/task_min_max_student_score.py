student_scores={
    "Ivan" : 5.0,
    "Alex" : 3.5,
    "Maria" : 5.5,
    "Georgy" : 5.0
}
#hint:use min(), max()

# max_score=max(student_scores.values()) <----- Method doesnt work, as cant retreive key based on value
# max_name=student_scores.get(max_score)
# min_score=min(student_scores.values())
# min_name=student_scores.get(min_score)

# print(f"{max_name} - {max_score}")
# print(f"{min_name} - {min_score}")

for name, grade in student_scores.items():
    if grade == max(student_scores.values()):
        print(f"{name} - {grade}")
    if grade == min(student_scores.values()):
        print(f"{name} - {grade}")