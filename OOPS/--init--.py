class Animals:
    def __init__(self, name: str, age: int, color: str):

        assert age >= 0, f"Age {age} is not a valid age"

        self.name = name
        self.age = age
        self.color = color


class Items:
    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, f"Price {price} is not a valid price"
        assert quantity >= 0, f"Quantity {quantity} is not a valid quantity"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity


dog = Animals("Bruno", 3, "Black")
cat = Animals("Meow", 2, "White")

phone = Items("Phone", 2, 15000)
laptop = Items("Laptop", 1, 70000)

print(phone.calculate_price())
print(laptop.calculate_price())
