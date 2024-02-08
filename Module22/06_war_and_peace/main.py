# TODO здесь писать код
import zipfile

archive = " "  # Путь к архиву.
directory_to_extract_to = " "  # Путь, куда будет распакован архив.
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall(directory_to_extract_to)

# Дальше повторение прошлой задачи, с маленькими изменениями:

str_open = open("# Путь к файлу, который распаковали", 'r', encoding='utf-8')
list_file = str_open.read()
count_dict = {}
count_letter = 0
for letter in list_file:
    if (letter.isalpha()):
        x = count_dict.get(letter, 0)
        count_dict[letter] = x + 1
        count_letter += 1
count_letter_dict = [(k, "{:8.6f}".format(count_dict[k] / count_letter)) for k in count_dict.keys()]
str_open.close()
count_letter_dict.sort(key=lambda x: x[1], reverse=True)
print()
for i in count_letter_dict:
    print(i[0] + " " + i[1])
