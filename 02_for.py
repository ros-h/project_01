# Задача 2
# Напишите код, который принимает список из чисел и возвращает сумму только положительных чисел в нем.
# например [1,-4,7,12] -> 1 + 7 + 12 = 20
#Вариант 1 - с циклом while
#Вариант 2 с циклом for
lst = [1,-4,7,12]
s = 0
for l in lst:
    if l > 0:
        s += l
print(s)

#вариант 3 с индексом for
#и с функцией range
#print(list(range(100, 200))) #генерация последовательности
total = 0
for ind in range(len(lst)):
    if lst[ind] > 0:
        total += lst[ind]
print(s)
#вариант 4 функция enumerate
total = 0
for i, el in enumerate(lst):
    if el > 0:
        total += el
print(total)
#Варинт 5 Списковое включение (однострочник)
print(sum([n for n in lst if n > 0]))