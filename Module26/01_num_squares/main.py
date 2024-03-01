# TODO здесь писать код
# Реализация посредством класса-итератора
class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


# Реализация посредством функции-генератора
def square_generator(n):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1


# Реализация посредством генераторного выражения
def square_expression(n):
    return (x ** 2 for x in range(1, n + 1))


# Получение данных от пользователя
n = int(input("Введите число n: "))

# Генерация последовательности с помощью класса-итератора
iterator = SquareIterator(n)
sequence_iterator = [x for x in iterator]
print("Сгенерированная последовательность с помощью класса-итератора:", sequence_iterator)

# Генерация последовательности с помощью функции-генератора
generator = square_generator(n)
sequence_generator = [x for x in generator]
print("Сгенерированная последовательность с помощью функции-генератора:", sequence_generator)

# Генерация последовательности с помощью генераторного выражения
sequence_expression = [x for x in square_expression(n)]
print("Сгенерированная последовательность с помощью генераторного выражения:", sequence_expression)
