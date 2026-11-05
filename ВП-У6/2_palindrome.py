def is_palindrome(n):
    original = abs(n)
    reversed_num = 0
    temp = original
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    if original == reversed_num:
        return 1
    return 0


number = int(input("Въведете число: "))

if is_palindrome(number) == 1:
    print(f"{number} е палиндром")
else:
    print(f"{number} не е палиндром")
