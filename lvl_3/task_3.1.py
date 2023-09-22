import random
# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

class Matrix():
#инициализация
    def __init__(self, h, w, v=0):
        self.A = [[ [v] for i in range(w)] for j in range(h)]

#добавить строку
    def add_str(self, v=0):
        self.A.append([ [v] for i in range(len(self.A[0]))])

#добавить столбец
    def add_column(self, v=0):
        for i in self.A:
            i.append([v])

#смена значения отдельной ячейки
    def set_cell(self, s, c, value):
#поправка на то, что в списке отсчет начинается с нуля
        s = s - 1
        c = c - 1
# проверяем, не выходят ли указанные координаты ячейки за пределы матрицы
        if s < len(self.A) and c <= len(self.A[s]):
            self.A[s][c] = [value]

#получаем значение отдельной ячейки
    def get_cell(self, h, w):
        h = h - 1
        w = w - 1
        if h < len(self.A) and w <= len(self.A[h]):
            return self.A[h][w]
        else:
            print("Значение за пределами матрицы")

#заполнение матрицы одним значением
    def set_all(self, value):
        for i in range(len(self.A)):
            for j in range(len(self.A[i])):
                self.set_cell(i,j,value)

#количество  строк и стоблцов
    def h_w(self):
        str = len(self.A)
        h = str - 1
        column = len(self.A[h])
        return str,column

#вывод матрицы на экран ячейками  
    def matrix_print(self):
        for h in range(len(self.A)):
            for w in range(len(self.A[h])):
                print(self.A[h][w], end = ' ')
        print()
#вывод матрицы на экран построчно  
    def matrix_print_sq(self):
        for h in range(len(self.A)):
            print(self.A[h])
        print()

#Создаем экземляр с заданным значением
h, w = 3, 3
matrix = Matrix(h,w)
#Добавляем строку
matrix.add_str(7)
matrix.matrix_print_sq()

#добавляем столбец
matrix.add_column(4)
matrix.matrix_print_sq()

#Присваиваем значение 1 ячейке по координатам 2 строка, 1 столбец
s, c = 2, 1
matrix.set_cell(s,c,8)
matrix.matrix_print_sq()

#Выводим на экран значение ячейки по координатам 2 строка, 3 столбец
s, c = 2, 4
print(f"Значение ячейки в строке {s} столбце {c} равно {matrix.get_cell(s,c)}")

#Выводим матрицу на экран построчно
matrix.matrix_print_sq()

#Выводим матрицу на экран в виде перечня ячеек
matrix.matrix_print()

#Заполняем все ячейки матрицы значением 5
matrix.set_all(5)
matrix.matrix_print_sq()

#вывод количества строк и столбцов
qnty = matrix.h_w()
print(f"Количество строк {qnty[0]}")