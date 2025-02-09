#Tuple: Create a tuple of student records (name, age, grade) and sort by grade.

students_info = [("Masum", 22, 85), ("Jia", 22, 78), ("Nabil", 22, 92), ("Roy", 22, 88)]

final_students = sorted(students_info, key=lambda x: x[2])

print(final_students)