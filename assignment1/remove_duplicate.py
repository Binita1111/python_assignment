numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("List without duplicates:", unique_numbers)
