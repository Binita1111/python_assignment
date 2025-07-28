# Program 9: Key with highest value
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

max_key = max(students, key=students.get)
print(f"Topper: {max_key} with {students[max_key]} marks")
