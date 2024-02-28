import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.start_power * 3

    def attack(self, target):
        attack_power = self.get_power() / 2
        target.take_damage(attack_power)

    def take_damage(self, damage):
        super().take_damage(1.2 * damage)
        if self.get_hp() > 0:
            self.heal(self)

    def heal(self, target):
        target.set_hp(target.get_hp() + self.magic_power)

    def make_a_move(self, friends, enemies):
        target = random.choice(friends)
        if target.get_hp() < target.max_hp * 0.8:
            self.heal(target)
        else:
            self.attack(random.choice(enemies))


class Tank(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.shield_up = False

    def attack(self, target):
        attack_power = self.get_power() / 2
        target.take_damage(attack_power)

    def take_damage(self, damage):
        if self.shield_up:
            self.defense /= 2
            self.set_power(self.get_power() * 2)
        super().take_damage(damage / self.defense)
        if self.shield_up:
            self.defense *= 2
            self.set_power(self.get_power() / 2)

    def raise_shield(self):
        self.shield_up = True
        self.defense *= 2
        self.set_power(self.get_power() / 2)

    def lower_shield(self):
        self.shield_up = False
        self.defense /= 2
        self.set_power(self.get_power() * 2)

    def make_a_move(self, friends, enemies):
        if self.shield_up:
            self.lower_shield()
        else:
            self.raise_shield()
        self.attack(random.choice(enemies))


class Attacker(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target):
        attack_power = self.get_power() * self.power_multiply
        target.take_damage(attack_power)
        self.power_down()

    def take_damage(self, damage):
        super().take_damage(damage * (self.power_multiply / 2))

    def power_up(self):
        self.power_multiply *= 2

    def power_down(self):
        self.power_multiply /= 2

    def make_a_move(self, friends, enemies):
        self.power_up()
        self.attack(random.choice(enemies))
