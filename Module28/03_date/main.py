# TODO здесь писать код

class Date:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    """
    В данном примере мы создаем класс Date с приватными атрибутами _day, _month, _year,
    которые устанавливаются при создании объекта через конструктор __init__.
    Мы используем декораторы @classmethod для создания классового метода from_string,
    который принимает строку в формате dd-mm-yyyy и возвращает объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
    """
    @classmethod
    def from_string(cls, date_str: str) -> "Date":
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

    def is_date_valid(self, date_str: str) -> bool:
        day, month, year = map(int, date_str.split('-'))
        """Проверка валидности даты"""
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:
            return True
        else:
            return False

    """Метод is_date_valid принимает строку в формате dd-mm-yyyy и проверяет корректность чисел даты. Если дата валидна, то возвращается True, иначе - False."""

    def __str__(self) -> str:
        return f"день: {self._day}\tмесяц: {self._month}\tгод: {self._year}"

    """Метод __str__ переопределяет стандартный метод __str__ и возвращает строку, содержащую значения дня, месяца и года объекта класса Date."""


date = Date.from_string('10-12-2077')
print(date)
print(date.is_date_valid('10-12-2077'))
print(date.is_date_valid('40-12-2077'))
