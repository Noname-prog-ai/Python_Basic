# TODO здесь писать код
from random import randint


class Students:
    def __init__(self, name, group, grade):
        self.name = name
        self.group = group
        self.grade = grade

    def average_score(self):
        return sum(self.grade) / len(self.grade)

    def info_student(self):
        print(self.name, self.group, self.grade, self.average_score())


out_student = [
    ['Иванов.И.А: ', '(11) ', [randint(2, 5) for _ in range(5)]],
    ['Самойлов.Р.А: ', '(14) ', [randint(2, 5) for _ in range(5)]],
    ['Смирнов.Н.Ю: ', '(34) ', [randint(2, 5) for _ in range(5)]],
    ['Петров.А.А: ', '(34) ', [randint(2, 5) for _ in range(5)]],
    ['Таибова.П.А: ', '(321) ', [randint(2, 5) for _ in range(5)]],
    ['Фёдоров.О.Р: ', '(21) ', [randint(2, 5) for _ in range(5)]],
    ['Орлов.М.М: ', '(17) ', [randint(2, 5) for _ in range(5)]],
    ['Михайлов.А.Г: ', '(321) ', [randint(2, 5) for _ in range(5)]],
    ['Захаров.И.И: ', '(10) ', [randint(2, 5) for _ in range(5)]],
    ['Кузнецов.В.В: ', '(34) ', [randint(2, 5) for _ in range(5)]]
   ]

lst_student = []

for i in range(len(out_student)):
    lst_student.append(Students(out_student[i][0], out_student[i][1], out_student[i][2]))

sort_students = sorted(lst_student, key=lambda item: item.average_score())

for student in sort_students:
    student.info_student()