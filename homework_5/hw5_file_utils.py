# 4. Напиши модуль hw5_file_utils.py с тремя полностью аннотированными функциями:
# def read_lines(filename): ...
# def write_lines(filename, lines): ...
# def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь.
# В hw5_main.py импортируй и протестируй все три.

from typing import List, Dict


def read_lines(filename: str) -> List[str]:
    """
    Функция используется для чтения файла и возвращает список строк.

    Args:
        filename (str): путь к файлу для чтения

    Returns:
        List[str]: список строк из файла
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file]

        print(f"Прочитано {len(lines)} строк из файла '{filename}'")
        return lines

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


def write_lines(filename: str, lines: List[str]) -> bool:
    """
    Записывает список строк в файл.

    Args:
        filename (str): путь к файлу для записи
        lines (List[str]): список строк для записи

    Returns:
        bool: True если запись успешна, False если произошла ошибка
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for line in lines:  # Записываем каждую строку с переносом
                file.write(line + "\n")

        print(f"Записано {len(lines)} строк в файл '{filename}'")
        return True

    except Exception as e:
        print(f"Ошибка при записи файла: {e}")
        return False


def count_words(filename: str) -> Dict[str, int]:
    """
    Подсчитывает, сколько раз каждое слово встречается в файле.

    Args:
        filename (str): путь к файлу для анализа

    Returns:
        Dict[str, int]: словарь, где ключ - слово, значение - количество вхождений

    Примечание:
        - Слова приводятся к нижнему регистру
        - Удаляются знаки препинания
        - Слова разделяются пробелами
    """
    import string

    word_count = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        # Приводим текст к нижнему регистру
        content = content.lower()

        # Удаляем знаки препинания
        # Для себя: string.punctuation содержит: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        for punct in string.punctuation:
            content = content.replace(punct, " ")

        # Разбиваем текст на слова (по пробелам и переносам строк)
        words = content.split()

        # Подсчитываем каждое слово
        for word in words:
            # Пропускаем пустые слова (если вдруг появятся)
            if word:
                # Если слово уже есть в словаре, увеличиваем счетчик
                if word in word_count:
                    word_count[word] += 1
                # Если слова нет, добавляем его со значением 1
                else:
                    word_count[word] = 1

        print(f"В файле '{filename}' найдено {len(words)} слов")
        print(f"Уникальных слов: {len(word_count)}")
        return word_count

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")
        return {}
    except Exception as e:
        print(f"Ошибка при подсчете слов: {e}")
        return {}


def display_word_count(word_count: Dict[str, int], top_n: int = None) -> None:
    """
    Красиво выводит словарь с подсчетом слов.

    Args:
        word_count (Dict[str, int]): словарь со словами и их количеством
        top_n (int, optional): показать только топ N слов
    """
    if not word_count:
        print("Словарь пуст")
        return

    # Сортируем слова по убыванию частоты
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Если указано top_n, показываем только первые N
    if top_n:
        sorted_words = sorted_words[:top_n]

    print("\n" + "=" * 40)
    print("СТАТИСТИКА СЛОВ:")
    print("=" * 40)

    for word, count in sorted_words:
        # Создаем визуальный индикатор частоты
        bar = "█" * min(count, 20)  # максимум 20 символов
        print(f"{word:15} : {count:3} {bar}")

    print("=" * 40)
