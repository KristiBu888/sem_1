# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Введите трехзначное число: "))

digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10

sum_of_digits = digit1 + digit2 + digit3
print(f"{digit1} + {digit2} + {digit3} = {sum_of_digits}")
