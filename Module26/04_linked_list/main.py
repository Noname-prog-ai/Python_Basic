# TODO здесь писать код
"""Класс Node представляет узел списка и имеет два атрибута: data (содержит данные узла) и next (ссылка на следующий узел)."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""Класс LinkedList представляет сам связный список и имеет атрибут head (ссылка на первый узел в списке)."""
class LinkedList:
    def __init__(self):
        self.head = None

    """Метод append добавляет новый узел в конец списка."""
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    """Метод get возвращает данные узла по указанному индексу."""
    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None

    """Метод remove удаляет узел по указанному индексу."""
    def remove(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            current = self.head
            count = 0
            previous = None
            while current and count < index:
                previous = current
                current = current.next
                count += 1
            if current:
                previous.next = current.next

    """Метод __iter__ позволяет проходить по элементам связного списка при помощи цикла for ... in ...."""
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    """Метод __str__ возвращает строковое представление списка."""
    def __str__(self):
        return '[' + ' '.join(str(data) for data in self) + ']'

"""Последние строки кода иллюстрируют использование созданного списка и вызов нескольких его методов для демонстрации работы реализации."""
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)