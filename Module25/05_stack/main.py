# TODO здесь писать код
# Создаем класс Stack, который реализует стек
class Stack:
    def __init__(self):
        self.stack = []  # Создаем пустой стек

    def push(self, item):
        self.stack.append(item)  # Добавляем элемент в стек

    def pop(self):
        if self.is_empty():  # Проверяем, пустой ли стек
            return None
        return self.stack.pop()  # Удаляем и возвращаем верхний элемент

    def is_empty(self):
        return len(self.stack) == 0  # Проверяем, пустой ли стек

# Создаем класс TaskManager, который работает на основе стека
class TaskManager:
    def __init__(self):
        self.tasks = Stack()  # Создаем экземпляр класса Stack для хранения задач

    def new_task(self, task, priority):
        self.tasks.push((task, priority))  # Добавляем задачу в стек

    def remove_task(self, task):
        temp_stack = Stack()  # Создаем временный стек для хранения задач
        removed = False  # Флаг, показывающий, была ли удалена задача
        while not self.tasks.is_empty():
            item = self.tasks.pop()  # Берем верхний элемент из стека
            if item[0] != task:  # Если задача не совпадает, добавляем ее во временный стек
                temp_stack.push(item)
            else:
                removed = True  # Устанавливаем флаг удаления
        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())  # Возвращаем задачи обратно в основной стек
        return removed

    def __str__(self):
        temp_stack = Stack()  # Создаем временный стек для сортировки задач по приоритету
        sorted_tasks = []
        while not self.tasks.is_empty():
            item = self.tasks.pop()  # Берем верхний элемент из стека
            sorted_tasks.append(item)  # Добавляем задачу в список для сортировки
            temp_stack.push(item)  # Добавляем задачу во временный стек
        sorted_tasks.sort(key=lambda x: x[1])  # Сортируем задачи по приоритету
        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())  # Возвращаем задачи обратно в основной стек
        result = ""
        for task in sorted_tasks:
            result += str(task[1]) + " — " + task[0] + "\n"  # Форматируем строку для вывода
        return result.rstrip()  # Удаляем лишние переносы строки

# Основная программа
manager = TaskManager()

manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

print(manager)  # Выводим отсортированный список задач
