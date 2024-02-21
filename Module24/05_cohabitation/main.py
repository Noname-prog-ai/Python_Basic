# TODO здесь писать код
import random

class Person:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.house = House()

    def live_one_day(self):
        dice_number = random.randint(1, 6)

        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50:
            self.work()
        elif dice_number == 1:
            self.work()
        elif dice_number == 2:
            self.eat()
        else:
            self.play()

    def eat(self):
        if self.house.food > 0:
            self.satiety += 10
            self.house.food -= 10
            if self.satiety > 100:
                self.satiety = 100
            print(f"{self.name} поел(а). Сытость: {self.satiety}")
        else:
            print(f"{self.name} не может поесть. В доме нет еды.")

    def work(self):
        self.satiety -= 10
        self.house.money += 50
        print(f"{self.name} поработал(а). Деньги в доме: {self.house.money}")

    def play(self):
        self.satiety -= 10
        print(f"{self.name} поиграл(а). Сытость: {self.satiety}")

    def go_shopping(self):
        self.satiety -= 10
        self.house.food += 50
        self.house.money -= 50
        print(f"{self.name} сходил(а) в магазин за едой. В доме теперь еды: {self.house.food}")

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

person1 = Person("Артем")
person2 = Person("Виктор")
house = House()

for i in range(365):
    print(f"===== День {i + 1} =====")
    person1.live_one_day()
    person2.live_one_day()
    print()
