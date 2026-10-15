n = int(input("Въведете номер на ден (1-7): "))

if n == 1:
    print(f"{n} - Понеделник")
elif n == 2:
    print(f"{n} - Вторник")
elif n == 3:
    print(f"{n} - Сряда")
elif n == 4:
    print(f"{n} - Четвъртък")
elif n == 5:
    print(f"{n} - Петък")
elif n == 6:
    print(f"{n} - Събота")
elif n == 7:
    print(f"{n} - Неделя")
else:
    print(f"{n} не е валиден номер на ден")
