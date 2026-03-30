import functools, warnings
from typing import Callable, Any, List, Optional


# 1. Напишите рекурсивную функцию palindrome(s), которая проверяет, является ли строка палиндромом. Без срезов и reversed(), только рекурсия.
print("*" * 40)
print(
    "Задание №1: Напишите рекурсивную функцию palindrome(s), которая проверяет, является ли строка палиндромом."
)
print("*" * 40)


def palindrome(s: str) -> bool:
    """
    Рекурсивная функция проверки строки на палиндром.

    Палиндром - это строка, которая читается одинаково слева направо и справа налево.

    Args:
        s (str): строка для проверки
    Returns:
        bool: True если строка палиндром, False в противном случае
    """
    if (
        len(s) <= 1
    ):  # если строка будет пустой или содержит один символ, то она всегда палиндром
        return True
    if (
        s[0] != s[-1]
    ):  # если первый и последний символ не совпадут, то это уже точно не палиндром
        return False
    return palindrome(
        s[1:-1]
    )  # рекурсия, чтобы проверить  строку без первого и последнего символа. Проверяем "от второго символа до предпоследнего"


print("Тестируем работу функции palindrome: ")
print("_-" * 40)

print("казак ->", "палиндром" if palindrome("казак") else "не палиндром")
print("шалаш ->", "палиндром" if palindrome("шалаш") else "не палиндром")
print("hello ->", "палиндром" if palindrome("hello") else "не палиндром")
print("a ->", "палиндром" if palindrome("a") else "не палиндром")
print("101 ->", "палиндром" if palindrome("101") else "не палиндром")
print("2020 ->", "палиндром" if palindrome("2020") else "не палиндром")
print("", "палиндром" if palindrome("") else "не палиндром")

print("-" * 40)

# 2. Напишите функцию make_validator(min_val, max_val), которая возвращает функцию-валидатор. Валидатор принимает число и возвращает True если оно в диапазоне, иначе False.
# Для себя: делаем через замыкание (closures)
print("*" * 40)
print("Задание №2: Напишите функцию make_validator")
print("*" * 40)


def make_validator(min_val: float, max_val: float) -> Callable[[float], bool]:
    """
    Назначение:
        Создаёт функцию-валидатор для проверки чисел на вхождение в диапазон.
        Это функция высшего порядка, которая будет возвращать другую функцию.
    Args:
        min_val (float): минимальное допустимое значение (включительно)
        max_val (float): максимальное допустимое значение (включительно)
    Returns:
        Callable[[float], bool]: функция-валидатор, которая принимает число
        и возвращает True, если число в диапазоне, и False в противном случае
    """

    def validator(number: float) -> bool:
        """
        Назначение:
            Проверяет, находится ли число в заданном диапазоне
        Args:
            number (float): число для проверки
        Returns:
            bool: True если min_val <= number <= max_val, иначе False
        """
        return min_val <= number <= max_val

    return validator


print("Тестируем работу разных валидаторов: ")
print("_-" * 40)

water_temp_validator = make_validator(0, 100)
print("Проверяем температуру воды от 0 до 100:")
print(f"Температура 20°C: {water_temp_validator(20)}")
print(f"Температура -5°C: {water_temp_validator(-5)}")
print(f"Температура 100°C: {water_temp_validator(100)}")
print("_-" * 40)
height_validator = make_validator(50, 250)
print("Проверяем длину доски (от 50 до 250 см):")
print(f"Рост 175 см: {height_validator(175)}")
print(f"Рост 30 см: {height_validator(30)}")
print(f"Рост 300 см: {height_validator(300)}")
print("_-" * 40)
check_range = make_validator(15, 40)
numbers = [
    5,
    10,
    14.99,
    15,
    15.0000001,
    20,
    25,
    12,
    8,
    18,
    33,
    5,
    2,
    0,
    -1,
    2.7,
    33.7,
    -33.7,
    39.99999,
    40,
    40.0000000000001,
]
print(f"Проверяем входят ли {numbers} в диапазон от 15 до 40:")
for num in numbers:
    if check_range(num):
        print(f"Число {num} -> ВХОДИТ в диапазон")
    else:
        print(f"Число {num} -> НЕ входит в диапазон")


print("-" * 40)

# 3. Напишите декоратор @retry(n), который при возникновении любого исключения повторяет вызов функции до n раз. Если все попытки провалились — пробрасывает последнее исключение.
print("*" * 40)
print("Задание №3: Напишите декоратор @retry(n)")
print("*" * 40)

