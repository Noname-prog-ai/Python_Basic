nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код
for i in nice_list:
  if not isinstance(i, list):
    n += [i]
  else:
    def f(y):
      global n
      for k in y:
        if not isinstance(k, list):
          n += [k]
        else:
          f(k)
    f(i)
print(n)