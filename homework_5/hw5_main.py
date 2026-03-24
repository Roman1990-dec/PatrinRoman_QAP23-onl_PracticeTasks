# 4. Напиши модуль hw5_file_utils.py с тремя полностью аннотированными функциями:
# def read_lines(filename): ...
# def write_lines(filename, lines): ...
# def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь.
# В hw5_main.py импортируй и протестируй все три.

from hw5_file_utils import read_lines, write_lines, count_words, display_word_count


folder_path = r"D:\AQA_2026\PatrinRoman_QAP23-onl_PracticeTasks\homework_5"
# Для себя: r - raw string. Python: "Не обрабатывай обратные слеши \ как специальные символы, воспринимай их как обычные". Нужно для Windows!!!
text_file = folder_path + "\\test_text.txt"

print("=" * 50)
print("Задание №4: Проверка работы фукций read_lines, write_lines, count_words")
print("=" * 50)

# Проверка write_lines
print("\n1. Записываем данные в файл:")
test_data = [
    "Привет Python!",
    "Python такой Питон",
    "Питон сказал питону: Эй, Питон, ты такой Питон и хватит давить питона",
]
write_lines(text_file, test_data)

# 2. Тестируем read_lines
print("\n2. Читаем данные из файла:")
lines = read_lines(text_file)
for line in lines:
    print(f"  {line}")

# 3. Тестируем count_words
print("\n3. Подсчитываем слова:")
word_count = count_words(text_file)
display_word_count(word_count)
