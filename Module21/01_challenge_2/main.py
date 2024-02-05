# TODO здесь писать код
def printNos(n):
  if n > 0:
    printNos(n - 1)
    print(n, end='\n')


n = int(input('Введите num: '))
printNos(n)