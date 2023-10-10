# TODO здесь писать код
def del1(n):
    for i in range(2, n + 1):
        if (n % i == 0):
            return i

x = int(input("Введите целое число : "))
print("Наименьший делитель, отличный от единицы:", del1(x))