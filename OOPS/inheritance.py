class Pet:
    def __init__(self, name: str, age: int) -> None:
        # Checking the passed values
        assert age >= 0, f"the {age} is not valid"

        # Assigning the values to the pet
        self.name = name
        self.age = age

    def speak(self):
        print("I dont know what to say")

    def how_many_legs(self):
        print("I have 4 legs")


class Dog(Pet):
    def bark(self):
        print("Bark")

    def speak(self):
        print(f"Hello, i am {self.name} and i am {self.age} years old")


class Cat(Pet):
    def __init__(self, name, age, color: str) -> None:
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(
            f"Hello, i am {self.name} and i am {self.age} years old and i am of {self.color} color"
        )

    def meow(self):
        print("Meow")


p = Pet("bill", 12)
p.speak()
p.how_many_legs()

d = Dog("bruno", 7)
d.speak()
d.bark()
d.how_many_legs()

c = Cat("sily", 5, "white")
c.speak()
c.meow()
c.how_many_legs()
