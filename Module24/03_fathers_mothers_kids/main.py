# TODO здесь писать код
import random


class Parent:

    def __init__(self, name, age, list_of_children):
        self.name = name
        self.age = age
        self.list_of_children = list_of_children

    def report_information_about_yourself(self):
        children_names = [f"Ребенок {x.name}" for x in self.list_of_children]
        print('\nИнформация о родителе.')
        print(f'Имя: {self.name}\n' 
              f'Возраст: {self.age}\n' 
              f'Дети: {str(children_names)}')

    def soothe_the_child(self, child_object):
        child_object.state_of_calm = 1
        print(f'Ребенок {child_object.name} был успокоен!')

    def feed_the_child(self, child_object):
        child_object.state_of_hunger = 1
        print(f'Ребенок {child_object.name} накормлен!')


class Child:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.states_of_calm = {1: 'Спокоен', 2: 'Неспокоен'}
        self.states_of_hunger = {1: 'Сытый', 2: 'Голоден'}
        self.state_of_calm = random.choice(list(self.states_of_calm.keys()))
        self.state_of_hunger = random.choice(list(self.states_of_hunger.keys()))

    def checking_the_child_state_of_mind(self):
        print(f'Ребенок {self.name} {self.states_of_calm[self.state_of_calm]}!')

    def checking_your_child_hunger(self):
        print(f'Ребенок {self.name} {self.states_of_hunger[self.state_of_hunger]}!')


parent_name = input('Введите имя родителя: ')
parent_age = int(input('Введите возраст родителя: '))
list_of_children_names = list(map(str, input('Введите имя ребенка ' 
                                             '(если их несколько, введите через пробел): ').split()))

list_of_ages = []
for i_index, i_child in enumerate(list_of_children_names, start=1):
    child_age = int(input(f'{i_index}. Введите возраст ребенка {i_child}: '))
    if parent_age - child_age >= 16:
        list_of_ages.append(child_age)
    else:
        print('Ошибка! Неверная разница в возрасте.')
        exit(1)

child_properties = []
for first_list, second_list in zip(list_of_children_names, list_of_ages):
    child_properties.append(Child(first_list, second_list))

new_parent = Parent(parent_name, parent_age, child_properties)

for child_object in new_parent.list_of_children:
    child_object.checking_the_child_state_of_mind()
    child_object.checking_your_child_hunger()

print('---------------------------------------')
for child_object in new_parent.list_of_children:
    if child_object.state_of_calm == 2:
        new_parent.soothe_the_child(child_object)
    if child_object.state_of_hunger == 2:
        new_parent.feed_the_child(child_object)
