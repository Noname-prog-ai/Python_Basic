# TODO здесь писать код
class LRUCache:
    """В конструкторе класса определены три атрибута: "capacity" (емкость кэша), "cache_dict" (словарь для хранения элементов кэша) и "used_keys" (список, отслеживающий порядок использования ключей в кэше)."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        self.used_keys = []

    """Метод "current_cache" возвращает текущее состояние кэша в виде словаря."""
    @property
    def current_cache(self):
        return self.cache_dict

    """Декоратор "@current_cache.setter" определяет метод "cache", который принимает новый элемент кэша в виде пары ключ-значение и обновляет состояние кэша. Если ключ уже существует в кэше, то он перемещается в конец списка "used_keys" (отслеживающего порядок использования ключей), иначе, если емкость кэша достигнута или превышена, удаляется самый старый элемент (самый первый ключ из "used_keys") и добавляется новый элемент в кэш. Затем список "used_keys" и словарь "cache_dict" обновляются соответственно."""
    @current_cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            self.used_keys.remove(key)
        elif len(self.cache_dict) >= self.capacity:
            oldest_key = self.used_keys.pop(0)
            del self.cache_dict[oldest_key]
        self.cache_dict[key] = value
        self.used_keys.append(key)

    """Метод "print_cache" печатает текущее состояние кэша, выводя все пары ключ-значение, отсортированные в порядке использования ключей."""
    def print_cache(self):
        print("lRU Cache:")
        for key in self.used_keys:
            print(f"{key} : {self.cache_dict[key]}")

    """Метод "get" проверяет, есть ли ключ в кэше. Если ключ будет найден, он будет перемещен в конец списка "used_keys" для отслеживания использования. Затем метод возвращает соответствующее значение. Если ключ не найден, возвращается значение None."""
    def get(self, key):
        if key in self.cache_dict:
            self.used_keys.remove(key)
            self.used_keys.append(key)
            return self.cache_dict[key]
        return None

    """Метод "add" добавляет новый элемент кэша. Если ключ уже существует в кэше, то он перемещается в конец списка "used_keys". Иначе, если емкость кэша достигнута или превышена, удаляется самый старый элемент (самый первый ключ из "used_keys") и добавляется новый элемент в кэш. Затем список "used_keys" и словарь "cache_dict" обновляются соответственно."""
    def add(self, key, value):
        if key in self.cache_dict:
            self.used_keys.remove(key)
        elif len(self.cache_dict) >= self.capacity:
            oldest_key = self.used_keys.pop(0)
            del self.cache_dict[oldest_key]
        self.cache_dict[key] = value
        self.used_keys.append(key)


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4