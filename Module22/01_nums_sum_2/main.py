# TODO здесь писать код
with open("numbers.txt", "r") as fi:
    t = sum(int(u) for s in fi for u in s.split())
with open("answer.txt", "w") as fo:
    fo.write(str(t) + '\n')