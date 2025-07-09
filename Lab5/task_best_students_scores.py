student_scores={
    "Ivan" : 5.00,
    "Alex" : 3.50,
    "Maria" : 5.50,
    "Georgy" : 5.00
}

best_student_scores={

}

for name, grade in student_scores.items():
    if grade>4.00:
        best_student_scores[name]=grade
        print(f"{name:<15}-{grade:>5.2f}")

