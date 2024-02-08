# TODO здесь писать код
with open('zen.txt', 'r', encoding='utf-8') as f:
    arr = f.read().splitlines()
print('\n'.join(arr[::-1]))