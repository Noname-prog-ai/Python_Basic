# TODO здесь писать код
# Создаем абстрактный базовый класс Shape
from abc import ABC, abstractmethod

class Shape(ABC):
    # Абстрактный метод area, который должны переопределить наследники
    @abstractmethod
    def area(self):
        pass

# Класс Circle наследует от Shape и реализует метод area для вычисления площади круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Класс Rectangle наследует от Shape и реализует метод area для вычисления площади прямоугольника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Класс Triangle наследует от Shape и реализует метод area для вычисления площади треугольника
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Проверка кода:

# Нельзя создавать объекты класса Shape, так как он абстрактный

# Создание объектов классов Circle, Rectangle и Triangle
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площадей фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод площадей фигур
print(f"Площадь круга: {circle_area}")
print(f"Площадь прямоугольника: {rectangle_area}")
print(f"Площадь треугольника: {triangle_area}")


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
