# Функция - это блок кода, который можно вызывать с разными параметрами.
#Ф позволяет реализовать решение для разных словарей
# Ф - это молотилка данных: загружаем значения, на выходе получаем результат

#этапы создания функции
# объявляем с помощью оператора def
def get_topmgr(empl):
    return [n for n,s in empl.items() if s >= 100000]

employees1 = {'Alice' : 100000,
'Bob' : 99817,
'Carol' : 122908,
'Frank' : 88123,
'Eve' : 93121}
employees2 = {'Alice' : 100000,
'Nikita' : 1,
'Masha' : 110000,
'Matvey' : 90000,
'Sasha' : 88123,
'Tanya' : 193121}
#Этап вызова функции
get_topmgr(employees1)
get_topmgr(employees2)

#воспользуемся результатом работы функции
print([employees2[i]*1.5 for i in get_topmgr(employees2)])