# TODO здесь писать код
import random


def main():
  team1 = [round(random.uniform(5, 10), 2) for i in range(20)]
  team2 = [round(random.uniform(5, 10), 2) for i in range(20)]
  winners = list(map(max, team1, team2))

  print(f"Первая команда: {team1}")
  print(f"Вторая команда: {team2}")
  print(f"Победители тура: {winners}")

if __name__ == '__main__':
  main()