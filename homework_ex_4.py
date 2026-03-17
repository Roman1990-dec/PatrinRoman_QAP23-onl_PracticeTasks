# 1. Напиши код который выведет таблицу умножения до 10 на N (введенное с клавиатуры) в таком формате
print(
    "Задание №1: Напиши код, который выведет таблицу умножения до 10 на N в заданном формате"
)
print("*" * 40)

try:
    N = int(input("Введите число N: "))

    for i in range(1, 11):
        product_result = N * i
        if i < 10:
            print(f"{product_result} | ", end="")
    else:
        print(f"{product_result}")

except ValueError:
    print("Ошибка: введите целое число!")

print("*" * 40)


# 2. Попроси пользователя ввести имя и возраст. Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»
print(
    "Задание №2: Попроси пользователя ввести имя и возраст. Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»"
)
print("*" * 40)

your_name = input("Введите ваше имя: ")
your_age = int(input("Введите ваш возраст: "))

aging = [your_age + 10]
years = ["Через 10 лет тебе будет"]

for a, b in zip(years, aging):
    print(f"{a} {b} лет, {your_name}!")

print("*" * 40)


# 3. Даны два списка цен в долларах и курс валюты. Используй map чтобы перевести все цены в рубли. Затем используй zip чтобы создать словарь {товар: цена_в_рублях}:
print(
    "Задание №3: Даны два списка цен в долларах и курс валюты. Используй map чтобы перевести все цены в рубли. Затем используй zip чтобы создать словарь -> товар: цена_в_рублях"
)
print("*" * 40)

items = ["хлеб", "молоко", "кофе"]
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2


# Определение функции на конвертацию USD>RUB
def convert_to_rubles(price: float) -> float:
    return round(price * rate, 2)


print("Прай-лист на продукты в USD")
print()
price_dict_usd = dict(zip(items, prices_usd))
print(price_dict_usd)
print()

print(f"Прай-лист на продукты в RUB при курсе {rate}")
print()
prices_rub = list(map(convert_to_rubles, prices_usd))
price_dict_rus = dict(zip(items, prices_rub))
print(price_dict_rus)
print()

print("*" * 40)


# 4. Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку:
#'Fizz' если делится на 3, 'Buzz' если делится на 5, 'FizzBuzz' если делится на оба, иначе само число в виде строки. Вызови её для чисел от 1 до 20 через map.

print(
    "Задание №4: Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку по условию"
)
print("*" * 40)


def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


task_range = range(1, 21)
result = list(map(fizzbuzz, task_range))

print(result)
print("*" * 40)


# 5. Напиши функцию *args с именем my_stats которая принимает любое количество чисел и возвращает сразу три значения — минимум, максимум и среднее.


# 6. Напиши функцию build_profile(**kwargs) которая принимает любые именованные аргументы и
# возвращает словарь с этими данными плюс автоматически добавляет ключ 'registered': True. Добавь к функции docstring.


# 7. Создай модуль math_utils.py с тремя функциями: square(n) — возводит в квадрат, cube(n) — возводит в куб,
# is_even(n) — возвращает True/False. В main.py импортируй модуль, попроси пользователя ввести число через input, примени все три функции и выведи результаты.
# Защити вызовы конструкцией if __name__ == "__main__".
