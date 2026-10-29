sentence = input("Въведете изречение: ")

unique_words = set(sentence.split())

print("Брой уникални думи:", len(unique_words))
print("Уникални думи:", ", ".join(sorted(unique_words)))
