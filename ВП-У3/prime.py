n = int(input("Въведете число: "))

is_prime = n > 1
i = 2
while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(f"{n} е просто число")
else:
    print(f"{n} не е просто число")
