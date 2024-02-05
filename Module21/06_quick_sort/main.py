# TODO здесь писать код
def qsort(arr):
  if len(arr) <= 1:
      return arr
  sep=arr[-1]
  left=[]
  mid=[]
  right=[]
  for a in arr:
      if a < sep:
          left.append(a)
      elif a==sep:
          mid.append(a)
      else:
          right.append(a)
  return qsort(left)+mid+qsort(right)

x=[4, 9, 2, 7, 5]

print(qsort(x))
