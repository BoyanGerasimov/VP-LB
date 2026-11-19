class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, faculty_number):
        super().__init__(name, age)
        self.faculty_number = faculty_number


s = Student("Георги", 20, "F12345")
print(f"Име: {s.name}, Възраст: {s.age}, Факултетен номер: {s.faculty_number}")
