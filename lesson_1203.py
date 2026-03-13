"""
Попроси пользователя ввести 3 числа через пробел (одной строкой),
преобразуй их в список целых чисел с помощью map и выведи их сумму.
"""

numbers = input("Введите 3 числа: ")

list_number = numbers.split(sep=" ")
int_numbers = map(int, list_number)
target_list = list(int_numbers)

print(sum(target_list))
print(target_list)