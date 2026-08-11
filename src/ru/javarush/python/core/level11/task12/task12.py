# Перегрузка операторов индексации

# Напишите класс Matrix, который будет представлять двумерную матрицу и поддерживать перегрузку операторов индексации ([]).
# Реализуйте методы __getitem__ и __setitem__.

class Matrix:
    def __init__(self, rows, cols):
        if rows < 2 or cols < 2:
            raise ValueError("Rows and columns value must be more than 1 to get a matrix")
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def __setitem__(self, index:tuple, value):
        index1 = index[0]
        index2 = index[1]
        if index1 < 0 or index1 >= len(self.matrix) or index2 < 0 or index2 >= len(self.matrix[0]):
            raise IndexError('Wrong index or indexes')
        self.matrix[index1][index2] = value

    def __getitem__(self, index:tuple):
        index1 = index[0]
        index2 = index[1]
        if index1 < 0 or index1 >= len(self.matrix) or index2 < 0 or index2 >= len(self.matrix[0]):
            raise IndexError('Wrong index or indexes')
        return self.matrix[index1][index2]

# Пример использования
try:
    matrix = Matrix(3, 3)
except ValueError as e:
    print(f"Matrix has to be a matrix: {str(e)}")
else:
    try:
        matrix[0, 0] = 1
    except IndexError as e:
        print(f'Index error: {str(e)}')
    else:
        print(matrix[0, 0])  # Вывод: 1