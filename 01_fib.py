# Задача 1: Последовательность Фибоначи
# вариант с while
# fib1, fib2 = 1, 1
# m= input("Номер элемента ряда Фибоначчи: ")
# i = int(m) - 2
# while i > 0:
#  print(fib2)
#  fib1, fib2 = fib2, fib1 + fib2
#  i -= 1
# print("Значение этого элемента:", fib2)
#вариант 2 с циклом for
fib1, fib2 = 1, 1
n = input("Номер элемента")
for el in range(2, int(n)):
 fib1, fib2 = fib2, fib1 + fib2
 print(fib2)