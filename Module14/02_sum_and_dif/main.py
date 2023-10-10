# TODO здесь писать код
number = int(input('Введите число: '))
suma = 0
def suma_number(number):
   global suma
   while number > 0:
       digit = number % 10
       suma = suma + digit
       number = number // 10
   print('Сумма чисел:', suma)

suma_number(number)
digitcount = 0
def count_number(number):
   global digitcount
   countnumber = number
   while countnumber > 0:
       digitcount += 1
       countnumber = countnumber // 10
   print('Кол-во цифр в числе:', digitcount)
count_number(number)
def differ(suma, digitcount):
   diff = suma - digitcount
   print('Разность суммы и кол-ва цифр:', diff)
differ(suma, digitcount)