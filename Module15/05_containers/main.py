# TODO здесь писать код
def f(x):
    if x < 1 or x > 200:
        print('Вес є [1;200]'); return False
    else: return True
quantity=int(input('Количество контейнеров: '))
a,i=[],0


while i < quantity:
    weight = int(input\
    ('Введите вес контейнера: '))
    if f(weight): a.append(weight); i+=1
while True:
    weight_new = int(input\
    ('Введите вес нового контейнера: '))
    if f(weight_new): break
for i in range(quantity):
    if weight_new >= a[i]: print('Номер, который получит новый контейнер:', i+1); break