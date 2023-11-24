# TODO здесь писать код
def merge(list1, list2):
    res = []
    sz1 = len(list1)
    sz2 = len(list2)
    i1 = 0
    i2 = 0
    sz = 0
    while True:
        if i1 >= sz1:
            for i in range(i2, sz2):
                a = list2[i]
                if sz == 0 or res[-1] != a:
                    res.append(a)
                    sz += 1
            return res
        if i2 >= sz2:
            for i in range(i1, sz1):
                a = list1[i]
                if sz == 0 or res[-1] != a:
                    res.append(a)
                    sz += 1
            return res
        a = list1[i1]
        b = list2[i2]
        if a < b:
            if sz == 0 or res[-1] != a:
                res.append(a)
                sz += 1
            i1 += 1
        if b < a:
            if sz == 0 or res[-1] != b:
                res.append(b)
                sz += 1
            i2 += 1
        if a == b:
            if sz == 0 or res[-1] != b:
                res.append(b)
                sz += 1
            i2 += 1
            i1 += 1


x1 = [1, 1, 2, 2, 4, 5, 5, 5, 6, 6, 7, 8, 9]
x2 = [-1, -1, 0, 0, 1, 2, 3, 7, 8, 9, 9, 9]

x = merge(x1, x2)



# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge(list1, list2)
print(merged)