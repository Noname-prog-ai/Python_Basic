# TODO здесь писать код
"""Определение базового класса Property"""
class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        pass

"""Определение класса Apartment, производного от Property"""
class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 1000

"""Определение класса Car, производного от Property"""
class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 200

"""Определение класса CountryHouse, производного от Property"""
class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 500

"""Функция для взаимодействия с пользователем"""
def main():
    total_money = int(input("Введите количество денег: "))
    property_worth = int(input("Введите стоимость имущества: "))

    # Создание экземпляров классов и вычисление налога
    apartment = Apartment(property_worth)
    car = Car(property_worth)
    country_house = CountryHouse(property_worth)

    apartment_tax = apartment.calculate_tax()
    car_tax = car.calculate_tax()
    country_house_tax = country_house.calculate_tax()

    # Вывод результатов на экран
    print("Налог на квартиру:", apartment_tax)
    print("Налог на машину:", car_tax)
    print("Налог на дачу:", country_house_tax)

    total_tax = apartment_tax + car_tax + country_house_tax
    if total_money < total_tax:
        print("Не хватает денег:", total_tax - total_money)
    else:
        print("Денег хватает")

# Вызов основной функции
if __name__ == "__main__":
    main()