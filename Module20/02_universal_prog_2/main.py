# TODO здесь писать код
def crypto(checking_list):
  return [v for i, v in enumerate(checking_list) if is_prime(i)]


def is_prime(num):
  k = 0
  for i in range(1, num + 1):
      if num % i == 0:
          k += 1
  return k == 2


print(crypto('О Дивный Новый мир!'))