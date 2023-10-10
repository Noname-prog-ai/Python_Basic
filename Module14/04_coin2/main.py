# TODO здесь писать код
def find_monetka(c1,c2,r):
    if c1<=r and c2<=r:
        print('где-то рядом')
    else:
        print('в области нет')
print('Введите координаты монетки:')
x=float(input("X: "))
y=float(input("Y: "))
r=int(input("Введите радиус: "))

find_monetka(x,y,r)

