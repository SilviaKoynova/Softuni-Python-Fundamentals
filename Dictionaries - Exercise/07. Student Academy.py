n = int(input())
grades = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)
filtered_grade = {}
for student_name, grades in grades.items():
    avr_grade = sum(grades) / len(grades)
    if avr_grade >= 4.50:
        filtered_grade[student_name] = avr_grade
sorted_best_students = sorted(filtered_grade.items(), key=lambda kvp: kvp[1], reverse=True)
for student_name, grade in sorted_best_students:
    print(f"{student_name} -> {grade:.2f}")
