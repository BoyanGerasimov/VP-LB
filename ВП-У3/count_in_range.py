low = float(input("Долна граница: "))
high = float(input("Горна граница: "))

count = 0
for i in range(1, 11):
    x = float(input(f"Число {i}: "))
    if low <= x <= high:
        count += 1

print(f"Брой числа в [{low}; {high}]: {count}")
