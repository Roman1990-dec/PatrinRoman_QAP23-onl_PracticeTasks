import math
from typing import Union, Generator, Any, Callable, Optional
# Callable - функция, которая принимает Any и возвращает Any
# Optional - может быть какое-то значение или None, поэтому воспользуемся им


# 1. Используя filter() и lambda, отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа.
print("*" * 40)
print(
    "Задание №1: Используя filter() и lambda, отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа."
)
print("*" * 40)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(f"Исходные данныe: {numbers}")
print("Результат: ")
print(odd_numbers)

print("-" * 40)

# 2. Напишите функцию apply_operations(numbers, *operations), которая принимает список чисел и произвольное количество lambda-функций,
#  последовательно применяя каждую ко всему списку.
print("*" * 40)
print("Задание №2: Напишите функцию apply_operations(numbers, *operations)")
print("*" * 40)


def apply_operations(
    numbers: list[int | float], *operations: callable
) -> list[int | float]:
    """
    Последовательно применяет каждую операцию ко всему списку чисел

    Args:
        - numbers: список чисел
        - *operations: произвольное количество lambda-функций

    Returns:
        список после применения всех операций
    """
    result = numbers.copy()

    for operation in operations:
        result = list(map(operation, result))

    return result


numbers = [3, 5, 3, 6, 5]
result = apply_operations(
    numbers, lambda x: x * 5, lambda x: x + 1, lambda x: round(x * 2.4, 2)
)

print("Результат: ")
print(f"Исходные данныe: {numbers}")
print(result)

print("-" * 40)

# 3. Напишите генератор chunked(lst, size), который разбивает список на куски заданного размера и поочередно их выдает. Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5].
print("*" * 40)
print("Задание №3: Напишите генератор chunked")
print("*" * 40)


def chunked(lst: list, size: int) -> Generator[list, None, None]:
    """
    Генератор, который разбивает список на куски заданного размера.

    Args:
        lst: список, который нужно разбить
        size: размер одного куска (сколько элементов в каждом куске)

    Returns:
        Generator: генератор, который выдает куски списка
    """
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


numbers = [1, 3, 5, 7, 9, 12, 15, 18, 21]
size = 3
result = chunked(numbers, size)

print(f"Исходные данныe: {numbers}")
print(f"Размер разбиения: {size}")
for chunk in result:
    print(chunk)

print("-" * 40)

# 4. Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. Выведите первые 20.
print("*" * 40)
print("Задание №4: Напишите генератор prime_numbers")
print("*" * 40)


def is_prime(n: int) -> bool:
    """
    Проверяет, является ли число простым.

    Args:
        n (int): число для проверки

    Returns:
        bool: True, если число простое, False в противном случае
    """
    if n <= 1:  # 1 и числа меньше 1 не являются простыми
        return False

    if n == 2:  # 2 - единственное четное простое число
        return True

    if n % 2 == 0:  # Если число четное и больше 2 - оно не простое
        return False

    limit = int(math.sqrt(n)) + 1  # Проверяем делители от 3 до квадратного корня из n
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


def prime_numbers() -> Generator[int, None, None]:
    """
    Бесконечный генератор простых чисел.

    Returns:
        Generator[int, None, None]: генератор, который бесконечно выдает простые числа
    """
    num = 2  # Начинаем с 2 (первое простое число)

    while True:
        if is_prime(num):
            yield num  # Если число простое, возвращаем его
        num += 1  # Переходим к следующему числу


print("Первые 20 простых чисел:")
print("=" * 30)

primes = prime_numbers()

for i in range(20):
    prime = next(primes)
    print(f"{i + 1:2}. {prime}")

print("-" * 40)

# 5. Напишите функцию safe_convert(value, type_func), которая пытается преобразовать value
# с помощью переданной функции (например, int, float). При ошибке возвращает None.
print("*" * 40)
print("Задание №5: Напишите функцию safe_convert")
print("*" * 40)


def safe_convert(value: Any, type_func: Callable[[Any], Any]) -> Optional[Any]:
    """
    Преобразует значение с помощью функции

    Args:
        value: значение, которое нужно преобразовать
        type_func: функция преобразования (int, float, str и тд)

    Returns:
        Optional: Результат преобразования или None
    """
    try:
        result = type_func(value)
        return result
    except (ValueError, TypeError):
        return None


print("Тестируем преобразования: ")
print("_-" * 40)
print("Успешные преобразования: ")
print(safe_convert("456", int))
print(safe_convert("3.14", float))
print(safe_convert(789, str))
print("_-" * 40)
print("Неудачные преобразования: ")
print(safe_convert("abc", int))
print(safe_convert("hello", float))
print(safe_convert([1, 2, 3], int))

print("-" * 40)

# 6. Создайте собственный класс исключения NegativeNumberError.
# Напишите функцию sqrt_safe(n), которая считает квадратный корень из числа,
# но при отрицательном n выбрасывает NegativeNumberError с понятным сообщением.
print("*" * 40)
print("Задание №6: Создайте собственный класс исключения NegativeNumberError")
print("*" * 40)


