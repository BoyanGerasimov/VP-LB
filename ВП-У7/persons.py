class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"Име: {self.name} {self.family}, Националност: {self.nationality}")


class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        super().print()
        print(f"  Университет: {self.university}, Година на обучение: {self.yearofstudy}")


class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        super().print()
        print(f"  Университет: {self.university}, Преподавателски стаж: {self.experience} г.")


print("--- Лица ---")
p1 = Person("Иван", "Петров", 25, "българин")
p2 = Person("John", "Smith", 40, "англичанин")
p1.print()
p2.print()

print("--- Студенти ---")
s1 = Student("Георги", "Димитров", 20, "българин", "ТУ-София", 2)
s2 = Student("Елена", "Иванова", 22, "българка", "СУ \"Св. Климент Охридски\"", 4)
s1.print()
s2.print()

print("--- Преподаватели ---")
l1 = Lecturer("Николай", "Стоянов", 52, "българин", "ТУ-София", 25)
l2 = Lecturer("Анна", "Колева", 38, "българка", "УНСС", 10)
l1.print()
l2.print()
