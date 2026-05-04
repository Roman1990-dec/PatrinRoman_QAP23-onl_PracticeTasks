# 5. Напиши функцию password_checker(correct_password) которая возвращает вложенную функцию check(password).
#  Вложенная принимает пароль и возвращает True если совпадает, иначе False. Внешняя переменная с паролем не должна быть доступна снаружи.
print("=" * 50)
print("Задание №5: Проверка функции password_checker")
print("=" * 50)


def password_checker(correct_password):
    """
    Создает функцию для проверки пароля.
    """
    
    print(f"Создан проверяльщик для пароля: '{correct_password}'") # Хочу убедиться, что сorrect_password сохранился
    
    def check(password):
        """
        Проверяет пароль.
        """
        # Внутренняя функция имеет доступ к correct_password
        # даже после того, как внешняя функция завершилась
        result = password == correct_password
        
        if result:
            print(f"Пароль '{password}' принят")
        else:
            print(f"Пароль '{password}' отклонен")
        
        return result
    
    return check


print("Создаем проверяльщика")
checker = password_checker("secret123")

print("\nПроверяем пароли:")
checker("wrongpass")
checker("secret123")

# Для себя: так можно посмотреть, что correct_password недоступна напрямую
print(f"\nПопытка доступа к correct_password: {hasattr(checker, 'correct_password')}")
