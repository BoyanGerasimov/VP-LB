n = int(input("Въведете цяло число: "))

digits = tuple(sorted(int(d) for d in str(abs(n))))
reversed_digits = tuple(sorted(digits, reverse=True))

print("Цифри в прав ред:", digits)
print("Цифри в обратен ред:", reversed_digits)
