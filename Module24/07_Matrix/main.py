# TODO здесь писать код
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]
    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны быть одинакового размера для вычитания.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result
    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result
    def transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[j][i] = self.data[i][j]
        return result
    def __str__(self):
        output = ""
        for row in self.data:
            output += "\t".join(str(element) for element in row)
            output += "\n"
        return output




# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())