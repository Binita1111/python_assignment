# Sort students by their marks
students = {
    "Ram": 80,
    "Sita": 90,
    "Gita": 85
}
sorted_students = dict(sorted(students.items(), key=lambda x: x[1]))
print(sorted_students)
