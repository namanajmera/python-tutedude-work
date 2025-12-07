# Dict is s key:value pair
# Dict have the unique keys.

student_marks = {'bio': 90, 'chem': 90, 'math': 90}
print(student_marks)
print(type(student_marks))

print(student_marks['bio'])
print(type(student_marks['chem']))

print(student_marks.get('physics'))
print(type(student_marks.get('physics')))

student_marks_sem2 = {'c': 90, 'java': 76, 'python': 80}
print(student_marks_sem2)

student_marks.update(student_marks_sem2)
print(student_marks)


