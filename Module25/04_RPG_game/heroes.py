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

    def is_alive(self):  # жив или мёртв
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нет кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        pass

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ",
              round(damage), ". Осталось здоровья - ",
              round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию,
        # чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
        self.magic_power = self.get_power() * 3

    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * 1.2))
        super().take_damage(damage)

    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    def heal(self, target):
        target.set_hp(target.get_hp() + self.magic_power)

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии
    # выполняет ОДНО из действий (атака, исцеление) на выбранную им цель
    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        target_of_heal = friends[0]
        min_health = target_of_heal.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_heal = friend
                min_health = target_of_heal.get_hp()

        if min_health < 60:
            print("исцеляет", target_of_heal.name)
            self.heal(target_of_heal)
        else:
            if not enemies:
                return
            print("атакует -", enemies[0].name)
            self.attack(enemies[0])
        print('\n')

        # if enemies:
        #     print('атакует - {}'.format(enemies[0].name))
        #     self.attack(enemies[0])
        # else:
        #     print('Нет подходящей цели для атаки.')
        print('\n')


class Tank(Hero):
    # Танк:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
        self.defense = 1
        # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
        self.shield_up = False

    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage / self.defense))
        super().take_damage(damage)

    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    def raise_shield(self):
        if not self.shield_up:
            self.shield_up = True
            self.defense *= 2
            self.set_power(self.get_power() / 2)
            print('{} поднимает щит!'.format(self.name))

    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    def lower_shield(self):
        if self.shield_up:
            self.shield_up = False
            self.defense /= 2
            self.set_power(self.get_power() * 2)
            print('{} опускает щит!'.format(self.name))

        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
        # поднять щит/опустить щит) на выбранную им цель

        print('\n')

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        if not enemies:
            return
        if self.get_hp() > 70:
            if self.shield_up == False:
                print("атакует двуручным оружием -", enemies[0].name)
                self.attack(enemies[0])
            else:
                self.lower_shield()
                print('{} опускает щит!'.format(self.name))

        else:
            if self.shield_up == True:
                print('атакует из-за щита - {}'.format(enemies[0].name))
                self.attack(enemies[0])
            else:
                self.raise_shield()
                print('{} поднимает щит!'.format(self.name))

        print('\n')


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        # - коэффициент усиления урона (входящего и исходящего)
        self.power_multiply = 1

    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        # после нанесения урона - вызывается метод ослабления power_down.
        self.power_down()

    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * (self.power_multiply / 2)))
        super().take_damage(damage)

    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    def power_up(self):
        self.power_multiply *= 2

    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    def power_down(self):
        self.power_multiply /= 2

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')

        if self.power_multiply < 2:
            print('Усиливаемся!')
            self.power_up()
        else:
            target_of_attack = None
            min_health = float('inf')

            for enemy in enemies:
                if 0 < enemy.get_hp() < min_health:
                    target_of_attack = enemy
                    min_health = enemy.get_hp()

            if target_of_attack:
                print('атакует - {}.'.format(target_of_attack.name))
                self.attack(target_of_attack)
            else:
                print('Нет подходящей цели для атаки. Восстанавливает силы')

        super().make_a_move(friends, enemies)
        print('\n')