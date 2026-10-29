numbers = [int(x) for x in input("Въведете числа (разделени с интервал): ").split()]
print("Начален списък:", numbers)

new_list = []
for x in numbers:
    if x not in new_list:
        new_list.append(x)

print("Без дубликати:", new_list)
