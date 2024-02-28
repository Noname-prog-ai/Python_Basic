# TODO здесь писать код
import random
import time

# Объявляем константу
KARMA_GOAL = 500

# Создаем исключения
class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

def one_day():
    # С вероятностью 1 к 10 выбираем исключение
    if random.randint(1, 10) == 1:
        error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        raise error

    # Возвращаем случайное количество кармы от 1 до 7
    return random.randint(1, 7)

# Открываем файл для записи лога
log_file = open("karma.log", "w")

# Инициализируем счетчик кармы
karma = 0

# Бесконечный цикл до достижения цели кармы
while karma < KARMA_GOAL:
    try:
        karma += one_day()
        time.sleep(1)  # Имитация прохождения времени
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
        # Записываем информацию об исключении в лог
        log_file.write(str(error))
        log_file.write("\n")

# Закрываем файл
log_file.close()