class Animal:
    def make_sound(self):
        print("Животното издава звук")


class Dog(Animal):
    def make_sound(self):
        print("Кучето лае: Бав-бав!")


animal = Animal()
dog = Dog()
animal.make_sound()
dog.make_sound()
