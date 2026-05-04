# 1. Создай класс Library с атрибутом класса books = [] и методами add_book(title), remove_book(title) и show_books().
# Продемонстрируй, что список книг общий для всех объектов класса.
print("*" * 40)
print("Задание №1: Создай класс Library с атрибутом класса books и требуемыми методами")
print("*" * 40)


class Library:
    books: list[str] = []

    def add_book(self, title: str) -> None:
        """Добавляет книгу в общий список"""
        Library.books.append(title)
        print(f"Книга {title} добавлена")

    def remove_book(self, title: str) -> None:
        """Удаляет книгу из общего списка"""
        if title in Library.books:
            Library.books.remove(title)
            print(f"Книга {title}")
        else:
            print(f"Книга {title} не найдена")

    def show_books(self) -> None:
        """Показывает все книги в библиотеке"""
        if Library.books:
            print("Список книг:")
            for i, book in enumerate(
                Library.books, 1
            ):  # Для себя: enumerate можно использовать, чтобы нумеровать сущности в списке
                print(f" {i}.{book}")
        else:
            print("Библиотека пуста")


print("=== Создаем две библиотеки ===")
lib1 = Library()
lib2 = Library()

print("\n=== Добавляем книгу через lib1 ===")
lib1.add_book("Марсианин")

print("\n=== Проверяем через lib2, видна ли книга ===")
lib2.show_books()

print("\n=== Добавляем еще книги через lib2 ===")
lib2.add_book("Артемида")
lib2.add_book("Проект: Аве Мария")

print("\n=== Проверяем через lib1 ===")
lib1.show_books()

print("\n=== Удаляем книгу через lib1 ===")
lib1.remove_book("Артемида")

print("\n=== Удаляем книгу, которой нет, через lib2 ===")
lib2.remove_book("Война и мир")

print("\n=== Проверяем через lib2 ===")
lib2.show_books()

print("\n=== Создаем третий объект библиотеки ===")
lib3 = Library()
print("Новая библиотека видит все старые книги:")
lib3.show_books()

print("-" * 40)

# 2. Создай иерархию: базовый класс Employee с атрибутами name и salary, методом get_info().
# Дочерние классы Manager (добавляет department) и Developer (добавляет language).
# Каждый переопределяет get_info().
print("*" * 40)
print("Задание №2: Создай базовый класс Employee и дочерние к нему")
print("*" * 40)


class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def get_info(self) -> str:
        return f"Сотрудник: {self.name}, Зарплата: {self.salary} USD"


class Manager(Employee):
    def __init__(self, name: str, salary: int, department: str) -> None:
        super().__init__(name, salary)
        self.department = department

    def get_info(self) -> str:
        return f"{super().get_info()}, Отдел: {self.department}"


class Developer(Employee):
    def __init__(self, name: str, salary: int, language: str) -> None:
        super().__init__(name, salary)
        self.language = language

    def get_info(self) -> str:
        return f"{super().get_info()}, Язык: {self.language}"


print("=== Создаём сотрудников ===")

empl = Employee("Сергей Петров", 1000)
mngr = Manager("Роман Патрин", 2500, "QA")
dev = Developer("Иван Исупов", 3000, "Python")

print(empl.get_info())
print(mngr.get_info())
print(dev.get_info())

print("-" * 40)

# 3. Реализуй класс Stack (стек) с протектед атрибутом _items = [] и методами push(item),
#  pop(), peek() (посмотреть верхний элемент), is_empty() и size().
print("*" * 40)
print("Задание №3: Реализуй класс Stack (стек) с протектед атрибутом _items")
print("*" * 40)


class Stack:
    def __init__(self) -> None:
        """Конструктор создаёт пустой список для хранения данных/ элементов"""
        self._items = []

    def push(self, item) -> None:
        """Добавляет элемент на вершину стека"""
        self._items.append(item)
        print(f"Элемент {item} добавлен в стек")

    def pop(self) -> None:
        """Удаляет и возвращает верхний элемент стека"""
        if self.is_empty():
            print("Ошибка: стек пуст, нельзя удалить элемент")
            return None  # Возвращаем None, если стек пуст
        else:
            item = (
                self._items.pop()
            )  # если не указываем индекс, то pop должен удалить последний элемент
            print(f"Элемент {item} удален из стека")
            return item

    def peek(self) -> None:
        """Показываем верхний элемент стека, не удаляя его"""
        if self.is_empty():
            print("Стек пуст, нечего показывать")
            return None  # Возвращаем None, если стек пуст
        else:
            return self._items[-1]  # последний элемент списка (стека)

    def is_empty(self) -> None:
        """Проверяем пустой ли стек"""
        return len(self._items) == 0

    def size(self) -> int:
        """Возвращает количество элементов в стеке"""
        return len(self._items)

    def show(self) -> None:
        """Показывает весь стек"""  # доп метод для наглядности работы
        if self.is_empty():
            print("Стек пуст")
        else:
            print("Стек: ", self._items)


print("=== Проверка работы ===")

stack = Stack()  # создаём тестовый стек

print(f"Стек пуст? {stack.is_empty()}")
print(f"Размер стека: {stack.size()}")

