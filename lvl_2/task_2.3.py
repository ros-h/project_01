# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    result = ""
    match number:
        case 0:
          result = "Zero"
        case 1:
          result = "One"
        case 2:
          result = "Two"
        case 3:
          result = "Three"
        case 4:
          result = "Four"
        case 5:
          result = "Five"
        case 6:
          result = "Six"
        case 7:
          result = "Seven"
        case 8:
          result = "Eight"
        case 9:
          result = "Nine"
        case _:
          result = "Too much"
    return result

while True:
    print(switch_it_up(int(input())))

