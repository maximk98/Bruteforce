import time

# Словарь паролей (может быть заменен на более длинный список для тестов)
passwords_dictionary = [
    "123456", "password", "qwerty", "abc123", "iloveyou", "admin", "letmein", "welcome", "monkey",
    "sunshine", "123456789", "password1", "111111", "qwerty123", "654321", "password123"
]

# Целевой пароль, который мы пытаемся подобрать
target_password = "welcome"  # Меняйте для тестов с разными паролями

# Начало измерения времени
start_time = time.time()

# Брутфорс подбор по словарю
def brute_force_password(dictionary, target):
    for attempt in dictionary:
        if attempt == target:
            return attempt
    return None

# Запускаем брутфорс и фиксируем результат
result = brute_force_password(passwords_dictionary, target_password)

# Окончание измерения времени
end_time = time.time()
elapsed_time = end_time - start_time

# Вывод результата
if result:
    print(f"Пароль найден: '{result}'")
else:
    print("Пароль не найден в словаре")

print(f"Время, затраченное на взлом: {elapsed_time:.4f} секунд")
