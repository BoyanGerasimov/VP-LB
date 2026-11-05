def replace_greater(numbers, limit):
    for i in range(len(numbers)):
        if numbers[i] > limit:
            numbers[i] = 0


numbers = [int(x) for x in input("Въведете числа, разделени с интервал: ").split()]
limit = int(input("Въведете число: "))

replace_greater(numbers, limit)
print(f"Резултат: {numbers}")
