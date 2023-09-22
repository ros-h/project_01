import sqlite3 as sql

# Задача 4.1.
# Домашнее задание на SQL
# В базе данных teacher создайте таблицу Students
# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)
# Наполните таблицу следующими данными:
Students =[
[201, 'Иван', 1],
[202, 'Петр', 2],
[203, 'Анастасия', 3],
[204, 'Игорь', 4]
]
db = sql.connect('teatchers.db')
req = db.cursor()
req.execute("CREATE TABLE IF NOT EXISTS Students(Student_Id INTEGER, Student_Name TEXT, School_Id INTEGER PRIMARY KEY);")
try:
    for s in Students:
        req.execute("INSERT INTO Students (Student_Id, Student_Name, School_Id) VALUES(?,?,?);",(s[0], s[1], s[2]))
    db.commit()
except:
    pass

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.
# Формат вывода:
# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

id = int(input('Введите ID студента  '))
ans = req.execute("SELECT Student_Name, School_Id FROM Students WHERE Student_Id = ?", (id,)).fetchone()
school = req.execute("SELECT School_Name FROM School WHERE School_Id = ?", (int(ans[1]),)).fetchone()
print(f"ID Студента: {id}")
print(f"Имя студента: {ans[0]}")
print(f"ID школы: {ans[1]}")
print(f"Название школы: {school[0]}")
db.close()