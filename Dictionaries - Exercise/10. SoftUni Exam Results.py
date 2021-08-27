data = input()
students = {}
while not data == "exam finished":
    if 'banned' not in data:
        name, language, grade = data.split('-')
        grade = int(grade)
        if name not in students:
            students[name] = {'language': language, 'grade': grade}
            if language in students[name]['language']:
                students[name]['language'] = language
                if grade > students[name]['grade']:
                    students[name]['grade'] = grade
        else:
            if name in students:
                students[name]['language'] = language
                if grade > students[name]['grade']:
                    students[name]['grade'] = grade
    else:
        name, command = data.split("-")
        del (students[name])

    data = input()

print('Results:')
sorted_results = sorted(students.items(), key=lambda kvp: (-kvp[1]['grade'], kvp[0]))
for user, points in sorted_results:
    print(f"{user} | {points['grade']}")
