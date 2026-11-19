class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def show(self):
        print(f"Текуща стойност: {self.value}")


c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c2.increment()

print("Брояч 1:")
c1.show()  # 2
print("Брояч 2:")
c2.show()  # 1
