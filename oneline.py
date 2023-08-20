#Поиск самых высокооплачиваемых сотрудников. Словарь.
employees = {'Alice' : 100000,
'Bob' : 99817,
'Carol' : 122908,
'Frank' : 88123,
'Eve' : 93121}
#Задача: получить сотрудников с з/п выше 100k
#Вариант 1

# top = []
# for name in employees.keys(): #если убрать .keys() тоже будет работать
#     if employees[name] >= 100000:
#         top.append(name)
# print(top)

#Мой варинт
# for item, val in employees.items():
#     if val >= 100000:
#         print(item, val)

#вариант 2: списковые включения - однострочники
# for i in [1, 2, 3]:
#     print(i**2)
# print(
#     list(i**2 for i in [1, 2, 3]) #Генератор объектов
# )
# top = [employees[n] >= 100000 for n in employees]
# print(top) #[True, False, True, False, False]
top1 = [n for n in employees if employees[n] >= 100000]
top2 = [n for n,s in employees.items() if s >= 100000]
print(top2)