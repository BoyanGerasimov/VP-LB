text = input("Въведете текст: ")

counts = {}
for ch in text:
    if ch != " ":
        counts[ch] = counts.get(ch, 0) + 1

if counts:
    best = max(counts, key=counts.get)
    print(f"Най-често срещан символ: '{best}' ({counts[best]} пъти)")
else:
    print("Няма символи за броене.")
