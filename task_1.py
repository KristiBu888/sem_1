# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Введите трехзначное число: "))

digit1 = n // 100
digit2 = (n % 100) // 10
digit3 = n % 10

sum_of_digits = digit1 + digit2 + digit3
print(f"{digit1} + {digit2} + {digit3} = {sum_of_digits}")
