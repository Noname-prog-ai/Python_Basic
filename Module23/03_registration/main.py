# TODO здесь писать код
def answer(file_str):
    long = len(file_str.split())
    name, mail, age = file_str.split(" ")
    symbol = ("@", ".")
    age = int(age)
    if not isinstance(age, int):
        raise ArithmeticError(f" {age} - возраст не число\n")
    if long < 3:
        raise IndexError(f"НЕ присутствуют все три поля\n")
    if name.isalpha() is False:
        raise NameError(f"{name} - Поле «Имя» содержит НЕ только буквы\n")
    if age not in range(10, 100):
        raise ValueError(f"{age} - Поле «Возраст» вне диапазона 10-100\n")
    for char in symbol:
        if char not in mail:
            raise SyntaxError(f"{mail} - Поле «Имейл» НЕ содержит @ и . (точку)\n")
    return file_str


with open("registrations.txt", "r", encoding="utf-8") as file, \
        open('registration_bad.log', 'a', encoding='utf-8') as error, \
        open('registrations_good.log', 'a', encoding='utf-8') as good:
    for str_in_file in file:
        # print(str_in_file, end="")
        try:
            str_file = answer(str_in_file)
        except (ArithmeticError, IndexError, NameError, ValueError, SyntaxError) as err:
            error.write(str_in_file + str(err) + '\n')
        else:
            good.write(str_in_file + '\n')