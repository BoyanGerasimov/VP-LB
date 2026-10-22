n = int(input("Въведете цяло число: "))

numbers = list(range(1, n + 1))
print("Списък:", numbers)

result = dict(zip(numbers, numbers[::-1]))
print("Речник:", result)
