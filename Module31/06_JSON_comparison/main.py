# TODO здесь писать код
import json
from typing import List, Dict


def dict_diff(dict_1: Dict, dict_2: Dict, diff_keys: List[str]) -> Dict:
    """
    Функция, перебирающая ключи в двух json-файлах на предмет несоответствия значений
    :param dict_1: словарь из первого файла
    :param dict_2: словарь из второго файла
    :param diff_keys: список ключей, которые нужно проверить на изменения
    :return: словарь с различающимися значениями
    """
    diff_dict = {}

    for key in dict_1:
        if isinstance(dict_1[key], dict) and key in dict_2 and isinstance(dict_2[key], dict):
            nested_diff = dict_diff(dict_1[key], dict_2[key], diff_keys)
            if nested_diff:
                diff_dict[key] = nested_diff
        elif key in diff_keys and dict_1[key] != dict_2[key]:
            diff_dict[key] = {'file1': dict_1[key], 'file2': dict_2[key]}

    return diff_dict


with open('json_new.json', 'r') as new_file, open('json_old.json', 'r') as old_file:
    """
    Загрузка данных из json-файлов
    """
    data1 = json.load(new_file)
    data2 = json.load(old_file)

diff_keys = ["services", "staff", "datetime"]
result = dict_diff(data1, data2, diff_keys)
print(result)

"""
Запись результата в json-файл
"""
with open('result.json', 'w') as final:
    json.dump(result, final, indent=4)