# TODO здесь писать код
import json
from typing import List, Dict

with open('json_new.json', 'r') as new_file, open('json_old.json', 'r') as old_file:
    """Загрузка данных из json-файлов"""
    data1 = json.load(new_file)
    data2 = json.load(old_file)


def dict_diff(dict_1: Dict, dict_2: Dict, diff: List) -> Dict:
    """
    Функция, перебирающая ключи в двух JSON-файлах на предмет не соответствия значений
    """

    for key in dict_1:
        if isinstance(dict_1[key], dict):
            dict_diff(dict_1[key], dict_2[key], diff)
        if dict_1[key] != dict_2[key] and key in diff:
            dict_of_values[key] = {'file1': dict_1[key], 'file2': dict_2[key]}
    return dict_of_values


dict_of_values: Dict = {}
diff_list: List[str] = ["services", "staff", "datetime"]
result: Dict = dict_diff(data1, data2, diff_list)
print(result)

"""Запись результата в json-файл"""
with open('result.json', 'w') as final:
    json.dump(result, final, indent=4,)