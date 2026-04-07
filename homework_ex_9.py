from dataclasses import dataclass
import math


# 1. Создай класс Circle с protected атрибутом _radius.
# Добавь @property для radius (с проверкой: радиус > 0), и вычисляемые свойства area
# и perimeter через @property - они должны пересчитываться автоматически при изменении радиуса.
print("*" * 40)
print("Задание №1: Создай класс Circle и добавь @property")
print("*" * 40)


class Circle:
    """Класс, представляющий круг с радиусом"""

    def __init__(self, radius: float) -> None:
        """
        Конструктор для круга

        Args:
            radius: радиус круга (положительное число)
        """
        self.radius = radius  # вызывает сеттер @radius.setter
        print(f"Создан круг с радиусом {self.radius}")

    @property  # Для себя: Property (свойство) — это специальный декоратор, который позволяет методу выглядеть как обычный атрибут
    def radius(self) -> float:
        """
        Getter для радиуса - позволяет читать радиус как circle.radius
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """
        Setter для радиуса - вызывается при записи cirle.radius = значение
        """
        if value > 0:
            self._radius = value
            print(f"Радиус: {value}")
        else:
            raise ValueError(f"Радиус должен быть больше 0! Получено: {value}")

    @property
    def area(self) -> float:
        """
        Вычисляемое свойство: площадь круга.
        """
        return math.pi * self._radius**2

    @property
    def perimeter(self) -> float:
        """
        Вычисляемое свойство: длина окружности (периметр круга)
        """
        return 2 * math.pi * self._radius


print("=== Проверка работы ===")
circle = Circle(2.8)

print("\n=== Читаем радиус через property ===")
print(f"Радиус круга: {circle.radius}")
print("\n=== Находим площадь и периметр через property ===")
print(f"Площадь круга: {circle.area:.2f}")
print(f"Длина окружности: {circle.perimeter:.2f}")

print("\n=== Меняем радиус ===")
print("Меняем радиус на 10")
circle.radius = 10  # Здесь вызывается @radius.setter
print(f"Новый радиус: {circle.radius}")
print(f"Новая площадь: {circle.area:.2f}")  # автоматический пересчёт
print(f"Новая длина: {circle.perimeter:.2f}")  # автоматический пересчёт

print("\n=== Пробуем установить неправильный радиус ===")
try:
    circle.radius = -3  # проверяем работу с отрицательным числом
except ValueError as e:
    print(f"Ошибка: {e}")

print("\n=== Пробуем установить радиус 0 ===")
try:
    circle.radius = 0  # проверяем работу с 0
except ValueError as e:
    print(f"Ошибка: {e}")

print("-" * 40)

# 2. Создай класс Vector с атрибутами x и y.
# Реализуй магические методы __add__ (сложение двух векторов), __str__ (вывод в формате "Vector(x, y)"),
#  и __eq__ (сравнение).
# Проверь: Vector(1, 2) + Vector(3, 4) должен давать Vector(4, 6).
print("*" * 40)
print(
    "Задание №2: Создай класс Vector с атрибутами x и y и реализауй магические методы"
)
print("*" * 40)


class Vector:
    """Класс, представляющий вектор на плоскости с координатами x и y"""

    def __init__(self, x=float, y=float) -> None:
        """
        Конструктор вектора

        Args:
            x: координата по оси X
            y: координата по оси Y
        """
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        """
        Магический метод для оператора сложения (+).
        Вызывается при использовании: vector1 + vector2

        Args:
            other: другой вектор (то, что справа от +)

        Returns:
            Vector: новый вектор, равный сумме двух векторов
        """
        print(f"Складываем {self} и {other}")
        if not isinstance(other, Vector):  # проверим, что other тоже вектор
            raise TypeError(f"Нельзя сложить Vector с {type(other).__name__}")

        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vector(new_x, new_y)

    def __str__(self) -> str:
        """
        Магический метод для строкового представления.
        Вызывается автоматически при print(vector) или str(vector).

        Должен возвращать строку в формате "Vector(x, y)"
        """
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        """
        Магический метод для сравнения на равенство (==).
        Вызывается автоматически при vector1 == vector2.

        Возвращает True, если векторы равны (x и y совпадают)
        Возвращает False, если векторы разные или сравниваются с не-вектором
        """
        # Векторы равны, если равны их x и y
        return self.x == other.x and self.y == other.y


print("=== Создаем векторы ===")
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print("\n=== Проверяем вывод (__str__) ===")
print(f"v1 = {v1}")
print(f"v2 = {v2}")

print("\n=== Проверяем сложение (__add__) ===")
v3 = v1 + v2  # Здесь вызывается __add__
print(f"{v1} + {v2} = {v3}")
print("\n=== Проверяем результат ===")
print("Должно получиться: Vector(4, 6)")
print(f"Получили: {v3}")

print("\n=== Проверяем обработку ошибки ===")
try:
    result = v1 + 4
    print(f"Результат: {result}")
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n=== Проверяем сравнение (__eq__) ===")
v4 = Vector(1, 2)
v5 = Vector(1, 2)
v6 = Vector(5, 6)

print(f"{v1} == {v4} -> {v1 == v4}")  # True (1,2) == (1,2)
print(f"{v1} == {v2} -> {v1 == v2}")  # False (1,2) == (3,4)
print(f"{v1} == {v5} -> {v1 == v5}")  # True (1,2) == (1,2)
print(f"{v1} == {v6} -> {v1 == v6}")  # False (1,2) == (5,6)

print("-" * 40)

# 3. Создай класс Temperature с @property для celsius, fahrenheit и kelvin.
# При установке значения через любое свойство должны автоматически пересчитываться остальные.
# Хранить следует только одно внутреннее значение.
print("*" * 40)
print(
    "Задание №3: Создай класс Temperature с @property для celsius, fahrenheit и kelvin"
)
print("*" * 40)


class Temperature:
    """
    Класс для работы с температурой в разных шкалах.
    Внутри хранится только значение в Цельсиях
    """

    def __init__(self, celsius: float = 0) -> None:
        """
        Конструктор температуры. По умолчанию 0°C.

        Args:
            celsius: начальная температура в градусах Цельсия
        """
        self._celsius = celsius
        print(f"Создан объект Temparetare: {self._celsius} °C")

    @property
    def celsius(self) -> float:
        """Геттер для градусов Цельсия"""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Сеттер для градусов Цельсия"""
        self._celsius = value
        print(f"Установлена температура: {self._celsius} °C")

    @property
    def fahrenheit(self) -> float:
        """Геттер для градусов Фаренгейта"""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Сеттер для градусов Фарегейта"""
        self._celsius = (value - 32) * 5 / 9
        print(f"Установлена температура: {value}°F -> {self._celsius:.2f}°C")

    @property
    def kelvin(self) -> float:
        """Геттер для градусов в Кельвинах"""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float) -> float:
        """Сеттер для градусов Кельвинов"""
        self._celsius = value - 273.15
        print(f"Установлена температура: {value}K -> {self._celsius:.2f}°C")

    def __str__(self) -> str:
        return (
            f"Температура: {self.celsius:.2f}°C, "
            f"{self.fahrenheit:.2f}°F, "
            f"{self.kelvin:.2f}K"
        )


print("СОЗДАНИЕ ОБЪЕКТА")
print("=" * 50)

temp = Temperature(25.6)
print(temp)

print("\n" + "=" * 50)
print("УСТАНОВКА ЧЕРЕЗ ЦЕЛЬСИИ")
print("=" * 50)
temp.celsius = 100
print("После установки 100°C:")
print(f"  Цельсий: {temp.celsius}°C")
print(f"  Фаренгейт: {temp.fahrenheit:.2f}°F")
print(f"  Кельвин: {temp.kelvin:.2f}K")

print("\n" + "=" * 50)
print("УСТАНОВКА ЧЕРЕЗ ФАРЕНГЕЙТ")
print("=" * 50)
temp.fahrenheit = 212
print("\nПосле установки 212°F (температура кипения воды):")
print(temp)

print("\n" + "=" * 50)
print("УСТАНОВКА ЧЕРЕЗ КЕЛЬВИНЫ")
print("=" * 50)
temp.kelvin = 0
print("\nПосле установки 0K (абсолютный ноль):")
print(temp)

print("-" * 40)

# 4. Используй @dataclass для создания класса Point с полями x: float и y: float.
# Добавь метод distance_to(other: Point) - расстояние до другой точки.
# Затем создай дочерний @dataclass класс Point3D, добавив поле z: float, и переопредели distance_to.
print("*" * 40)
print(
    "Задание №4: Используй @dataclass для создания класса Point с полями x: float и y: float"
)
print("*" * 40)


@dataclass
class Point:
    """Класс для точки на плоскости (2D).
    @dataclass автоматически создает:
    - __init__(self, x, y)
    - __repr__(self) для вывода
    - __eq__(self, other) для сравнения"""

    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        """
        Вычисляет расстояние до другой точки
        Формула: √[(x2 - x1)² + (y2 - y1)²]

        Args:
            other: другая точка (объект Point)

        Returns:
            float: расстояние между точками
        """
        dx = self.x - other.x  # Разница координат по X
        dy = self.y - other.y  # Разница координат по Y

        distance_squared = dx**2 + dy**2

        distance = math.sqrt(distance_squared)

        return distance


@dataclass
class Point3D(Point):
    """
    Класс для точки в пространстве (3D).
    Наследует от Point, добавляет координату z.
    """

    z: float

    def distance_to(self, other: "Point3D") -> float:
        """
        Вычисляет расстояние до другой точки в 3D пространстве.
                Формула: √[(x2 - x1)² + (y2 - y1)² + (z2 - z1)²]

        Args:
            other: другая точка (объект Point3D)

        Returns:
            float: расстояние между точками
        """
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z

        distance_squared = dx**2 + dy**2 + dz**2

        distance = math.sqrt(distance_squared)

        return distance


print("\n" + "=" * 50)
print("РАБОТА С 2D ТОЧКАМИ (Point)")
print("=" * 50)

p1 = Point(1, 0)
p2 = Point(3, 6)
print(f"Точка p1: {p1}")
print(f"Точка p2: {p2}")

dist = p1.distance_to(p2)
print(f"\nРасстояние от {p1} до {p2}: {dist:.2f}")

print("\n" + "=" * 50)
print("РАБОТА С 3D ТОЧКАМИ (Point3D)")
print("=" * 50)

p3d_1 = Point3D(1, 0, 4)
p3d_2 = Point3D(2.5, 5.6, 10)
print(f"Точка p3d_1: {p3d_1}")
print(f"Точка p3d_2: {p3d_2}")

dist_3d = p3d_1.distance_to(p3d_2)
print(f"\nРасстояние от {p3d_1} до {p3d_2}: {dist_3d:.2f}")

print("-" * 40)
