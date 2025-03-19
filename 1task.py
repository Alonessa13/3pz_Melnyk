def process_number(input_str):
    try:
        number = int(input_str)
    except ValueError:
        try:
            number = float(input_str)
        except ValueError:
            return "Помилка: введене значення не є числом"

    return str(number + 10)


user_input = input("Введіть число: ")
print("Результат:", process_number(user_input))
