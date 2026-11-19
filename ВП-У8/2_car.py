class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self):
        return f"Кола: {self.brand}, мощност: {self.horsepower} к.с."


car = Car("BMW", 190)
print(car)
