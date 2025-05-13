# TODO здесь писать код
def merge_sorted_lists(list1, list2):
  merged_list = []
  pointer1 = 0
  pointer2 = 0

  while pointer1 < len(list1) and pointer2 < len(list2):
    if list1[pointer1] == list2[pointer2]:
      merged_list.append(list1[pointer1])
      pointer1 += 1
      pointer2 += 1
    elif list1[pointer1] < list2[pointer2]:
      merged_list.append(list1[pointer1])
      pointer1 += 1
    else:
      merged_list.append(list2[pointer2])
      pointer2 += 1

  return merged_list + list1[pointer1:] + list2[pointer2:]


# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)