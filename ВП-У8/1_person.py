class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Здравей, аз съм {self.name} и съм на {self.age} години.")


p1 = Person("Иван", 25)
p2 = Person("Мария", 30)
p1.introduce()
p2.introduce()
