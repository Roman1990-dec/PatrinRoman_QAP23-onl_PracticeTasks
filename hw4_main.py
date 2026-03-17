print("Задача 7: Попроси пользователя ввести число. Возведи число в квадрат, в куб и проверь чётность.")
print("*" * 40)

"""
Главная программа, которая использует созданнфй модуль math_utils
"""
import hw4_maths_utils

def main() -> None:
    """
    Функция программы:
    Запрашивает число у пользователя и возводит число в квадрат, в куб и проверяет чётность
    """
    print("Математические вычисления")
    print("=" * 40)

    user_input = input("Введите число: ")
    try:
        number = float(user_input) # преобразуем ввод в число (float, чтобы поддерживать дробные)

        squared = hw4_maths_utils.square(number)
        cubed = hw4_maths_utils.cube(number)
        even_check = hw4_maths_utils.is_even(number)
       
        print("\n" + "=" * 40)
        print("Результат:")
        print(f"Введенное число: {number}")
        print(f"Квадрат числа: {squared}")
        print(f"Куб числа: {cubed}")
        if even_check:
            print(f"Четность: число ЧЕТНОЕ")
        else:
            print(f"Четность: число НЕЧЕТНОЕ")
    except ValueError:
        print("Ошибка! Введено некорректное число!")


if __name__ == "__main__":
    main()
