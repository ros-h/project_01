# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("") -> "Oh, no"

def remove_exclamation_marks(s):
    arr = s.split("!")
    result = ""
    for i in arr:
        result = result + i
    return result

str = "Oh, no!!!"
print(remove_exclamation_marks(str))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == "!":
        result=s[:-1]
    else:
        result=s
    return result

str = "Oh, no!!!"
print(remove_last_em(str))

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    result = ""
    arr = s.split(" ")
    for i in arr:
        if i.count("!") == 1:
            pass
        else:
            result = result + i
    return result

str = "Hi! Hi!! Hi!"
print(remove_word_with_one_em(str))
