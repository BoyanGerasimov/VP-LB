a = float(input("a = "))
b = float(input("b = "))
op = input("Действие (+, -, *, /): ")

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b == 0:
        print("Грешка: деление на нула!")
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print("Невалидно действие")
