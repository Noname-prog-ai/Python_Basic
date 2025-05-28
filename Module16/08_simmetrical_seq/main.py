# TODO здесь писать код
n = int(input("Кол-во чисел: "))
arr = []
for i in range(n):
    arr.append(int(input("Число: ")))

if arr == arr[::-1]:
    print("Нужно приписать чисел: 0")
else:
    copy_arr = arr.copy()
    count = 0
    while copy_arr != copy_arr[::-1]:
        count += 1
        copy_arr = arr.copy()
        for i in range(count):
            copy_arr.append(copy_arr[count-i-1])
            print(f"Нужно приписать чисел: {count}")
            print(f"Сами числа: {copy_arr[-count:][::-1]}") 
