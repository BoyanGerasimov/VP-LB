import random

size = int(input("Брой елементи: "))

numbers = [random.randint(1, 100) for i in range(size)]
print("Начален списък:", numbers)

result = []
for i in range(len(numbers)):
    result.append(numbers[i])
    if i < len(numbers) - 1:
        result.append(numbers[i] + numbers[i + 1])

print("Резултат:", result)
