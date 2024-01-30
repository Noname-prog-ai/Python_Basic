# TODO здесь писать код
def myzip(a, b):
  return ((a[i], b[i]) for i in range(min(len(a), len(b))))

g = myzip("abcd", (10, 20, 30, 40))

print(g)
print(*g, sep='\n')