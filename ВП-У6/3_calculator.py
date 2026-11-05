def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


op = input("Действие (+, -, *, /): ")
a = int(input("a = "))
b = int(input("b = "))

if op == "+":
    print(f"{a} + {b} = {add(a, b)}")
elif op == "-":
    print(f"{a} - {b} = {subtract(a, b)}")
elif op == "*":
    print(f"{a} * {b} = {multiply(a, b)}")
elif op == "/":
    if b == 0:
        print("Грешка: деление на нула!")
    else:
        print(f"{a} / {b} = {divide(a, b)}")
else:
    print("Невалидно действие")
