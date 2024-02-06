nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код
def list_unpacking(arr):
  result_list = []

  for el in arr:
    if isinstance(el, list):
      result_list.extend(list_unpacking(el))
    else:
      result_list.append(el)

  return result_list


print(list_unpacking(nice_list))
