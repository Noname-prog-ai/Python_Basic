# TODO здесь писать код
import json


def generate_all_items(structure):
    """
    Рекурсивно обходит JSON-структуру и генерирует все ключи и значения.
    """
    if isinstance(structure, dict):
        for key, elem in structure.items():
            yield key, elem
            yield from generate_all_items(elem)
    elif isinstance(structure, list):
        for elem in structure:
            yield from generate_all_items(elem)


def search_differences(old_info, new_info, target_tags):
    """
    Сравнивает два JSON-объекта и возвращает отличающиеся значения по заданным тегам.
    """

    def check_pair(first_pair, second_pair):
        # Проверяет, что первая пара входит в список целевых тегов и пары не равны.
        return first_pair[0] in target_tags and first_pair != second_pair

    return {
        second_pair[0]: second_pair[1]
        for first_pair, second_pair in zip(generate_all_items(old_info), generate_all_items(new_info))
        if check_pair(first_pair, second_pair)
    }


def main():
    """
    Основная функция программы.
    """
    with open('json_old.json', 'r') as file:
        old_json = json.loads(file.read())

    with open('json_new.json', 'r') as file:
        new_json = json.loads(file.read())

    diff_list = ["services", "staff", "datetime"]
    differences = search_differences(old_json, new_json, diff_list)
    print(differences)


if __name__ == "__main__":
    main()