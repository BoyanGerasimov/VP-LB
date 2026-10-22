n = int(input("Въведете цяло число: "))

digits = tuple(int(d) for d in str(abs(n)))
reversed_digits = digits[::-1]

print("Цифри в прав ред:", digits)
print("Цифри в обратен ред:", reversed_digits)
