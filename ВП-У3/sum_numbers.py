n = int(input("n = "))

total = 0
for i in range(1, n + 1):
    total += int(input(f"Число {i}: "))

print(f"Сума: {total}")
