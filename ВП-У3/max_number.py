n = int(input("n = "))
while n <= 0:
    n = int(input("n трябва да е > 0, n = "))

max_num = int(input("Число 1: "))
for i in range(2, n + 1):
    x = int(input(f"Число {i}: "))
    if x > max_num:
        max_num = x

print(f"Най-голямото число е: {max_num}")
