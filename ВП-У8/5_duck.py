class Flyer:
    def fly(self):
        print("Летя в небето")


class Swimmer:
    def swim(self):
        print("Плувам във водата")


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
duck.fly()
duck.swim()
print(Duck.mro())
