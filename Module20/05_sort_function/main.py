# TODO здесь писать код
def tpl_sort(tpl):
  for element in tpl:
    if not isinstance(element, int):
      return tpl
  return tuple(sorted(tpl))

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))