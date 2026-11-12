class Person:
    def __init__(this, name, family, age, nationality):
        this.name = name
        this.family = family
        this.age = age
        this.nationality = nationality

    def print(this):
        print(f"Име: {this.name} {this.family}, Националност: {this.nationality}")


class Student(Person):
    def __init__(this, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        this.university = university
        this.yearofstudy = yearofstudy

    def print(this):
        super().print()
        print(f"  Университет: {this.university}, Година на обучение: {this.yearofstudy}")


class Lecturer(Person):
    def __init__(this, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        this.university = university
        this.experience = experience

    def print(this):
        super().print()
        print(f"  Университет: {this.university}, Преподавателски стаж: {this.experience} г.")


print("--- Лица ---")
p1 = Person("Иван", "Петров", 25, "българин")
p2 = Person("John", "Smith", 40, "англичанин")
p1.print()
p2.print()
 
print("--- Студенти ---")
s1 = Student("Георги", "Димитров", 20, "българин", "ТУ-София", 2)
s2 = Student("Елена", "Иванова", 22, "българка", "СУ", 4)
s1.print()
s2.print()

print("--- Преподаватели ---")
l1 = Lecturer("Николай", "Стоянов", 52, "българин", "ТУ-София", 25)
l2 = Lecturer("Анна", "Колева", 38, "българка", "УНСС", 10)
l1.print()
l2.print()