def retry(n: int) -> Callable:
    '''
    Декоратор, который повторяет вызов функции при возникновении исключения.

    Args:
        n (int): максимальное количество попыток
    Returns:
        Callabe: декоратор, оборачивающий функцию
    '''
    def decorator(func: Callable) -> Callable:
        '''
        Внутренняя функция-декоратор, которая оборачивает исходную функцию

        Args:
            func (Callable): функция, которую нужно обернуть
        Returns:
            Callble: обёрнутая функция с логикой повторных попыток
        '''
        # Сохраняем метаданные исходной функции (имя, документацию и т.д.)
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            '''
            Обёртка, которая выполняет функцию с повторными попытками

            Args:
                *args: позиционные аргументы для исходной функции
                **kwargs: именованные аргументы для исходной функци
            Returns:
                Any: результат вызова исходной функции
            Raises:
                Exception: последнее исключение, если все попытки неудачны
            '''
            last_exception = None # переменная, в которой будем хранить по итогу последнее исключение

            for attempt in range(1, n + 1):
                try:
                    result = func(*args, **kwargs)
                    print(f"Попытка {attempt}/{n}: Успешно ✅")
                    return result
                except Exception as e:
                    last_exception = e
                    print(f"Попытка {attempt}/{n}: ОШИБКА ❌ - {type(e).__name__}: {e}")
                    if attempt == n:
                        print(f"Все {n} попыток провалились!")
                        break
                    print(f"Повторяем... Осталось попыток: {n - attempt}")
            raise last_exception
        return wrapper
    return decorator

print("Тестируем работу декоратора: ")
print("_-" * 40)

print("=== Пример 1: Функция, которая работает с первой попытки ===\n")
@retry(3)
def always_works_function():
    pass
    return "Успешный результат!"

result = always_works_function()
print(f"Результат: {result}\n")

print("=== Пример 2: Функция, которая работает со второй попытки ===\n")
@retry(3)
def works_on_second_attempt():
    if not hasattr(works_on_second_attempt, "attempts"): # сделано для демонстрации, т.к. hasattr(объект, "имя_атрибута") - проверяет, есть ли у объекта атрибут с таким именем
        works_on_second_attempt.attempts = 0 # сделано для демонстрации, т.к. hasattr(объект, "имя_атрибута") - проверяет, есть ли у объекта атрибут с таким именем
    
    works_on_second_attempt.attempts += 1
    
    if works_on_second_attempt.attempts == 1:
        raise ValueError("Неверное значение")
    
    return f"Успех после {works_on_second_attempt.attempts} попыток!"

result = works_on_second_attempt()
print(f"Результат: {result}\n")

print("=== Пример 3: Функция, которая всегда падает ===\n")
@retry(3)
def always_fails():
    """Функция, которая всегда выбрасывает исключение"""
    raise ConnectionError("Сервер недоступен")

try:
    result = always_fails()
except Exception as e:
    print(f"Поймано исключение после всех попыток: {type(e).__name__}: {e}\n")

print("-" * 40)

# 4. Напишите декоратор @deprecated(message), который выводит предупреждение при вызове функции (через warnings.warn) и всё равно выполняет её. Сохраняйте метаданные через functools.wraps.
print("*" * 40)
print("Задание №4: Напишите декоратор @deprecated(message)")
print("*" * 40)

def deprecated(message: str) -> Callable:
    '''
    При вызове функции выводит предупреждение с указанным сообщением,
    но функция всё равно выполняется.
    
    Args:
        message (str): сообщение-предупреждение (например, объяснение, какую новую функцию использовать вместо устаревшей)
    Returns:
        Callable: декоратор, оборачивающий функцию
    '''
    def decorator(func: Callable) -> Callable:
        '''
        Внутренняя функция-декоратор, оборачивающая исходную функцию.
        '''
        # Сохраняем метаданные исходной функции (имя, документацию и т.д.)
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """
            Обёртка, которая выводит предупреждение и вызывает функцию.
            """
            # Выводим предупреждение
            # category=DeprecationWarning - специальный тип для устаревших функций
            # stacklevel=2 - показывает правильную строку в предупреждении
            warnings.warn(
                message, # Текст предупреждения
                category=DeprecationWarning, # Тип предупреждения
                stacklevel=2 # Уровень стека (чтобы указывало на вызов функции)
            )
            
            # Вызываем исходную функцию и возвращаем её результат
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

print("Тестируем работу декоратора @deprecated(message): ")
print("_-" * 40)

@deprecated("Функция old_calc устарела. Используйте new_calc()")
def old_calc(a: int, b: int) -> int:
    """Старая функция для вычислений"""
    return a + b

result = old_calc(5, 3)
print(f"Результат: {result}")
print(f"Имя функции: {old_calc.__name__}")  # Проверяем, что метаданные сохранились
print(f"Документация: {old_calc.__doc__}")

print("-" * 40)