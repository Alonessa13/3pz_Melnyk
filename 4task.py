def format_number(input_number, decimal_places=2):
    try:
        number = float(input_number)
        return f"Відформатоване число: {number:.{decimal_places}f}"
    except ValueError:
        return "Помилка: Введене значення не є числом."

# Приклад використання
user_input = input("Введіть число: ")
decimals = int(input("Введіть кількість десяткових знаків: "))
print(format_number(user_input, decimals))
