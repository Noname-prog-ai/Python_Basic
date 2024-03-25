# TODO здесь писать код
import re


def check_phone_numbers(phone_numbers):
    for number in phone_numbers:
        """Проверяем длину номера"""
        if len(number) != 10:
            print(f'{number}: не подходит')
            continue

        """Проверяем первую цифру номера"""
        if number[0] != '8' and number[0] != '9':
            print(f'{number}: не подходит')
            continue

        """Проверяем, что все остальные символы - цифры"""
        if not re.match(r'^\d+$', number[1:]):
            print(f'{number}: не подходит')
            continue

        print(f'{number}: всё в порядке')


"""Пример списка номеров"""
phone_numbers = ['9999999999', '999999-999', '99999x9999']

"""Проверяем номера"""
check_phone_numbers(phone_numbers)

