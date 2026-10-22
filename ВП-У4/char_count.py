text = input("Въведете текст: ")

counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

print(f"Речникът се състои от {len(counts)} елемента:")
for key in sorted(counts):
    print(f"{key}:{counts[key]}", end="  ")
print()
