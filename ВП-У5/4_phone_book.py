phone_book = {}

for i in range(3):
    name = input(f"Име на контакт {i + 1}: ")
    phone = input(f"Телефон на {name}: ")
    phone_book[name] = phone

search = input("Въведете име за търсене: ")

if search in phone_book:
    print(f"Телефонът на {search} е {phone_book[search]}")
else:
    print(f"Контакт с име {search} не е намерен.")