class NegativeNumberError(Exception):
    """
    Исключение, которое выводиться при попытке взять квадратный корень
    из отрицательного числа.

    Наследуется от встроенного класса Exception.
    """

    # Для себя: Метод init в Python — это специальный метод, который автоматически вызывается при создании нового экземпляра класса.
    # Его основная задача — инициализировать объект, установив начальные значения его атрибутов
    def __init__(self, number: Union[int, float], message: str = None):
        """
        Конструктор исключения.

        Args:
            number: отрицательное число, вызвавшее ошибку
            message: пользовательское сообщение об ошибке
        """
        self.number = number

        if message is None:
            # Создаем стандартное сообщение
            self.message = f"Невозможно вычислить квадратный корень из отрицательного числа {number}"
        else:
            self.message = message

        super().__init__(self.message)  # Вызываем конструктор родительского класса


def sqrt_safe(n: int | float) -> float:
    """
    Вычисляет квадратные корень из числа

    Args:
        n: число, из которого нужно извлечь корень
    Returns:
        Квадратный корень из числа
    Exceptions:
        NegativeNumberError: если n < 0
        TypeError: если n не число
    """
    if not isinstance(
        n, (int, float)
    ):  # isinstance() в Python — это встроенная функция для проверки, является ли объект экземпляром указанного класса или одного из классов в цепочке наследования
        raise TypeError(f"Аргумент должен быть числом, получено {type(n).__name__}")

    if n < 0:
        raise NegativeNumberError(n)

    return math.sqrt(n)


print("=== Тестируем sqrt_safe ===\n")

print("1. Квадратный корень из 25:")
result = sqrt_safe(25)
print(f"   Результат: {result}\n")

print("2. Квадратный корень из 9:")
result = sqrt_safe(9)
print(f"   Результат: {result}\n")

print("3. Квадратный корень из 2:")
result = sqrt_safe(2)
print(f"   Результат: {result:.4f}\n")

print("4. Квадратный корень из 0:")
result = sqrt_safe(0)
print(f"   Результат: {result}\n")

print("5. Пытаемся взять корень из отрицательного числа:")
try:
    result = sqrt_safe(-4)
    print(f"   Результат: {result}")  # Эта строка не выполнится
except NegativeNumberError as e:
    print(f"   Поймано исключение: {e}")
    print(f"   Отрицательное число: {e.number}")

print("6. Пытаемся взять корень из строки abc:")
try:
    result = sqrt_safe("abc")
    print(f"   Результат: {result}")  # Эта строка не выполнится
except TypeError as e:
    print(f"   Поймано исключение: {e}\n")

print("-" * 40)

# 7. Напишите функцию-калькулятор calculator(a, b, op), где op — строка ("+", "-", "*", "/").
# Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов.
print("*" * 40)
print("Задание №7: Напишите функцию-калькулятор calculator")
print("*" * 40)


def calculator(a: int | float, b: int | float, op: str) -> Union[int, float]:
    """
    Просто калькулятор

    Args:
        a: первый аргумент (число)
        b: второй аргурмент (число)
        op: операция ("+", "-", "*", "/")
    Returns:
        Результат операции
    Exceptions:
        TypeError: если аргументы не числа
        ZeroDivisionError: если деление на ноль
        ValueError: если операция неизвестна
    """
    # Проверяем типы аргументов
    if not isinstance(a, (int, float)):
        raise TypeError(
            f"Первый аргумент должен быть числом, получено {type(a).__name__}"
        )
    if not isinstance(b, (int, float)):
        raise TypeError(
            f"Второй аргумент должен быть числом, получено {type(b).__name__}"
        )

    # Проверяем операцию и выполнение вычисления
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        # Проверяем деление на ноль
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        return a / b
    else:
        # Если операция неизвестна
        raise ValueError(f"Неизвестная операция '{op}'. Используйте: +, -, *, /")


print("\n=== Тестирование калькулятора ===\n")
print("1. Сложение: 10 + 5")
result = calculator(10, 5, "+")
print(f"   Результат: {result}\n")

print("2. Вычитание: 10 - 5")
result = calculator(10, 5, "-")
print(f"   Результат: {result}\n")

print("3. Умножение: 10 * 5")
result = calculator(10, 5, "*")
print(f"   Результат: {result}\n")

print("4. Деление: 10 / 5")
result = calculator(10, 5, "/")
print(f"   Результат: {result}\n")

print("5. Деление с дробным результатом: 10 / 3")
result = calculator(10, 3, "/")
print(f"   Результат: {result:.2f}\n")

print("6. Деление на ноль: 10 / 0")
try:
    result = calculator(10, 0, "/")
    print(f"   Результат: {result}")
except ZeroDivisionError as e:
    print(f"   Ошибка: {e}\n")

print("7. Неизвестная операция: 10 % 5")
try:
    result = calculator(10, 5, "%")
    print(f"   Результат: {result}")
except ValueError as e:
    print(f"   Ошибка: {e}\n")

print("8. Некорректный тип: '10' + 5")
try:
    result = calculator("10", 5, "+")
    print(f"   Результат: {result}")
except TypeError as e:
    print(f"   Ошибка: {e}\n")

print("9. Некорректный тип: None + 5")
try:
    result = calculator(None, 5, "+")
    print(f"   Результат: {result}")
except TypeError as e:
    print(f"   Ошибка: {e}\n")

print("10. Некорректный тип: 10 + '5'")
try:
    result = calculator(10, "5", "+")
    print(f"   Результат: {result}")
except TypeError as e:
    print(f"   Ошибка: {e}\n")


print("-" * 40)
