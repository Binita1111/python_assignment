items = ["apple", "banana", "apple", "orange", "banana", "apple"]
count_dict = {}

for item in items:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Count of each item:", count_dict)
