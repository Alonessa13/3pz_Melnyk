def list_conversion(input_str):
    try:
        numbers = list(map(float, input_str.split(",")))
        return (f"Сума: {sum(numbers)}\n"
                f"Середнє значення: {sum(numbers) / len(numbers)}")
    except ValueError:
        return "Помилка: Невірний формат введення. Використовуйте коми для розділення чисел."
# Приклад використання
user_input = input("Введіть числа, розділені комами: ")
print(list_conversion(user_input))
