# TODO здесь писать код
def tpl_sort(tpl):
  for a in tpl:
    if not a is int:
      return tpl
  lst=list(tpl)
  c = 0
  k = 1
  sz = len(lst)
  while True:
    c = 0
    for i in range(sz - k):
      if lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        c += 1
    if c == 0:
      return tuple(lst)
    k += 1

tpl = (6, 3, -1, 8, 4, 10, -5)
tpls = sorted(tpl)
print(tpl_sort(tpls))