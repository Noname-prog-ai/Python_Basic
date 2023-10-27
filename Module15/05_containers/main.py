# TODO здесь писать код
def f(x):
    if x < 1 or x > 200:
        print('Вес є [1;200]'); return False
    else: return True
n=int(input('Количество контейнеров: '))
a,i=[],0


while i < n:
    b=int(input\
    ('Введите вес контейнера: '))
    if f(b): a.append(b); i+=1
while True:
    X=int(input\
    ('Введите вес нового контейнера: '))
    if f(X): break
for i in range(n):
    if X >= a[i]: print('Номер, который получит новый контейнер:', i+1); break