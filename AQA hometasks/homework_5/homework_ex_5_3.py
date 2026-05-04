# 3. Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет
from datetime import date


print(":" * 40)
print(
    "Задание №3: Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет"
)
print(":" * 40)


def age_calculator(birth_date_str: str) -> int:
    """
    Функция вычисляет полное количество лет на текущую дату.

    Args:
        birth_date_str (str): дата рождения в формате 'dd/mm/yyyy'

    Returns:
        int: количество полных лет

    Exceptions:
        ValueError: Некорректные числа
        Exception: Неверный формат даты
    """
    try:
        parts = birth_date_str.split("/")

        if len(parts) != 3:
            print("Ошибка: Неверный формат! Используйте дд/мм/гггг")
            return None
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        birth_date = date(year, month, day)  # Проверяем, что дата существует

        today = date.today()  # Получаем текущую дату

        if birth_date > today:
            print("Ошибка: Дата рождения не может быть в будущем!")
            return None

        age = today.year - year
        if (
            (today.month < month) or (today.month == month and today.day < day)
        ):  # корректировка на случай, если день рождения ещё не было в этом году, без неё поулчим лишний год к возрасту
            age = age - 1

        return age
    except ValueError:
        print("Ошибка: Введите корректные числа! Используйте формат дд/мм/гггг")
        return None
    except Exception:
        print("Ошибка: Неверный формат даты! Используйте дд/мм/гггг")
        return None


birth_date_str = input("Введите вашу дату рождения (дд/мм/гггг): ")

age = age_calculator(birth_date_str)

if age is not None:
    print(f"\nВаш возраст: {age} полных лет")
else:
    print("\nНе удалось вычислить возраст. Попробуйте еще раз.")
