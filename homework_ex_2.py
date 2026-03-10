# 1. Привести к целому типу -1.6, 2.99
print("1. Привести к целому типу -1.6, 2.99")
first_number = int(-1.6)
second_number = int(2.99)

print(first_number)
print(type(first_number))
print(second_number)
print(type(second_number))
print("-"*100)

# 2. Заменить символ “#” на символ “/” в строке www.my_site.com#about
print("2. Заменить символ “#” на символ “/” в строке www.my_site.com#about")
text = "www.my_site.com#about"
new_text = text.replace("#", "/")
print("Было:", text)
print("Стало:", new_text)
print("-"*100)

# 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
print("3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’")
word="stroka"

new_word="".join([word,"ing"])

print("Было:",word)
print("Стало:",new_word)
print("-"*100)

# 4. В строке “Ivanou Ivan” поменяйте местами слова => “Ivan Ivanou”
print("4. В строке “Ivano""u Ivan” поменяйте местами слова => “Ivan Ivanou”")
source_text="Ivan Ivanou"

parts=source_text.split()
parts.reverse()
swapped_text=" ".join(parts)

print("Было:",source_text)
print("Стало:",swapped_text)
print("-"*100)

# 5. Напишите программу, которая удаляет пробел в начале, в конце строки
print("5. Напишите программу, которая удаляет пробел в начале, в конце строки")
text_example=" Привет "

text_wo_space=text_example.strip()

print("Было:",text_example)
print("Стало:",text_wo_space)
print("-"*100)

# 6. Создайте словарь, связав его с переменной school, и наполните его данными,
#  которые бы отражали количество учащихся в десяти разных классах 
# (например, 1а, 1б, 2б, 6а, 7в и т.д.)
print("6. Создайте словарь, связав его с переменной school, и наполните его данными")
school = {
    "1а": 25,
    "1б": 24,
    "2а": 26,
    "2б": 23,
    "3а": 22,
    "4б": 25,
    "6а": 24,
    "7а": 28,
    "8а": 26,
    "9в": 21
}

print("Словарь school:", school)
print("-"*100)

# 7. Создайте список и извлеките из него второй элемент
print("7. Создайте список и извлеките из него второй элемент")
car_parts=["дверь","фары","двигатель","бампер"]

second_car_part=car_parts[1]

print("Список: ",car_parts)
print("Второй элемент из списка: ",second_car_part)
print("-"*100)

# 8. Вывести входит ли строка1 в строку2 (пример: employ и employment)
print("8. Вывести входит ли строка1 в строку2 (пример: employ и employment)")
str1="employ"
str2="employment"

position = str2.find(str1)

if position != -1:
    print(f"'{str1}' найдена в '{str2}' на позиции {position}")
else:
    print(f"'{str1}' не найдена")

print("-"*100)

# 9. Вывести нужные символы
# x = “My name is Agent Smith”
# print(x[?]) #y
# print(x[?:?:?]) #nesgt
print("9. Вывести нужные символы из x = “My name is Agent Smith”: print(x[?]) #y и print(x[?:?:?]) #nesgt")
x = "My name is Agent Smith"

print("Извлекли y: ", x[1]) #y
print("Извлекли nesgt: ",x[3]+x[6]+x[9]+x[12]+x[15])
print("-"*100)

# 10*. Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, 
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5.
# Напишите программу, которая будет выводить уникальное число
print("10*. Задача с массивом")
source_data=[1,5,2,9,2,9,1]
print("Исходный массив:", source_data)
print("-"*40)

count={} # создаю пустой словарь, использую как счётчик

# ввел такой цикл, который будет добавлять в словарь кол-во чисел в массиве, проходя по каждому
for value in source_data:
    if value in count:
        count[value]+=1
    else:
         count[value]=1

print("Сколько раз встречается число в массиве:")
for value, value_count in count.items():
    print(f"  Число {value} встречается {value_count} раз(а)")

# Ищу число в полученном словаре, которое в массиве всего 1 раз, и вывожу его
for value, value_count in count.items():
    if value_count == 1:
        target_value = value
        break

print(f"Уникальное число: {target_value}")   
print("-"*100)