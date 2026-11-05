def square_area(a):
    return a * a


def rectangle_area(a, b):
    return a * b


def right_triangle_area(a, b):
    return a * b / 2


print("1 - квадрат")
print("2 - правоъгълник")
print("3 - правоъгълен триъгълник")
choice = input("Изберете фигура: ")

if choice == "1":
    a = float(input("Страна a = "))
    print(f"Лицето на квадрата е {square_area(a)}")
elif choice == "2":
    a = float(input("Страна a = "))
    b = float(input("Страна b = "))
    print(f"Лицето на правоъгълника е {rectangle_area(a, b)}")
elif choice == "3":
    a = float(input("Катет a = "))
    b = float(input("Катет b = "))
    print(f"Лицето на триъгълника е {right_triangle_area(a, b)}")
else:
    print("Невалиден избор")