stack.push("Яблоко")
stack.push("Банан")
stack.push("Киви")
stack.show()

print(f"\nРазмер стека: {stack.size()}")

top = stack.peek()
print(f"Верхний элемент: {top}")

item = stack.pop()  # должен удалиться Киви
print(f"Удаленный элемент: {item}")
stack.show()

item = stack.pop()  # теперь должен удалиться Банан
stack.show()

# остался один элемент (Яблоко), проверим стек на пустоту, а затем удалим последний элемент, проверим снова
print(f"Стек пуст? {stack.is_empty()}")
print(f"Верхний элемент: {stack.peek()}")

stack.pop()  # удалили Яблока
print(f"Стек пуст? {stack.is_empty()}")

stack.pop()  # список пуст, проверяем вывод условия
stack.peek()  # список пуст, проверяем вывод условия

print("-" * 40)

# 4. Создай класс Vehicle с методом move(), выводящим "Moving...". Создай дочерние классы Car,
# Boat и Plane, каждый переопределяет move() по-своему. Напиши функцию start_journey(vehicle),
# которая вызывает move() у любого переданного транспорта - продемонстрируй полиморфизм.
print("*" * 40)
print("Задание №4: Задача про транспортные средства")
print("*" * 40)


class Vehicle:
    """Базовый класс для всех транспортных средств"""

    def move(self) -> None:
        print("Moving ...")


class Car(Vehicle):
    def move(self) -> None:
        print("Машина едет по дороге, колонки бассят")


class Boat(Vehicle):
    def move(self) -> None:
        print("Лодка мчится по волнам, нравится")


class Plane(Vehicle):
    def move(self) -> None:
        print("Самолёт рассекает небеса, опаопапапа")


def start_journey(vehicle: Vehicle) -> None:
    print("Начинаем наше путешествие...")
    vehicle.move()
    print("Путешествие продолжается!\n")


# Создаем разные виды транспорта
car = Car()
boat = Boat()
plane = Plane()

# Создаем список из разных транспортных средств
transports = [car, boat, plane]

print("=== Проверка работы ТС ===")

start_journey(car)
start_journey(boat)
start_journey(plane)

for transp in transports:  # проверка полиморфизма в цикле
    transp.move()


print("-" * 40)

# 5. Создай класс Student с атрибутами name и grades (список оценок).
# Добавь методы add_grade(grade), average() (средняя оценка),
# highest() и lowest(). Защити grades через одиночное подчёркивание.
print("*" * 40)
print("Задание №5: Задача со студентиком")
print("*" * 40)


class Student:
    def __init__(self, name: str) -> None:
        """
        Конструктор студента

        Args:
            name: имя студента
        """
        self.name = name
        self._grades = []  # изначально пустой/ защищенный атрибут
        print(f"В системе создан студент: {self.name}")

    def add_grade(self, grade: int) -> None:
        """
        Добавление оценки

        Args:
            grade: цело число от 2 до 5
        """
        if 2 <= grade <= 5:
            self._grades.append(grade)
            print(f"Оценка {grade} добавлена студенту {self.name}")
        else:
            print(f"Ошибка: оценка {grade} не подходит (должна быть от 2 до 5)")

    def average(self) -> float:
        """
        Возвращение средней оценки

        Returns:
            float: среднее арифметическое всех оценок
        """
        if not self._grades:
            print("Нет оценок для подсчета среднего")
            return 0.0

        total = sum(self._grades)
        count = len(self._grades)
        avg = total / count
        return round(avg, 2)

    def highest(self) -> int:
        """
        Возвращение высшей оценки

        Returns:
            int: максимальная оценка
        """
        if not self._grades:
            print("Нет оценок для поиска максимальной")
        else:
            return max(self._grades)

    def lowest(self) -> int:
        """
        Возвращает наименьшую оценку

        Returns:
            int: минимальная оценка
        """
        if not self._grades:
            print("Нет оценок для поиска минимальной")
        else:
            return min(self._grades)

    def show_info(self) -> None:
        """Вся информация о студенте"""
        print(f"\n=== Информация о студенте {self.name} ===")
        print(f"Оценки: {self._grades if self._grades else 'нет оценок'}")

        if self._grades:
            print(f"Средняя: {self.average()}")
            print(f"Лучшая: {self.highest()}")
            print(f"Худшая: {self.lowest()}")
            print(f"Всего оценок: {len(self._grades)}")
        else:
            print("Оценок пока нет")


print("=== Проверка работы со студентиком ===")

student = Student("Роман Патрин")
print(f"Имя студента (публичный): {student.name}")  # незащищенный атрибут
print(f"Оценки (защищенный): {student._grades}")  # защищенный атрибут

print("\n=== Добавляем оценки через метод ===")
student.add_grade(1)  # Некорректная оценка (должна быть от 2 до 5)
student.add_grade(4)
student.add_grade(3)
student.add_grade(6)  # Некорректная оценка (должна быть от 2 до 5)
student.add_grade(5)

print("\n=== Выводим информацию ===")
student.show_info()

print("-" * 40)
