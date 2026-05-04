# 1. Напиши функцию copy_file(source: str, destination: str) -> bool, которая читает содержимое файла source и записывает его в destination.
# Возвращает True если успешно. Проверь что файл-копия создался.
import os

print(":" * 40)
print("Задание №1: Напиши функцию copy_file")
print(":" * 40)


def copy_file(source: str, destination: str) -> bool:
    """
    Назначение: копирует содержимое файла source и записывает его в destination

    Args:
        source: путь к исходному файлу
        destination: путь к файлу-копии

    Returns:
        True если копирование успешно, False в противном случае
    """
    print("-" * 40)

    if not os.path.exists(source):
        print(f"ОШИБКА: Файл '{source}' не существует!")
        return False

    source_file = open(
        source, "r", encoding="utf-8"
    )  # исправление кодировки, иначе ошибка
    file_content = source_file.read()
    source_file.close()
    print(f"Прочитан файл '{source}'")

    print("-" * 40)

    dest_file = open(
        destination, "w", encoding="utf-8"
    )  # исправление кодировки, иначе ошибка
    dest_file.write(file_content)
    dest_file.close()
    print(f"Записан файл '{destination}'")

    check_file = open(
        destination, "r", encoding="utf-8"
    )  # исправление кодировки, иначе ошибка
    check_content = check_file.read()
    check_file.close()

    print("-" * 40)
    if file_content == check_content:
        print("Проверка пройдена: содержимое совпадает!")
        return True
    else:
        print("Ошибка: содержимое не совпадает!")
        return False


source = "D:/AQA_2026/PatrinRoman_QAP23-onl_PracticeTasks/homework_5/test_file.txt"
destination = (
    "D:/AQA_2026/PatrinRoman_QAP23-onl_PracticeTasks/homework_5/test_file_copy.txt"
)
result = copy_file(source, destination)

print(f"Результат: {result}\n")
print("*" * 40)
