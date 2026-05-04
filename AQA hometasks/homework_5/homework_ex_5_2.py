# 2 Создай файл grades.txt, где каждая строка содержит имя студента и его оценку через запятую: Анна,85; Иван,72; Петр,91
# Напиши код который читает файл и добавляет в конец каждой строки статус: 'отлично' если оценка >= 90, 'хорошо' если >= 75, иначе 'удовлетворительно'.
# Сохрани результат в новый файл grades_with_status.txt.

print(":" * 40)
print(
    "Задание №2: Создай файл grades.txt, а потом примени условие задачи и сохрани результат в новый файл grades_with_status.txt"
)
print(":" * 40)

folder_path = r"D:\AQA_2026\PatrinRoman_QAP23-onl_PracticeTasks\homework_5"
# Для себя: r - raw string. Python: "Не обрабатывай обратные слеши \ как специальные символы, воспринимай их как обычные". Нужно для Windows!!!
grades_file = folder_path + "\\grades.txt"
grades_with_status_file = folder_path + "\\grades_with_status.txt"

"""
file - переменная, которая используется для СОЗДАНИЯ файла
input_file - переменная, которая используется для ЧТЕНИЯ содержимого созданного файла
output_file - переменная, которая используется для ЗАПИСИ результата задания в новый файл
"""

# Создаем файл с данными студентов
with open(grades_file, "w", encoding="utf-8") as file:
    file.write("Анна,85\n")
    file.write("Иван,72\n")
    file.write("Петр,91\n")

print("Файл 'grades.txt' создан!")
print("Содержимое файла:")
with open(grades_file, "r", encoding="utf-8") as file:
    print(file.read())

input_file = open(grades_file, "r", encoding="utf-8")
output_file = open(grades_with_status_file, "w", encoding="utf-8")

# Работа с данными в созданном файле, обработка требуемых условий
print("Структурируем полученные данные из файла grade.txt: ")
print("-" * 40)
for line in input_file:
    line = line.strip()
    parts = line.split(",")

    name = parts[0]
    grade = int(parts[1])

    print(f"Имя: {name}")
    print(f"Оценка: {grade}")

    if grade >= 90:
        status = "отлично"
    elif grade >= 75:
        status = "хорошо"
    else:
        status = "удовлетворительно"
    print(f"Статус: {status} ")

    new_line = f"{name},{grade},{status}\n"

    output_file.write(new_line)

input_file.close()
output_file.close()

print("=" * 50)
print("Проверка результата обработки и сохранения данных в файл: ")
print("=" * 50)

print("Содержимое файла 'grades_with_status.txt':")
print("-" * 40)
with open(grades_with_status_file, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
