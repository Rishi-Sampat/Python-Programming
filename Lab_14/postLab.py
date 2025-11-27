import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print("Radius:", c.radius)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

#b
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

    def apply_discount(self, percent):
        discount_amount = (percent / 100) * self.price
        self.price -= discount_amount

book1 = Book("Dairy of a Whimpy Kid", "Rishi Sampat", 450)
book2 = Book("Codex Gigas", "Saanvi", 1666)

print("Before Discount:")
book1.display()
book2.display()
print("After 10% Discount on book1:")
book1.apply_discount(10)
book1.display()
