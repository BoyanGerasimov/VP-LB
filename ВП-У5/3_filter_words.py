words = input("Въведете думи (разделени с интервал): ").split()
k = int(input("Въведете k: "))

result = tuple(word for word in words if len(word) >= k)

print(f"Думи с дължина >= {k}:", result)
